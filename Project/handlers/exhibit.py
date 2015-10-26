import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime
from models import *
from utilities import *

class ExhibitListHandler(webapp2.RequestHandler):
    def get(self):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        models = Exhibit().query().fetch()
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
        model       = Exhibit()
        location_id = self.request.get('location', default_value='-1')
        l           = RestHelper().key_from_id_string("Location", location_id)
        if (l == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        if (l.get() == None):
            self.response.set_status(404)
            self.response.headers.add_header("Content-type", "application/json")
            return
        attributes = dict(
            name        = self.request.get('name', default_value='').strip(),
            picture     = self.request.get('picture', default_value='').strip(),
            description = self.request.get('description', default_value='').strip(),
            location    = l
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(model, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

class ExhibitHandler(webapp2.RequestHandler):
    def get(self, exhibit_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Exhibit", exhibit_id)
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

    def post(self, exhibit_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE (MORE BELOW)
        entity_key = RestHelper().key_from_id_string("Exhibit", exhibit_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.get()

        if (entity == None):
            self.response.set_status(404)
            return

        # START UNIQUE PER RESOURCE
        location_id = self.request.get('location', default_value='-1')
        l           = RestHelper().key_from_id_string("Location", location_id)
        if (l.get() == None):
            l = entity.location
        attributes = dict(
            name        = self.request.get('name', default_value=entity.name).strip(),
            picture     = self.request.get('picture', default_value=entity.picture).strip(),
            description = self.request.get('description', default_value=entity.description).strip(),
            location    = l
        )
        # END UNIQUE PER RESOURCE

        RestHelper().put(entity, attributes)
        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return

    def delete(self, exhibit_id="-1"):
        # User must be authenticated
        if (RestHelper().authenticated(self) == False):
            self.response.set_status(503)
            return

        # START UNIQUE PER RESOURCE
        entity_key = RestHelper().key_from_id_string("Exhibit", exhibit_id)
        # END UNIQUE PER RESOURCE

        if (entity_key == None):
            self.response.set_status(400)
            return

        entity = entity_key.delete()

        self.response.set_status(200)
        self.response.headers.add_header("Content-type", "application/json")
        return
