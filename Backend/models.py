from google.appengine.ext import ndb

class Schedule(ndb.Model):
    """
        GET    /schedules
        PUT    /schedules
         - name
         - instructor
        POST   /schedules/<schedule_id>
         - name
         - instructor
        DELETE /schedules/<schedule_id>
    """
    name       = ndb.StringProperty()
    instructor = ndb.StringProperty()

class Location(ndb.Model):
    """
        GET    /locations
        PUT    /locations
         - name
         - picture
         - description
        POST   /locations/<location_id>
         - name
         - picture
         - description
        DELETE /locations/<location_id>
    """
    name        = ndb.StringProperty()
    picture     = ndb.StringProperty()
    description = ndb.StringProperty()

class SurveyQuestion(ndb.Model):
    """
        GET    /survey_questions
        PUT    /survey_questions
         - question
         - active
        POST   /survey_questions/<survey_question_id>
         - question
         - active
        DELETE /survey_questions/<survey_question_id>
    """
    question = ndb.StringProperty()
    active   = ndb.BooleanProperty()

class SurveyResponse(ndb.Model):
    """
        GET    /schedules/<schedule_id>/survey_responses
        PUT    /schedules/<schedule_id>/survey_responses
         - question
         - answer
        POST   /schedules/<schedule_id>/survey_responses/<survey_response_id>
         - question
         - answer
        DELETE /schedules/<schedule_id>/survey_responses/<survey_response_id>
    """
    question = ndb.StringProperty()
    answer   = ndb.StringProperty()
    schedule = ndb.KeyProperty(kind=Schedule)

class Notification(ndb.Model):
    """
        GET    /schedules/<schedule_id>/notifications
        PUT    /schedules/<schedule_id>/notifications
         - message
        POST   /schedules/<schedule_id>/notifications/<notification_id>
         - message
        DELETE /schedules/<schedule_id>/notifications/<notification_id>
    """
    message   = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now=True)
    schedule  = ndb.KeyProperty(kind=Schedule)

class Exhibit(ndb.Model):
    """
        GET    /exhibits
        PUT    /exhibits
         - name
         - picture
         - description
         - location (id)
        POST   /exhibits/<exhibit_id>
         - name
         - picture
         - description
         - location (id)
        DELETE /exhibits/<exhibit_id>
    """
    name        = ndb.StringProperty()
    picture     = ndb.StringProperty()
    description = ndb.StringProperty()
    location    = ndb.KeyProperty(kind=Location)

class Event(ndb.Model):
    """
        GET    /schedules/<schedule_id>/events
        PUT    /schedules/<schedule_id>/events
         - start_time
         - end_time
         - exhibit (id)
        POST   /schedules/<schedule_id>/events/<event_id>
         - start_time
         - end_time
         - exhibit (id)
        DELETE /schedules/<schedule_id>/events/<event_id>
    """
    start_time = ndb.DateTimeProperty()
    end_time   = ndb.DateTimeProperty()
    schedule   = ndb.KeyProperty(kind=Schedule)
    exhibit    = ndb.KeyProperty(kind=Exhibit)
