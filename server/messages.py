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

class Activity(messages.Message):
    activity_id = messages.IntegerField(1) # optional
    user_created_disrcription = messages.StringField(2)
    location_lat = messages.IntegerField(3, required=True)
    location_long = messages.IntegerField(4, required=True)

class ActivityList(messages.Message):
    activites = messages.MessageField(Activity, 1, repeated=True)


class StatusMessage(messages.Message):
    status = messages.EnumField(Status, 1, required=True)
