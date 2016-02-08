Python Django Skeleton for Google App Engine
============================================

A todo-list application using Python's NDB datastore API that can be deployed on Google App Engine.  
Link to: [The Python NDB Datastore API](https://cloud.google.com/appengine/docs/python/ndb/). This code can also be used as a skeleton for building Python applications on Google App Engine using NDB Datastore.

Sample Applications by Google
-----------------------------
This project is based on the skeleton from this [Github repo](https://github.com/GoogleCloudPlatform/appengine-django-skeleton).
See [Google Cloud Platform github repos](https://github.com/GoogleCloudPlatform) for sample applications and scaffolding for other python frameworks and use cases.

Run Locally
-----------
- requirements-vendor.txt includes dependencies that should be 'vendored', which means its completely included in the directory at time of deployment. This can only be done for pure Python libraries that don't require system libraries. In this case, a recent version of Django is vendored. These vendored libaries can be added to the project using the `pip -t` flag, which installs it directly into the folder specified, in this case the `lib` folder. In order to make this project deployable directly after clone, the vendored libraries were already checked into this repo, but new ones can be added and then installed using the `pip -t flag`.
```sh
# Vendor Django directly into the project `lib` folder
$ pip install -r requirements-vendor.txt -t lib
```
- Run this project locally from the command line:
```sh
$ dev_appserver.py app.yaml
```
You can also run the server using Django's server, assuming you install the dependencies:
```sh
$ python manage.py runserver
```
- Visit the application [http://localhost:8080](http://localhost:8080)

NOTE: See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver) for options when running dev_appserver.

Deploy
------
To deploy the application:

- Use the [Google Developer's Console](https://console.developer.google.com) to create a project, and note the project ID created. The project ID is sometimes the project name provided, and sometimes an auto-generated name.
- Collect the static files into the static/ directory
```sh
$ python manage.py collectstatic
```
- [Deploy the application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with
```sh
$ appcfg.py -A <your-project-id> update app.yaml
```
- Your application is now live at https://your-app-id.appspot.com
