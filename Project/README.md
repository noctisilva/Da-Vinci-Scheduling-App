Hokay.  So.

The key to understanding Google App Engine's NDB Datastore is that data is represented as a heirarhy or a tree.  As such, a particular entity is referenced by the chain of its parents from a root entity down.

For Example, the key to a particular notification would be:
`('Schedule', s_id, 'NotificationList', 1, 'Notification', n_id)`

https://cloud.google.com/appengine/docs/python/ndb/
https://cloud.google.com/appengine/docs/python/gettingstartedpython27/usingdatastore
https://cloud.google.com/appengine/docs/python/gettingstartedpython27/handlingforms
https://cloud.google.com/appengine/docs/python/ndb/modelclass#introspection
https://webapp-improved.appspot.com/guide/routing.html


```
Schedule
    Notifications
        Notification
            > message
            > timestamp
        ...
    ...
    Events
        Event
            > exhibit
            > start_time
            > end_time
        ...
    ...
    Surveys
        Survey
            >
    ...
...

Exhibits
    > name
    > title
...



```

### All data for the administrative overview panel
`/api/schedules`

### All data for the administrative and user view of a single schedule
`/api/schedules/{schedule_id}`

### List all notifications sent to a particular schedule
`/api/schedules/{schedule_id}/notifications`

### Access a singular notification
`/api/schedules/{schedule_id}/notifications/{notification_id}`

### List all events in a schedule
`/api/schedules/{schedule_id}/events`

### List information about a specific event
`/api/schedules/{schedule_id}/events/{event_id}`




GET
PUT
POST
DELETE