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
import request_messages
from google.appengine.datastore.datastore_query import Cursor
# from geo import geomodel, geotypes
from google.appengine.ext import ndb

API_EXPLORER = '292824132082.apps.googleusercontent.com'
CLIENT_IDS = ['651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com',
              API_EXPLORER]

__author__ = 'Sebastian Boyd, Duncan Grubbs'
__copyright__ = 'Copyright (C) 2016 SB Technology Holdings International'

@endpoints.api(name='backend', version='v1')
class BackendAPI(remote.Service):
    '''backend api'''
    @endpoints.method(request_messages.User,
                      request_messages.StatusMessage,
                      name='insert_user',
                      path='insert_user',
                      http_method='POST')
    def insert_user(self, request):
        ''' add user '''
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException('Invalid token.')

        # check user existance
        user = models.User.query(models.User.account == current_user).get()

        if user:
            # EXISTS
            if request.name:
                user.name = request.name
            if request.age:
                user.age = request.age
            if request.sex:
                user.sex = int(request.sex)
        else:
            # User not registered, add user
            user = models.User(account=current_user, name=request.name, age=request.age,
                               sex=int(request.sex))
        user.put()
        return request_messages.StatusMessage(status=request_messages.Status.OK)

    @endpoints.method(request_messages.Activity,
                      request_messages.StatusMessage,
                      name='add_activity',
                      path='activites/add',
                      http_method='POST')
    def add_activity(self, request):
        ''' add activity '''
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException('Invalid token.')

        user = models.User.query(models.User.account == current_user).get()
        try:
            user_key = user.key
        except AttributeError:
            # User does not exist
            return request_messages.StatusMessage(status=request_messages.Status.BAD_DATA)

        activity = models.Activity(activity_id=request.activity_id, parent=user_key)
        if request.user_created_description:
            activity.user_created_description = request.user_created_description

        activity.put()

        return request_messages.StatusMessage(status=request_messages.Status.OK)

    @endpoints.method(request_messages.ActivityRequest,
                      request_messages.ActivityList,
                      name='get_activities',
                      path='activites/list',
                      http_method='POST')
    def get_activities(self, request):
        ''' get activites '''
        activity_message_list = []
        if request.cursor:
            cursor = Cursor(urlsafe=request.cursor)
        else:
            cursor = Cursor()

        activities, new_cursor, more = models.Activity.query().fetch_page(10, start_cursor=cursor)

        print activities
        for a in activities:
            user = a.key.parent().get()
            msg_user = request_messages.User(name=user.name, age=user.age)
            activity = request_messages.ActivityResponse(activity_id=a.activity_id, user=msg_user, distance=9.5)
            if a.user_created_description:
                activity.description = a.user_created_description
            activity_message_list.append(activity)

        if new_cursor and more:
            print new_cursor.urlsafe()
            return request_messages.ActivityList(activites=activity_message_list,
                                                 cursor=new_cursor.urlsafe())

        return request_messages.ActivityList(activites=activity_message_list)


application = endpoints.api_server([BackendAPI])
