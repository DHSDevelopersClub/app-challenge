"""The endpoints server."""
# https://docs.google.com/drawings/d/1DnJy1rjOXMD7PLMm0Yr1MbEKpViYM2HvmnrgWycSwZU/edit?usp=sharing
# pylint: disable=W0232, E0401, E1101, E0611, R0201, C0103

import urllib2
import json
import endpoints
from protorpc import message_types, remote, messages
from google.appengine.api import urlfetch
import google.appengine.api.users
import models
import messages

API_EXPLORER = '292824132082.apps.googleusercontent.com'
CLIENT_IDS = ['651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com',
              API_EXPLORER]

__author__ = 'Sebastian Boyd, Duncan Grubbs'
__copyright__ = 'Copyright (C) 2016 SB Technology Holdings International'

@endpoints.api(name='backend', version='v1')
class BackendAPI(remote.Service):
    '''backend api'''
    @endpoints.method(messages.EditUser,
                      messages.StatusMessage,
                      name='insert_user',
                      path='insert_user',
                      http_method='POST')
    def insert_user(self, request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException('Invalid token.')

        # check user existance
        user = models.User.query(models.User.account == current_user).get()

        if user:
            # EXISTS
            for r in request:
                pass
        else:
            # User not registered, add user
            user = models.User(account=current_user, name=request.name, age=request.age, sex=request.sex)
            user.put()

        return messages.StatusMessage(status=messages.Status.OK)

    @endpoints.method(messages.Activity,
                      messages.ActivityList,
                      name='get_activities',
                      path='get_activities',
                      http_method='POST')
    def get_activities(self, request):
        fake_activities = [
                            messages.Activity(
                                activity_id=0,
                                user_created_disrcription="have fun at Stinson Beach",
                                location_lat=0,
                                location_long=0),
                            messages.Activity(
                                activity_id=666,
                                user_created_disrcription="sell my soul",
                                location_lat=0,
                                location_long=0),
                            messages.Activity(
                                activity_id=404,
                                user_created_disrcription="can't find anything ot do",
                                location_lat=0,
                                location_long=0),
                           ]
        return messages.ActivityList(activites=fake_activities)

    # def list_users(self, request):
    #     pass



application = endpoints.api_server([BackendAPI])
