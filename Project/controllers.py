import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
from models import *

DEFAULT_SCHEDULE_ID = "default_schedule"

def schedule_key(schedule_id=DEFAULT_SCHEDULE_ID):
    """"""
    return ndb.Key("Schedule", schedule_id)

def jsonifyEntity(entity):
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

######################
# BEGIN PoC Handlers #
######################

class LocationListHandler(webapp2.RequestHandler):
    def get(self):
        entities = Location.query().fetch()

        s = []
        for entity in entities:
            s.append(jsonifyEntity(entity))
        output = "[" + ",".join(s) + "]"

        self.response.out.write(output)

    def put(self):
        entity             = Location()
        entity.name        = self.request.get('name', default_value='').strip()
        entity.picture     = self.request.get('picture', default_value='').strip()
        entity.description = self.request.get('description', default_value='').strip()
        entity.put()

class LocationHandler(webapp2.RequestHandler):
    def get(self, location_id="-1"):
        entity = ndb.Key("Location", long(location_id)).get()
        output = jsonifyEntity(entity)
        self.response.out.write(output)

    def post(self, location_id="-1"):
        entity             = ndb.Key("Location", long(location_id)).get()
        entity.name        = self.request.get('name', default_value=entity.name).strip()
        entity.picture     = self.request.get('picture', default_value=entity.name).strip()
        entity.description = self.request.get('description', default_value=entity.name).strip()
        entity.put()

    def delete(self, location_id="-1"):
        entity = ndb.Key("Location", long(location_id)).get()
        entity.key.delete()




class ExhibitListHandler(webapp2.RequestHandler):
    def get(self):
        entities = Exhibit.query().fetch()

        s = []
        for entity in entities:
            s.append(jsonifyEntity(entity))
        output = "[" + ",".join(s) + "]"

        self.response.out.write(output)

    def put(self):
        entity             = Exhibit()
        entity.name        = self.request.get('name', default_value='').strip()
        entity.picture     = self.request.get('picture', default_value='').strip()
        entity.description = self.request.get('description', default_value='').strip()
        entity.put()

class ExhibitHandler(webapp2.RequestHandler):
    def get(self, exhibit_id="-1"):
        entity = ndb.Key("Exhibit", long(exhibit_id)).get()
        output = jsonifyEntity(entity)
        self.response.out.write(output)

    def post(self, exhibit_id="-1"):
        entity             = ndb.Key("Exhibit", long(exhibit_id)).get()
        entity.name        = self.request.get('name', default_value=entity.name).strip()
        entity.picture     = self.request.get('picture', default_value=entity.name).strip()
        entity.description = self.request.get('description', default_value=entity.name).strip()
        entity.put()

    def delete(self, exhibit_id="-1"):
        entity = ndb.Key("Exhibit", long(exhibit_id)).get()
        entity.key.delete()



class NotificationListHandler(webapp2.RequestHandler):
    def get(self, schedule_id="-1"):
        entities = Notification.query(ancestor=schedule_key(long(schedule_id))).order(-Notification.timestamp).fetch()

        s = []
        for entity in entities:
            s.append(jsonifyEntity(entity))
        output = "[" + ",".join(s) + "]"

        self.response.out.write(output)

    def put(self, schedule_id="-1"):
        parent         = schedule_key(long(schedule_id))
        entity         = Notification(parent=parent)
        entity.message = self.request.get('message', default_value='').strip()
        entity.put()

class NotificationHandler(webapp2.RequestHandler):
    def get(self, schedule_key="-1", notification_id="-1"):
        entity = ndb.Key("Schedule", schedule_key(long(schedule_id)), "Notification", long(notification_id)).get()
        output = jsonifyEntity(entity)
        self.response.out.write(output)

    def post(self, schedule_key="-1", notification_id="-1"):
        entity         = ndb.Key("Notification", long(notification_id)).get()
        entity.message = self.request.get('message', default_value=entity.message).strip()
        entity.put()

    def delete(self, schedule_key="-1",notification_id="-1"):
        entity = ndb.Key("Notification", long(notification_id)).get()
        entity.key.delete()