from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.urls import reverse

# https://pypi.org/project/django-tinymce/
# Create your models here.
# Category model



class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/images/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;border-radius:50%"  /> '.format(self.image))
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')



#Post mode


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/images/',null=True)
    likes = models.ManyToManyField(User , blank=True , related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

    def get_image_url(self):
        return f"/media/{self.image}"

class Comment(models.Model):
    post = models.ForeignKey(Post , related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)

class BlogPost(models.Model):
    ...
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()




