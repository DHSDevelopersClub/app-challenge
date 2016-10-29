'''Endpoints messages.'''

from protorpc import messages, message_types


class Status(messages.Enum):
    OK = 1
    MISSING_DATA = 2
    EXISTS = 3
    BAD_DATA = 4
    ERROR = 5
    NOT_LOGGED_IN = 6

class User(messages.Message):
    '''Edit user or update profile'''
    class Sex(messages.Enum):
        MALE = 0
        FEMALE = 1
        OTHER = 2
    name = messages.StringField(1)
    age = messages.IntegerField(2)
    sex = messages.EnumField(Sex, 3)

class Activity(messages.Message):
    activity_id = messages.IntegerField(1) # optional
    user_created_description = messages.StringField(2)
    lat = messages.IntegerField(3)
    lng = messages.IntegerField(4)

class ActivityResponse(messages.Message):
    activity_id = messages.IntegerField(1)
    description = messages.StringField(2)
    distance = messages.FloatField(3)
    user = messages.MessageField(User, 4)

class ActivityRequest(messages.Message):
    activity_id = messages.IntegerField(1)
    min_age = messages.IntegerField(2)
    max_age = messages.IntegerField(3)
    lat = messages.IntegerField(4)
    lng = messages.IntegerField(5)
    cursor = messages.StringField(6)

class ActivityList(messages.Message):
    activites = messages.MessageField(ActivityResponse, 1, repeated=True)
    cursor = messages.StringField(2)

class StatusMessage(messages.Message):
    status = messages.EnumField(Status, 1, required=True)
