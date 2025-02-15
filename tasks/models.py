from django.db import models
from django.utils.text import slugify

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()
    
    
    @classmethod
    def get_default_collection(cls) -> 'Collection':
        collection, _ = cls.objects.get_or_create(name="Default", slug="_default")
        return collection
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    description = models.TextField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(unique=True)

    @classmethod
    def get_default_collection(cls):
        collection, _ = cls.objects.get_or_create(name="Default", slug="_default")
        return collection

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.name)
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']

class Task(models.Model):
    description = models.TextField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.description

    class Meta:
        ordering = ['description']