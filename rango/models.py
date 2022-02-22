from tabnanny import verbose
from turtle import title
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # when unique=True, it can be a primary key
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    # will override the save() method of the Category method
    slug = models.SlugField(unique=True)

    # save the file from with spaces to without spaces
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    # solve the typo issue
    class Meta:
        verbose_name_plural = 'Categories'

    # this is useful for print()
    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    # We can set the default as 0. And also we can set null=True or null=Flase to say whether the attribute can be null

    def __str__(self):
        return self.title