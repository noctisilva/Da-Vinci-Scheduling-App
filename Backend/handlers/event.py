import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
from models import *
from utilities import *

from dateutil.parser import *

class EventListHandler(webapp2.RequestHandler):
    def get(self, schedule_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        s = RestHelper().key_from_id_string("Schedule", schedule_id)
        if (s.get() == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        models = Event.query(Event.schedule == s).fetch()
        # END UNIQUE PER RESOURCE

        output = RestHelper().to_json(models)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        self.response.out.write(output)

    def put(self, schedule_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        model      = Event()
        s          = RestHelper().key_from_id_string("Schedule", schedule_id)
        exhibit_id = self.request.get('exhibit', default_value='-1')
        e          = RestHelper().key_from_id_string("Exhibit", exhibit_id)
        if (s == None or e == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        if (s.get() == None or e.get() == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        attributes = dict(
            start_time  = parse(self.request.get('start_time', default_value='')),
            end_time    = parse(self.request.get('end_time', default_value='')),
            schedule    = s,
            exhibit     = e
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(model, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

class EventHandler(webapp2.RequestHandler):
    def get(self, schedule_id="-1", event_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Event", event_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.get()

        if (entity == None):
            self.response.set_status(404)
            return

        output = RestHelper().to_json(entity)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        self.response.write(output)
        return

    def post(self, schedule_id="-1", event_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE (MORE BELOW)
        entity_key = RestHelper().key_from_id_string("Event", event_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.get()

        if (entity == None):
            self.response.set_status(404)
            return

        # START UNIQUE PER RESOURCE
        s     = RestHelper().key_from_id_string("Schedule", schedule_id)
        e     = RestHelper().key_from_id_string("Exhibit", exhibit_id)
        if (s == None or e == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        if (s.get() == None):
            s = entity.schedule
        if (e.get() == None):
            e = entity.exhibit
        attributes = dict(
            start_time  = parse(self.request.get('start_time', default_value=entity.start_time)),
            end_time    = parse(self.request.get('end_time', default_value=entity.end_time)),
            schedule    = s,
            exhibit     = e
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(entity, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

    def delete(self, schedule_id="-1", event_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Event", event_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.delete()

        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return
