'''Endpoints messages.'''

from protorpc import messages, message_types


class Status(messages.Enum):
    OK = 1
    MISSING_DATA = 2
    EXISTS = 3
    BAD_DATA = 4
    ERROR = 5
    NOT_LOGGED_IN = 6

class EditUser(messages.Message):
    '''Edit user or update profile'''
    class Sex(messages.Enum):
        MALE = 0
        FEMALE = 1
        OTHER = 2
    name = messages.StringField(1, required=True)
    age = messages.IntegerField(2, required=True)
    sex = messages.EnumField(Sex, 3, required=True)


class StatusMessage(messages.Message):
    status = messages.EnumField(Status, 1, required=True)
