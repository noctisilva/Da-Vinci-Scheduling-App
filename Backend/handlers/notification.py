import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
from models import *
from utilities import *

class NotificationListHandler(webapp2.RequestHandler):
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
        models = Notification.query(Notification.schedule == s).order(-Notification.timestamp).fetch()
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
        model = Notification()
        s     = RestHelper().key_from_id_string("Schedule", schedule_id)
        if (s == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        attributes = dict(
            message     = self.request.get('message', default_value='').strip(),
            schedule    = s
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(model, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

class NotificationHandler(webapp2.RequestHandler):
    def get(self, schedule_id="-1", notification_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Notification", notification_id)
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

    def post(self, schedule_id="-1", notification_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE (MORE BELOW)
        entity_key = RestHelper().key_from_id_string("Notification", notification_id)
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
            message  = self.request.get('message', default_value=entity.message).strip(),
            schedule = entity.schedule
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(entity, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

    def delete(self, schedule_id="-1", notification_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Notification", notification_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.delete()

        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return
