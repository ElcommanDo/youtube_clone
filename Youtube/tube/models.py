from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    file = models.FileField(upload_to='videos')
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    thumb = models.ImageField(upload_to='thumb',null=True,blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):

    content = models.TextField(max_length=600)
    datetime = models.DateTimeField(blank=False,null=False,auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.content


