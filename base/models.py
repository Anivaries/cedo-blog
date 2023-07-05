from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
    

class Article(models.Model):

    CATEGORY = (
        ('Review','Review'),
        ('News','News'),
        ('Opinion','Opinion'),
        ('Hardware','Hardware'),
        )
    
    game_name = models.CharField(max_length=30)
    text = models.TextField()
    title = models.CharField(max_length=120)
    pub_date = models.DateTimeField("date published", auto_created = True)
    slug = models.SlugField(default="slug-one", max_length=70)
    category = models.CharField(max_length=10, choices=CATEGORY, default='Review')
    # author
    # tags

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"slug": self.slug})
    