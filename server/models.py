'''NDB models.'''

from google.appengine.ext import ndb


class User(ndb.Model):
    '''One user'''
    account = ndb.UserProperty()
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    sex = ndb.IntegerProperty() # 0 = male, 1 = female, 2 = other

class Activity(ndb.Model):
    activity_id = ndb.IntegerProperty()
    user_created_disrcription = ndb.StringProperty()
    location_lat = ndb.IntegerProperty()
    location_long = ndb.IntegerProperty()
