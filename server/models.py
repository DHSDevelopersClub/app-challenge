'''NDB models.'''

from google.appengine.ext import ndb


class User(ndb.Model):
    '''One user'''
    account = ndb.UserProperty()
