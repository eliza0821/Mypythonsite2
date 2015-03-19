from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=140)
    body=models.TextField()
    date=models.DateTimeField()

    def __unicode__(self):
        return self.title
