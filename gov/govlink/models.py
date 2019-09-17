from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField




# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)
    logo = models.ImageField(null=True, blank=True, upload_to="headshots/")
    creator = models.ForeignKey(User, on_delete=models.CASCADE,)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse('', args=[self.category])
    
class Post(models.Model):     
    category = models.ForeignKey(Category, on_delete=models.CASCADE,)
    coursename = models.CharField(max_length=50)
    amount = models.CharField(max_length=10)
    content = RichTextField(default = 'content', blank = True, null = True)
    img = models.ImageField(null=True, blank=True, upload_to="headshots/")
    view_count = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    popular = models.BooleanField(null=True, blank=True)

    
    date_1 = models.DateField(null=True, blank=True)
    date_2 = models.DateField(null=True, blank=True)
    date_3 = models.DateField(null=True, blank=True)
    date_4 = models.DateField(null=True, blank=True) 
    date_5 = models.DateField(null=True, blank=True)
    date_6 = models.DateField(null=True, blank=True) 
    date_7 = models.DateField(null=True, blank=True)
    date_8 = models.DateField(null=True, blank=True) 

   