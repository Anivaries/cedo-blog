from django.db import models

class Blog(models.Model):
    text = models.TextField()
    # author
    title = models.CharField(max_length=50)
    # date
    # tags