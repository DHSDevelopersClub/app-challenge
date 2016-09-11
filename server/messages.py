'''Endpoints messages.'''

from protorpc import messages, message_types


class Status(messages.Enum):
    OK = 1
    MISSING_DATA = 2
    EXISTS = 3
    BAD_DATA = 4
    ERROR = 5

class AddUser(messages.Message):
    name = messages.StringField(1, required=True)

class StatusMessage(messages.Message):
    status = messages.EnumField(Status, 1, required=True)
