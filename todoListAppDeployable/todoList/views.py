from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template import RequestContext, loader
from google.appengine.ext import ndb

from .models import Task


def index(request):
    """ Displays all the options and main page."""

    if request.method == 'POST':
        # Get the  dictionary-like object containing all given HTTP POST parameters
        queryDictionary = request.POST
        if(queryDictionary.get("task") == "" or queryDictionary.get("task") == None):
            # Empty query dictionary
            pageContent = '<h1>HTTP 404. Page not found.</h1><a href="/todoList/">Home</a>'
            return HttpResponseNotFound(pageContent)
        else:
            taskObject = Task(taskText=queryDictionary.get("task"))
            taskObject.put()

    latestTaskList = Task.query()

    # Create a Template object by loading it.
    # get_template(...) loads a template with the given name, compiles it and returns a Template object.
    template = loader.get_template('todoList/index.html')

    # Fill the RequestContext. You render the template with a Context.
    # We can simply use this -> context = RequestContext(request, { 'latestTaskList': latestTaskList, })
    # but using the below 2 statements, we make the context data to take priority over context processors.
    # https://docs.djangoproject.com/en/1.8/ref/templates/api/#django.template.RequestContext
    context = RequestContext(request)
    context.push({ 'latestTaskList': latestTaskList, })

    # We can also use a shortcut:
    # return render(request, 'todoList/index.html', context)
    # Call the Template object's render() method with a Context to "fill" the template.
    # Example:
    # >>> from django.template import Context, Template
    # >>> template = Template("My name is {{ my_name }}.")
    #
    # >>> context = Context({"my_name": "Adrian"})
    # >>> template.render(context)
    # "My name is Adrian."
    return HttpResponse(template.render(context))


def deleteTask(request, key_kind, key_id):
    """ Deletes a singe task entry."""

    task_key = ndb.Key(key_kind, int(key_id))
    task_key.delete()

    latestTaskList = Task.query()
    template = loader.get_template('todoList/index.html')
    context = RequestContext(request)
    context.push({ 'latestTaskList': latestTaskList, })
    return HttpResponse(template.render(context))


def deleteAllTasks(request):
    """ Deletes all the tasks."""

    ndb.delete_multi(Task.query().fetch(keys_only=True))

    latestTaskList = Task.query()
    template = loader.get_template('todoList/index.html')
    context = RequestContext(request)
    context.push({ 'latestTaskList': latestTaskList, })
    return HttpResponse(template.render(context))


def aboutMe(request):
    """ Shows the about me page."""

    template = loader.get_template('todoList/about.html')
    context = RequestContext(request)
    context.push({})
    return HttpResponse(template.render(context))
