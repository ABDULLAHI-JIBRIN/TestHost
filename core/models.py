from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class Category(models.Model):

    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=25)
    content = models.TextField()
    is_complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add = True)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('core:detail', kwargs = {'id':self.id})


