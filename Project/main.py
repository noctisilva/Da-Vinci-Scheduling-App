#The main routing module
import webapp2
import json
from google.appengine.ext import ndb
from datetime import datetime

from models import *
from controllers import *

class MainHandler(webapp2.RequestHandler):
    def get(self):

        testNotification = Notification(message="DOS!", parent=schedule_key())
        tn_key           = testNotification.put()


        for i in ["one", "two", "three", "four"]:
            s = Schedule()
            s.name = i
            s.instructor = "Mr." + i
            s_key = s.put()
            for j in ["one", "two", "three", "four"]:
                n = Notification(parent=s_key)
                n.message = "message" + j
                print n.put()

        notifications_query = Notification.query(ancestor=schedule_key()).order(-Notification.timestamp)
        notifications       = notifications_query.fetch()
        output = ""
        for notification in notifications:
            output += str(notification.key.id()) + " - " + json.dumps(notification.to_dict(), cls=DateTimeEncoder) + "<br>"

        self.response.out.write(output)


app = webapp2.WSGIApplication([
    ('/', MainHandler),

    # Locations (For Exhibits)
    webapp2.Route(
        '/locations',
        handler=LocationListHandler,
        name='location-list'
    ),
    webapp2.Route(
        '/locations/<location_id>',
        handler=LocationHandler,
        name='location'
    ),

    # Exhibits (CMS)
    webapp2.Route(
        '/exhibits',
        handler=ExhibitListHandler,
        name='exhibit-list'
    ),
    webapp2.Route(
        '/exhibits/<exhibit_id>',
        handler=ExhibitHandler,
        name='exhibit'
    ),

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
    )#,
#
#    # Schedules Event Calendars
#    webapp2.Route(
#        '/schedules/<schedule_id>/events',
#        handler = EventListHandler,
#        name    = 'event-list'
#    ),
#    webapp2.Route(
#        '/schedules/<schedule_id>/events/<event_id>',
#        handler = EventHandler,
#        name    = 'event'
#    ),
#
#    # Survey Questions
#    webapp2.Route(
#        '/survey_questions',
#        handler = SurveyQuestionListHandler,
#        name    = 'survey-question-list'
#    ),
#    webapp2.Route(
#        '/survey_questions/<survey_question_id>',
#        handler = SurveyQuestionHandler,
#        name    = 'survey-question-list'
#    ),
#
#    # Surveys
#    webapp2.Route(
#        '/schedules/<schedule_id>/surveys',
#        handler = SurveyListHandler,
#        name    = 'survey-list'
#    ),
#    webapp2.Route(
#        '/schedules/<schedule_id>/surveys/<survey_id>',
#        handler = SurveyHandler,
#        name    = 'survey'
#    ),
#
#    # Survey Question Responses
#    webapp2.Route(
#        '/schedules/<schedule_id>/surveys/<survey_id>/survey_responses',
#        handler = SurveyResponseListHandler,
#        name    = 'survey-response-list'
#    ),
#    webapp2.Route(
#        '/schedules/<schedule_id>/surveys/<survey_id>/surveys/survey_responses/<survey_response_id>',
#        handler = SurveyResponseHandler,
#        name    = 'survey-response-list'
#    )
], debug=True)
