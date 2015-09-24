from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext, loader

from .models import Task

def index(request):
    if request.method == 'POST':
        # Get the  dictionary-like object containing all given HTTP POST parameters
        queryDictionary = request.POST
        if(queryDictionary.get("task") == "" or queryDictionary.get("task") == None):
            # Empty query dictionary
            pageContent = '<h1>HTTP 404. Page not found.</h1><a href="/todoList/">Home</a>'
            return HttpResponseNotFound(pageContent)
        else:
            taskObject = Task(taskText=queryDictionary.get("task"))
            taskObject.save()

    latestTaskList = Task.objects.all()

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

def deleteTask(request, task_id):
    taskObject = Task.objects.get(id=task_id)
    taskObject.delete()

    latestTaskList = Task.objects.all()
    template = loader.get_template('todoList/index.html')
    context = RequestContext(request)
    context.push({ 'latestTaskList': latestTaskList, })
    return HttpResponse(template.render(context))

def deleteAllTasks(request):
    taskObject = Task.objects.all()
    taskObject.delete()

    latestTaskList = Task.objects.all()
    template = loader.get_template('todoList/index.html')
    context = RequestContext(request)
    context.push({ 'latestTaskList': latestTaskList, })
    return HttpResponse(template.render(context))

def aboutMe(request):
    template = loader.get_template('todoList/about.html')
    context = RequestContext(request)
    context.push({})
    return HttpResponse(template.render(context))

#NOTES:
# To delete the task list from the database using command line
#$ python manage.py shell
#>>> from todoList.models import Task
#>>> Task.objects.all().delete()
