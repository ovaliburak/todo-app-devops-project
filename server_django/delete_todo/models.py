from django.db import models

class Todo(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    todo_id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'todo'
