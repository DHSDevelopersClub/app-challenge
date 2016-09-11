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
    @endpoints.method(messages.AddUser,
                      messages.StatusMessage,
                      name='insert_user',
                      path='user',
                      http_method='POST')
    def insert_user(self, request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException('Invalid token.')

        # check user existance
        if models.User.query(models.User.account == current_user).get():
            return messages.StatusMessage(status=messages.Status.EXISTS)

        # User not registered, add user
        user = models.User(account=current_user)
        user.put()

        return messages.StatusMessage(status=messages.Status.OK)

    # def list_users(self, request):
    #     pass



application = endpoints.api_server([BackendAPI])
