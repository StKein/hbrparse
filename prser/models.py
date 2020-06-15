""" Project models """
from django.db import models

""" Model for parsed Habr posts """
class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    time = models.DateTimeField()

    """ Text short version for posts list """
    @property
    def annonce(self):
        return self.text.replace('\r','').replace('\n',' ')[:700]
    
    """ Inner link to show how to get certain post in API """
    @property
    def inner_link(self):
        return '/api/posts/{}'.format(self.id)
    
    """ Model meta class """
    class Meta:
        ordering = ['-time']