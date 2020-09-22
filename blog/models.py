from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='post_pictures')
    tag = models.CharField(max_length=255, default='Post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # def get_absolute_url(self):
    #     return reverse('article-detail', kwargs={'pk': self.object.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_pictures')

    def __str__(self):
        return str(self.user)

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            resize = (300, 300)
            img.thumbnail(resize)
            img.save(self.profile_pic.path)
