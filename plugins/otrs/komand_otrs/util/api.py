import mimetypes
from datetime import datetime, timezone
from functools import wraps
from logging import Logger
from typing import Any, Callable, Optional

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import clean
from pyotrs import Article, Attachment, Client, DynamicField, Ticket
from pyotrs.lib import HTTPError, PyOTRSError

from komand_otrs.util.constants import (
    NO_ACCESS_MESSAGE,
    SESSION_ASSISTANCE,
    SESSION_CAUSE,
)


def with_session(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self: "OTRSAPI", *args: Any, **kwargs: Any) -> Any:
        try:
            self.create_session()
            return method(self, *args, **kwargs)
        except HTTPError as error:
            raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=error) from error
        except (PyOTRSError, ValueError) as error:
            if NO_ACCESS_MESSAGE in str(error):
                raise PluginException(preset=PluginException.Preset.UNAUTHORIZED, data=error) from error
            raise PluginException(preset=PluginException.Preset.BAD_REQUEST, data=error) from error
        finally:
            # Every call gets a fresh session, so don't keep the token or the last response around
            self.client.session_id_store.value = None
            self.client.result_json = None
            self.client.result = []

    return wrapper


class OTRSAPI:
    def __init__(self, server: str, username: str, password: str, logger: Logger) -> None:
        self.client = Client(server, username, password)
        self.logger = logger

    def create_session(self) -> None:
        # PyOTRS falls back to a legacy session ID on its own for OTRS 7 and older
        try:
            created = self.client.session_create()
        except (PyOTRSError, ValueError) as error:
            raise PluginException(cause=SESSION_CAUSE, assistance=SESSION_ASSISTANCE, data=error)
        # Looks like PyOTRS returns `False` when the reply holds neither an access token nor a session ID
        if not created:
            raise PluginException(
                cause=SESSION_CAUSE,
                assistance=SESSION_ASSISTANCE,
                data="OTRS returned neither an access token nor a session ID",
            )

    @with_session
    def test_connection(self) -> None:
        # Opening the whole session is the test here, so that we just return
        return

    @with_session
    def create_ticket(
        self,
        title: str,
        queue: str,
        ticket_type: str,
        state: str,
        priority: str,
        customer_user: str,
        lock: str,
        service: str,
        sla: str,
        pending_time: str,
        owner: str,
        responsible: str,
        article: dict[str, Any],
        attachments: list[dict[str, Any]],
        dynamic_fields: list[dict[str, Any]],
    ) -> dict[str, int]:
        # Clean the basics, as it won't handle empty items
        basics = clean(
            {
                "Title": title,
                "Queue": queue,
                "Type": ticket_type,
                "State": state,
                "Priority": priority,
                "CustomerUser": customer_user,
            }
        )

        # Create a ticket with the basic information
        created = self.client.ticket_create(
            ticket=Ticket.create_basic(**basics),
            article=self._build_article(article),
            attachments=self._build_attachments(attachments),
            dynamic_fields=[DynamicField(**field) for field in dynamic_fields],
            **clean(
                {
                    "Lock": lock,
                    "Service": service,
                    "SLA": sla,
                    "Owner": owner,
                    "Responsible": responsible,
                }
            ),
        )

        # Get the ticket id from the created ticket
        ticket_id = created.get("TicketID")

        # Set the pending time, OTRS rejects it on create as it wants year, month, day, hour and minute
        self._set_pending_time(ticket_id, pending_time)

        # Set the SLA and Service
        if sla:
            self._set_sla(ticket_id, sla, service)
        return self._ticket_reference(created)

    @with_session
    def update_ticket(
        self,
        ticket_id: int,
        priority: str,
        pending_time: str,
        lock: str,
        service: str,
        sla: str,
        queue: str,
        responsible: str,
        title: str,
        customer_user: str,
        ticket_type: str,
        no_article: bool,
        article: dict[str, Any],
        attachments: list[dict[str, Any]],
        dynamic_fields: list[dict[str, Any]],
    ) -> dict[str, int]:
        # Set the pending time
        self._set_pending_time(ticket_id, pending_time)

        # Skip the article and attachments when No Article is set
        updated = self.client.ticket_update(
            ticket_id,
            article=None if no_article else self._build_article(article),
            attachments=[] if no_article else self._build_attachments(attachments),
            dynamic_fields=[DynamicField(**field) for field in dynamic_fields],
            **clean(
                {
                    "Priority": priority,
                    "Lock": lock,
                    "Service": service,
                    "SLA": sla,
                    "Queue": queue,
                    "Responsible": responsible,
                    "Title": title,
                    "CustomerUser": customer_user,
                    "Type": ticket_type,
                }
            ),
        )
        return self._ticket_reference(updated)

    @with_session
    def get_ticket(self, ticket_id: int) -> dict[str, Any]:
        ticket = self.client.ticket_get_by_id(ticket_id, articles=True, attachments=True, dynamic_fields=True)
        return self._format_ticket(clean(ticket.to_dct()).get("Ticket", {}))

    @with_session
    def search_tickets(
        self,
        queue: str,
        customer_id: str,
        external_parameters: list[dict[str, Any]],
        dynamic_fields: list[dict[str, Any]],
    ) -> list[str]:
        # Initialize the search parameters
        search_parameters = {}

        # If queue is provided add it to the search parameters
        if queue:
            search_parameters["Queues"] = queue

        # If customer ID is provided add it to the search parameters
        if customer_id:
            search_parameters["CustomerID"] = customer_id

        # Add external parameters if any
        for parameter in external_parameters:
            search_parameters.update(parameter)

        # If dynamic fields are provided add them to the search parameters
        if dynamic_fields:
            search_parameters["dynamic_fields"] = [
                DynamicField(
                    name=field.get("name"),
                    value=field.get("value"),
                    search_operator=field.get("operation", "Equals"),
                    search_patterns=field.get("patterns"),
                )
                for field in dynamic_fields
            ]
        return self.client.ticket_search(**search_parameters)

    def _set_pending_time(self, ticket_id: int, pending_time: str) -> None:
        # Skip when it is left unmodified
        if not pending_time or pending_time.startswith("0001-01-01"):
            return

        # Convert string to datetime object
        try:
            pending = datetime.fromisoformat(pending_time)
        except ValueError as error:
            raise PluginException(
                cause="Error with Pending Time.",
                assistance="Date may not be formatted correctly. Use RFC 3339, e.g. 2026-11-01T12:00:00Z.",
                data=error,
            ) from error

        # Pending time needs to be in the future and have timezone info
        if pending.tzinfo is None:
            pending = pending.replace(tzinfo=timezone.utc)

        # Calculate the time difference between now and the pending time
        time_difference = pending - datetime.now(timezone.utc)

        # Update the ticket with the pending time
        try:
            self.client.ticket_update_set_pending(
                ticket_id=ticket_id, pending_days=time_difference.days, pending_hours=time_difference.seconds // 3600
            )
        except (PyOTRSError, ValueError) as error:
            if NO_ACCESS_MESSAGE in str(error):
                raise
            # This is a workaround for a bug in PyOTRS where it doesn't properly handle errors
            self.logger.error(f"An error occurred while updating the pending time: {error}")

    def _set_sla(self, ticket_id: int, sla: str, service: str) -> None:
        # Set the SLA and Service
        self.client.ticket_update(ticket_id=ticket_id, SLA=sla, Service=service)

        # Make sure the SLA was set
        details = self.client.ticket_get_by_id(
            ticket_id, articles=False, attachments=False, dynamic_fields=False, html_body_as_attachment=False
        ).to_dct()
        if details.get("Ticket", {}).get("SLAID") == "":
            raise PluginException(
                cause="SLA and Service was not set.",
                assistance="Please check the SLA and Service parameters as they maybe set incorrectly! "
                f"Please note ticket ID:{ticket_id} was created but the SLA and Service parameters were not updated.",
                data=f"SLA Parameter: {sla}, SLA Service parameter: {service}",
            )

    def _format_ticket(self, ticket: dict[str, Any]) -> dict[str, Any]:
        # OTRS returns some numbers as strings, but the output schema expects integers
        for article in ticket.get("Article", []):
            self._format_article(article)

        # Escalation times come back as numeric strings, leave them alone if they are empty
        self._format_escalation_times(ticket)

        # Dynamic field value is a single str or int for some fields and a list for others, make it a list
        if ticket.get("DynamicField"):
            ticket["DynamicField"] = self._format_dynamic_fields(ticket.get("DynamicField"))

        # The type ID is the only ID that comes back as an integer, but the output schema expects a string
        if "TypeID" in ticket:
            ticket["TypeID"] = str(ticket.get("TypeID"))

        # Convert the ticket ID
        if "TicketID" in ticket:
            ticket["TicketID"] = int(ticket.get("TicketID"))
        return ticket

    @staticmethod
    def _build_article(article: dict[str, Any]) -> Optional[Article]:
        # We need to clean the article, as it won't handle ampty items
        cleaned_article = {key: value for key, value in clean(article).items() if value != []}
        return Article(cleaned_article) if cleaned_article else None

    @staticmethod
    def _build_attachments(attachments: list[dict[str, Any]]) -> list[Attachment]:
        return [
            Attachment.create_basic(
                Content=attachment.get("content"),
                ContentType=mimetypes.guess_type(attachment.get("filename"))[0],
                Filename=attachment.get("filename"),
            )
            for attachment in attachments
        ]

    @staticmethod
    def _ticket_reference(result: dict[str, Any]) -> dict[str, int]:
        # OTRS returns both as strings, but they are integers in the output schema
        return {"TicketID": int(result.get("TicketID")), "TicketNumber": int(result.get("TicketNumber"))}

    @staticmethod
    def _format_article(article: dict[str, Any]) -> None:
        # Convert the numeric fields in the article
        for key in ("IsVisibleForCustomer", "TicketID", "NoAgentNotify"):
            if key in article:
                article[key] = int(article.get(key))

        # Convert the attachment file sizes
        for attachment in article.get("Attachment", []):
            if "FilesizeRaw" in attachment:
                attachment["FilesizeRaw"] = int(attachment.get("FilesizeRaw"))

    @staticmethod
    def _format_escalation_times(ticket: dict[str, Any]) -> None:
        # Convert only the numeric values, an escalation time is an empty string when no escalation is set
        for key in ("EscalationTime", "EscalationResponseTime", "EscalationSolutionTime", "EscalationUpdateTime"):
            value = ticket.get(key)
            if isinstance(value, str) and value.isnumeric():
                ticket[key] = int(value)

    @staticmethod
    def _format_dynamic_fields(fields: list[dict[str, Any]]) -> list[dict[str, Any]]:
        # Wrap a single value in a list and drop the fields that have no value
        return [
            {
                **field,
                "Value": (
                    [str(field.get("Value"))] if isinstance(field.get("Value"), (str, int)) else field.get("Value")
                ),
            }
            for field in fields
            if "Value" in field
        ]
