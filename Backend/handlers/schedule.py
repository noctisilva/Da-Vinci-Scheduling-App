import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
from models import *
from utilities import *

class ScheduleListHandler(webapp2.RequestHandler):
    def get(self):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        models = Schedule().query().fetch()
        # END UNIQUE PER RESOURCE

        output = RestHelper().to_json(models)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        self.response.out.write(output)

    def put(self):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        model      = Schedule()
        attributes = dict(
            name       = self.request.get('name', default_value='').strip(),
            instructor = self.request.get('instructor', default_value='').strip()
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(model, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

class ScheduleHandler(webapp2.RequestHandler):
    def get(self, schedule_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Schedule", schedule_id)
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

    def post(self, schedule_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE (MORE BELOW)
        entity_key = RestHelper().key_from_id_string("Schedule", schedule_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.get()

        if (entity == None):
            self.response.set_status(404)
            return

        # START UNIQUE PER RESOURCE
        attributes = dict(
            name       = self.request.get('name', default_value=entity.name).strip(),
            instructor = self.request.get('instructor', default_value=entity.instructor).strip()
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(entity, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

    def delete(self, schedule_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Schedule", schedule_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.delete()

        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return
