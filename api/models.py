from django.db import models

class Task(models.Model):
    Due_Date = models.DateTimeField()
    Title = models.CharField(max_length = 128)
    Text = models.TextField()

    def __str__(self):
        return self.Title
