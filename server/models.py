'''NDB models.'''

from google.appengine.ext import ndb
import geo.geomodel

class User(ndb.Model):
    '''One user'''
    account = ndb.UserProperty()
    name = ndb.StringProperty()
    age = ndb.IntegerProperty()
    sex = ndb.IntegerProperty() # 0 = male, 1 = female, 2 = other

class Activity(geo.geomodel.GeoModel, ndb.Model):
    activity_id = ndb.IntegerProperty()
    user_created_disrcription = ndb.StringProperty()
    zip_code = ndb.IntegerProperty()
