#The main routing module
import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime

from models                import *
from handlers.location     import *
from handlers.schedule     import *
from handlers.notification import *
from handlers.exhibit      import *
from handlers.event        import *

class MainHandler(webapp2.RequestHandler):
    def get(self):

        for i in ["one", "two", "three", "four"]:
            l             = Location()
            l.name        = "l.name-" + i
            l.picture     = "l.picture-" + i
            l.description = "l.description-" + i
            l_key         = l.put();

            s             = Schedule()
            s.name        = i
            s.instructor  = "Mr." + i
            s.location    = l_key;
            s_key         = s.put()

        output = "DONE"
        self.response.out.write(output)


app = webapp2.WSGIApplication([
    ('/', MainHandler),

    # Schedules (High Level)
    webapp2.Route(
        '/schedules',
        handler = ScheduleListHandler,
        name    = 'schedule-list'
    ),
    webapp2.Route(
        '/schedules/<schedule_id>',
        handler = ScheduleHandler,
        name    = 'schedule'
    ),

    # Locations
    webapp2.Route(
        '/locations',
        handler = LocationListHandler,
        name    = 'location-list'
    ),
    webapp2.Route(
        '/locations/<location_id>',
        handler = LocationHandler,
        name    = 'location'
    ),

    # Notifications
    webapp2.Route(
        '/schedules/<schedule_id>/notifications',
        handler = NotificationListHandler,
        name    = 'notification-list'
    ),
    webapp2.Route(
        '/schedules/<schedule_id>/notifications/<notification_id>',
        handler = NotificationHandler,
        name    = 'notification'
    ),

    # Exhibits
    webapp2.Route(
        '/exhibits',
        handler = ExhibitListHandler,
        name    = 'exhibit-list'
    ),
    webapp2.Route(
        '/exhibits/<exhibit_id>',
        handler = ExhibitHandler,
        name    = 'exhibit'
    ),

    # Events
    webapp2.Route(
        '/schedules/<schedule_id>/events',
        handler = EventListHandler,
        name    = 'event-list'
    ),
    webapp2.Route(
        '/schedules/<schedule_id>/events/<event_id>',
        handler = EventHandler,
        name    = 'event'
    ),

], debug=True)
