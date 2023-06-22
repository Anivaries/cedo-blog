from django.db import models

class Blog(models.Model):
    text = models.TextField()
    # author
    title = models.CharField(max_length=120)
    pub_date = models.DateTimeField("date published", auto_created = True)
    slug = models.SlugField(default="slug-one", max_length=70)
    # tags

    def __str__(self) -> str:
        return self.title