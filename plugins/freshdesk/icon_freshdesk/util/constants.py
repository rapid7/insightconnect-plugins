class Attachment:
    NAME = "name"
    CONTENT = "content"


class Ticket:
    ID = "id"
    ATTACHMENTS = "attachments"
    CUSTOM_FIELDS = "custom_fields"
    SOURCE = "source"
    PRIORITY = "priority"
    STATUS = "status"

    FIELDS_TO_NAME_ID_CONVERSION = [STATUS, PRIORITY, SOURCE]


class TicketField:
    NAME = "name"
    CHOICES = "choices"


class Include:
    STATS = "stats"
    CONVERSATIONS = "conversations"
    COMPANY = "company"
    REQUESTER = "requester"

    @classmethod
    def get_include_parameters_list(cls):
        return [cls.STATS, cls.CONVERSATIONS, cls.COMPANY, cls.REQUESTER]
