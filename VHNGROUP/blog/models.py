from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 


# Creamos una tabla de nombre Post. con las columnas title, slug y body
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, #Creamos una relacion con el modelo User
                                on_delete=models.CASCADE, 
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # status de la publicacion segun la clase Status
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT) 
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    def __str__(self):
        return self.title