from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, related_name='Profile')
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)


    def __str__(self):
        return self.username


class Message(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False,blank=False)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.text

