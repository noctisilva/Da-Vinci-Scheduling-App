from google.appengine.ext import ndb

# ('Schedule', id, 'NotificationList', 1, 'Notification', id)

class Schedule(ndb.Model):
    """"""
    name       = ndb.StringProperty()
    instructor = ndb.StringProperty()

class Notification(ndb.Model):
    """"""
    message   = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now=True)

class Location(ndb.Model):
    """"""
    name        = ndb.StringProperty()
    picture     = ndb.StringProperty()
    description = ndb.StringProperty()

class Exhibit(ndb.Model):
    """"""
    name        = ndb.StringProperty()
    picture     = ndb.StringProperty()
    description = ndb.StringProperty()
#    location    = ndb.StructuredProperty(Location)

class Event(ndb.Model):
    """"""
    start_time = ndb.DateTimeProperty()
    end_time   = ndb.DateTimeProperty()
    exhibit    = ndb.StructuredProperty(Exhibit)

class SurveyQuestion(ndb.Model):
    """"""
    question     = ndb.StringProperty()
    answer       = ndb.StringProperty()
    type         = ndb.IntegerProperty()
    options      = ndb.JsonProperty()

class SurveyResponse(ndb.Model):
    """"""
    question     = ndb.StringProperty()
    answer       = ndb.StringProperty()

class Survey(ndb.Model):
    """"""
    questions = ndb.StructuredProperty(SurveyQuestion, repeated=True)
    responses = ndb.StructuredProperty(SurveyResponse, repeated=True)


