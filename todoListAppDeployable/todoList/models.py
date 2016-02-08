from google.appengine.ext import ndb

# Create your models here.
class Task(ndb.Model):
    taskText = ndb.StringProperty()

    def getKind(self):
        return self.key.kind()

    def getId(self):
        return self.key.id()

    def __str__(self):
        return self.taskText
