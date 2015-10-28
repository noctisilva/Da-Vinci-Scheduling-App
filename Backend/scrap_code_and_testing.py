"""

Schedules:
    name
    instructor

Notification:
    message
    timestamp
    schedule

-------------------------------------------------------------------------------

GET /schedules/<schedule_id>/notifications
 =>
s = ndb.Key("Schedule", schedule_id)
Notification.query(schedule == s).order(-Notification.timestamp).fetch()

-------------------------------------------------------------------------------

PUT /schedules/<schedule_id>/notifications
 =>
n = Notification()
n.message   = args[name]
n.timestamp = args[timestamp]
n.schedule  = ndb.Key("Schedule", schedule_id)
n.put()

-------------------------------------------------------------------------------

GET /schedules/<schedule_id>/notifications/<notification_id>
 =>
ndb.Key("Notification", notification_id).get()

-------------------------------------------------------------------------------

"""

################################################################################
################################################################################
################################################################################
################################################################################

import os
import pprint

from google.appengine.api import memcache
from google.appengine.api import mail
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
from models import *

class Notification(ndb.Model):
    message   = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now=True)
    schedule  = ndb.KeyProperty(kind=Schedule)

s = Schedule()
s.name = "NAME"
s.instructor = "INSRTUCTOR"
sk = s.put()

n = Notification()
n.message = "FIRST MESSAGE"
n.schedule = sk
nk = n.put()

n = Notification()
n.message = "SECOND MESSAGE"
n.schedule = sk
nk = n.put()

n = Notification()
n.message = "THIRD MESSAGE"
n.schedule = sk
nk = n.put()


sk = ndb.Key("Schedule", 4855443348258816)
print sk
print "-------"
print Notification.query(Notification.schedule == sk).order(-Notification.timestamp).fetch()
print "-------"
print ndb.Key("Notification", 5981343255101440).get()
print "-------"
print s, n
print "-------"
print ndb.Key("Notification", 5981343255101440).get().to_dict()

################################################################################
################################################################################
################################################################################
################################################################################

import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
from models import *

DEFAULT_SCHEDULE_ID = "default_schedule"

def schedule_key(schedule_id=DEFAULT_SCHEDULE_ID):
    """"""
    return ndb.Key("Schedule", schedule_id)

def jsonify_entity(entity):
    """Converts an entity to JSON.  Needs work for special cases."""
    entity_dict = entity.to_dict()
    entity_dict['id'] = str(entity.key.id())
    return json.dumps(entity_dict, cls=DateTimeEncoder)

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()

        return json.JSONEncoder.default(self, o)


######################
# END Bootstrapping, #
# BEGIN Handlers     #
######################

class RestHelper(object):
    def list(self, model):
        entities = model.query().fetch()

        s = []
        for entity in entities:
            s.append(jsonify_entity(entity))
        output = "[" + ",".join(s) + "]"

        return output

    def put(self, model, attributes):
        for key, value in attributes.items():
            setattr(model, key, value)
        model.put()


class ScheduleListHandler(webapp2.RequestHandler):
    def get(self):
        model  = Schedule()
        output = RestHelper().list(model)
        self.response.out.write(output)

    def put(self):
        model      = Schedule()
        attributes = dict(
            name       = self.request.get('name', default_value='').strip(),
            instructor = self.request.get('instructor', default_value='').strip()
        )
        RestHelper().put(model, attributes)


class ScheduleHandler(webapp2.RequestHandler):
    def get(self, **kvargs):
        try:
            entity = ndb.Key("Schedule", long(schedule_id)).get()
        except:
            print "ERROR"
            return
        print entity
        pass
        RestHelper().get(("Schedule"), self.request, self.response)

    def post(self, schedule_id="-1"):
        pass

    def delete(self, schedule_id="-1"):
        pass

################################################################################
################################################################################
################################################################################
################################################################################

class RestHelper(object):
    def get(self, key):
        entity = None

        try:
            entity = ndb.Key(*key).get()
        except:
            entity = None

        return entity

def get(self, request_handler, key, args):
    if !self.authenticated(self):
        self.send(self, 503)
        return

    if !self.keys_valid(schedule_id):
        self.send(self, 400)
        return

    key    = ("Schedule", long(schedule_id))
    entity = RestHelper().get(key)

    if key == None:
        RestHelper().send(self, 404)
        return




def get(self, schedule_id= "-1"):
    args = dict(
        schedule_id = schedule_id
    )
    key  = ("Schedule", "schedule_id")
    RestHelper().get(self, key, args)

################################################################################
################################################################################
################################################################################
################################################################################


class ScheduleListHandler(webapp2.RequestHandler):
    def get(self):
        entities = Schedule.query().fetch()

        s = []
        for entity in entities:
            s.append(jsonifyEntity(entity))
        output = "[" + ",".join(s) + "]"

        self.response.out.write(output)

    def put(self):
        entity = Schedule()
        entity.name       = self.request.get('name', default_value='').strip()
        entity.instructor = self.request.get('instructor', default_value='').strip()
        entity.put()

class ScheduleHandler(webapp2.RequestHandler):
    def get(self, schedule_id="-1"):
        entity = ndb.Key("Schedule", long(schedule_id)).get()
        output = jsonifyEntity(entity)
        self.response.out.write(output)

    def post(self, schedule_id="-1"):
        entity = ndb.Key("Schedule", long(schedule_id)).get()

        entity.name       = self.request.get('name', default_value=entity.name).strip()
        entity.instructor = self.request.get('instructor', default_value=entity.instructor).strip()

        entity.put()

    def delete(self, schedule_id="-1"):
        entity = ndb.Key("Schedule", long(schedule_id)).get()
        entity.key.delete()
