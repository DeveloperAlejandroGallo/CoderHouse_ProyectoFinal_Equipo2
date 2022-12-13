from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    about_me = models.TextField()
    github = models.URLField()

class Chat(models.Model):

    writer = models.CharField(max_length=50)
    body = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.writer} a {self.recipient} |{self.id}'

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f'{self.user} | Avatar'

class UserAbout(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    bio = models.TextField()
    instagram = models.URLField()
    facebook = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return f'{self.user} | About'


