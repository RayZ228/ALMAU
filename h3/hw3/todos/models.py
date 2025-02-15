from django.db import models

# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=100)

    description = models.CharField(max_length=100)

    due_date = models.DateField(max_length=100)

    status = models.BooleanField(max_length=100)

    def __str__(self):
        return self.title