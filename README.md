## ToEat

A todo app for food.

## Run Locally
1. Install the [App Engine Python SDK](https://cloud.google.com/appengine/downloads).
See the README file for directions. You'll need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed too.

2. Clone this repo with

```
   git clone git@github.com:shshank/toeat.git
```
3. Install dependencies in the project's lib directory.
   Note: App Engine can only import libraries from inside your project directory.

```
   pip install -r requirements.txt -t lib
```
4. Run this project locally using Google App Launcher or from the command line (symlinks can be created from the launcher):

```
   dev_appserver.py . --skip_sdk_update_check=yes
```

Visit the application at: <http://localhost:8080>

See [the development server documentation](https://cloud.google.com/appengine/docs/python/tools/devserver) for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Admin Console](https://appengine.google.com) to create a project/app id. (App id and project id are identical)
1. [Deploy the application](https://cloud.google.com/appengine/docs/python/tools/uploadinganapp):

```
   appcfg.py -A <your-project-id> --oauth2 update .
```

### Relational Databases and Datastore
To add persistence to your models, use [NDB](https://cloud.google.com/appengine/docs/python/ndb/) for scale.  Consider [CloudSQL](https://cloud.google.com/appengine/docs/python/cloud-sql/) if you need a relational database.

### Installing Libraries
See the [Third party libraries](https://cloud.google.com/appengine/docs/python/tools/libraries27) page for libraries that are already included in the SDK.  To include SDK libraries, add them in your app.yaml file. Other than libraries included in the SDK, only pure python libraries may be added to an App Engine project.