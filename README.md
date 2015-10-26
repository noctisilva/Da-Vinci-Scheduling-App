# Da Vinci Scheduling App
---


## Assorted Sites and Resources I Found or Used
---

NDB Docs:
`https://cloud.google.com/appengine/docs/python/ndb/`

WebApp2 Docs:
`https://cloud.google.com/appengine/docs/python/tools/webapp/`

Some Notes about Cloud Datastore:
`http://googlecloudplatform.blogspot.com/2015/08/Introduction-to-data-models-in-Cloud-Datastore.html`

Info about builtin Types:
`https://docs.python.org/2/library/stdtypes.html`

Variable Numbers and Types of Arguments:
`http://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function`

Programmatically setting Attributes:
`http://stackoverflow.com/questions/285061/how-do-you-programmatically-set-an-attribute-in-python`

## General Code Notes
---

### Authenticate to use the SDK
```
gcloud auth login;
```

### Run a dev server, executed from project directory
`~/google-cloud-sdk/platform/google_appengine/dev_appserver.py --php_executable_path="/usr/bin/php-cgi" --host="0.0.0.0" --port="8080" --admin_host="0.0.0.0" --admin_port="8000" --clear_datastore=yes .`

