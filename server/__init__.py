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
from math import cos, asin, sqrt

API_EXPLORER = '292824132082.apps.googleusercontent.com'
CLIENT_IDS = ['750712428354-d569r948i29du5to3rklkgemsv2sgtvo.apps.googleusercontent.com',
              API_EXPLORER]

__author__ = 'Sebastian Boyd, Duncan Grubbs'
__copyright__ = 'Copyright (C) 2016 SB Technology Holdings International'

def earth_distance(lat1, lon1, lat2, lon2):
    '''Finds Distace between two points on earth'''
    p = 0.017453292519943295
    a = cos((lat2 - lat1) * p) / 2
    b = cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    c = 0.5 - a + b
    return 12742 * asin(sqrt(c))

@endpoints.api(name='backend', version='v1')
class BackendAPI(remote.Service):
    '''backend api'''
    @endpoints.method(request_messages.User,
                      request_messages.StatusMessage,
                      name='insert_user',
                      path='insert_user',
                      http_method='POST',
                      allowed_client_ids=CLIENT_IDS)
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
                      http_method='POST',
                      allowed_client_ids=CLIENT_IDS)
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

        activity = models.Activity(activity_id=request.activity_id, lat=request.lat, lng=request.lng, parent=user_key)
        if request.user_created_description:
            activity.user_created_description = request.user_created_description

        activity.put()

        return request_messages.StatusMessage(status=request_messages.Status.OK)

    @endpoints.method(request_messages.ActivityRequest,
                      request_messages.ActivityList,
                      name='get_activities',
                      path='activites/list',
                      http_method='POST',
                      allowed_client_ids=CLIENT_IDS)
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
            print a
            user = a.key.parent().get()
            msg_user = request_messages.User(name=user.name, age=user.age)
            #d = round(earth_distance(a.lat, a.lng, request.lat, request.lng),2)
            d = 44.0
            activity = request_messages.ActivityResponse(activity_id=a.activity_id, user=msg_user, distance=d)
            if a.user_created_description:
                activity.description = a.user_created_description
            if user.age <= request.max_age and user.age >= request.min_age:
                activity_message_list.append(activity)

        if new_cursor and more:
            print new_cursor.urlsafe()
            return request_messages.ActivityList(activites=activity_message_list,
                                                 cursor=new_cursor.urlsafe())

        return request_messages.ActivityList(activites=activity_message_list)


application = endpoints.api_server([BackendAPI])
