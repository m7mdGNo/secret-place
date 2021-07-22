from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True, related_name='Profile')
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    bio = models.CharField(max_length=100,default='Hello ,iam member in secret-space')
    img = models.ImageField(null=True, blank=True,upload_to='profiles/',default='images/test.png')


    def __str__(self):
        return self.username
    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        size = 200,200
        if self.img:
            pic = Image.open(self.img.path)
            pic.thumbnail(size,Image.LANCZOS)
            pic.save(self.img.path)

class Message(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=False,blank=False)
    text = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.text

