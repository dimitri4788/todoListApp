from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addTask/$', views.index, name='index'),
    url(r'^deleteTask/(?P<task_id>[0-9]+)/$', views.deleteTask, name='deleteTask'),
    url(r'^deleteAllTasks/$', views.deleteAllTasks, name='deleteAllTasks'),
    url(r'^aboutMe/$', views.aboutMe, name='aboutMe'),
]
