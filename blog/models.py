from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

#auto_now = True  -> update date after each editing
#auto_now_add = True -> only when created but you can not update this date 
#timezone.now -> why not () because we dont need to execute this we want only pass this like action fucntion
#python manage.py sqlmigrate blog 0001
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    