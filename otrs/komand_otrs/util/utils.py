import maya
import komand


class PyOTRSUtils(komand.Action):

    def add_pendingtime(self, client, pendingtime, ticket_id):
        # Format date
        try:
            pending_time = maya.MayaDT.from_rfc3339(pendingtime)
        except Exception as e:
            raise Exception("Error with Pending Time. Date may not be formatted correctly")
        time_now = maya.now()
        # create Timedelta
        time_diff = pending_time - time_now
        # get days and hours
        days, hours = time_diff.days, time_diff.seconds // 3600
        try:
            client.ticket_update_set_pending(ticket_id=ticket_id, pending_days=days, pending_hours=hours)
        except Exception as e:
            if "TicketUpdate: User does not have access to the ticket!" in e.message:
                raise Exception(f"Ticket {ticket_id} may not exist or user does not have access to the ticket\n"
                                f"Error: {e}")
            else:
                self.logger.error(f"An error occurred while updating the pending time: {e}")

    def add_sla(self, client, sla, sla_service, ticket_id):
        try:
            client.ticket_update(ticket_id=ticket_id, SLA=sla, Service=sla_service)
        except Exception as e:
            if "TicketUpdate: User does not have access to the ticket!" in e.message:
                raise Exception(f"Ticket {ticket_id} may not exist or user does not have access to the ticket\n"
                                f"Error: {e}")
            else:
                self.logger.error(f"An error occurred while updating the SLA: {e}")
                raise
