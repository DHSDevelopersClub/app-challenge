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
from geo import geomodel, geotypes
from google.appengine.ext import ndb

API_EXPLORER = '292824132082.apps.googleusercontent.com'
CLIENT_IDS = ['651504877594-9qh2hc91udrhht8gv1h69qarfa90hnt3.apps.googleusercontent.com',
              API_EXPLORER]

__author__ = 'Sebastian Boyd, Duncan Grubbs'
__copyright__ = 'Copyright (C) 2016 SB Technology Holdings International'

@endpoints.api(name='backend', version='v1')
class BackendAPI(remote.Service):
    '''backend api'''
    @endpoints.method(request_messages.EditUser,
                      request_messages.StatusMessage,
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
            if request.name:
                user.name = request.name
            if request.age:
                user.age = request.age
            if request.sex:
                user.sex = int(request.sex)
        else:
            # User not registered, add user
            user = models.User(account=current_user, name=request.name, age=request.age, sex=int(request.sex))
        user.put()

        return request_messages.StatusMessage(status=request_messages.Status.OK)

    @endpoints.method(request_messages.Activity,
                      request_messages.StatusMessage,
                      name='add_activity',
                      path='activites/add',
                      http_method='POST')
    def add_activity(self, request):
        current_user = endpoints.get_current_user()
        if current_user is None:
            raise endpoints.UnauthorizedException('Invalid token.')

        user = models.User.query(models.User.account == current_user).get()
        try:
            user_key = user.key
        except AttributeError:
            # User does not exist
            return StatusResponse(status=request_messages.Status.BAD_DATA)

        activity = models.Activity(activity_id=request.activity_id,
                                   location = ndb.GeoPt(1, 2),
                                   parent=user_key)
        if request.user_created_disrcription:
            activity.user_created_disrcription = request.user_created_disrcription

        activity.put()

        return request_messages.StatusMessage(status=request_messages.Status.OK)

    @endpoints.method(request_messages.Activity,
                      request_messages.ActivityList,
                      name='get_activities',
                      path='activites/list',
                      http_method='POST')
    def get_activities(self, request):

        # activity_message_list = []
        # center = geotypes.Point(1, 2)
        # distance = 5000 # in meters
        # ndb_activity_list = models.Activity.proximity_fetch(models.Activity.query(), center, max_results=20,
        #                                                     max_distance=distance)
        # print ndb_activity_list
        # for a in ndb_activity_list:
        #     activity = request_messages.Activity(activity_id=a.activity_id, lat=a.lat, lng=a.lng)
        #     if a.user_created_disrcription:
        #         activity.user_created_disrcription = a.user_created_disrcription
        #     activity_message_list.append(activity)
        # return request_messages.ActivityList(activites=activity_message_list)
        fake_activities = [
                    request_messages.Activity(
                        activity_id=0,
                        user_created_disrcription="have fun at Stinson Beach",
                        lat=0,
                        lng=0),
                    request_messages.Activity(
                        activity_id=666,
                        user_created_disrcription="sell my soul",
                        lat=0,
                        lng=0),
                    request_messages.Activity(
                        activity_id=404,
                        user_created_disrcription="can't find anything to do",
                        lat=0,
                        lng=0),
                   ]
        return request_messages.ActivityList(activites=fake_activities)


application = endpoints.api_server([BackendAPI])
