from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=50)
#     body = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     # update_date = models.DateTimeField(default=timezone.now)
#     id_user = models.ForeignKey(User,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.title
class Post(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=255)
	#title VARCHAR(255) NOT NULL
	latitude = models.FloatField(default=0.0)
	#latitude DOUBLE NOT NULL
	longitude = models.FloatField(default=0.0)
	#longitude DOUBLE NOT NULL
	area = models.CharField(max_length=255, default='Tidak Diketahui')
	#area VARCHAR(255) NOT NULL
	body = models.TextField()
	#body TEXT NOT NULL
	image = models.ImageField(max_length=255, default='imgBlogDefault.jpg',upload_to='image_blog')
	#image VARCHAR(255) NOT NULL
	createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL
	updatedDate = models.DateTimeField(default=timezone.now)
	#updatedDate DATE NOT NULL
	state = models.BooleanField(default=False)
	#state INT NOT NULL
	idUsers = models.ForeignKey(User, on_delete=models.CASCADE)
	#idUsers INT NOT NULL
	#FOREIGN KEY (idUsers) REFERENCES User(id)
	idCategories = models.ForeignKey('Category', on_delete=models.CASCADE,default=0)
	#idCategories INT NOT NULL
	#FOREIGN KEY (idCategories) REFERENCES Category(id)
	idTypes = models.ForeignKey('Types', on_delete=models.CASCADE,default=0)
	#idTypes INT NOT NULL
	#FOREIGN KEY (idTypes) REFERENCES Type(id)

class Category(models.Model):
	name = models.CharField(max_length=255)
	#name VARCHAR(255) NOT NULL
	createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL

class Types(models.Model):
	name = models.CharField(max_length=255)
	#name VARCHAR(255) NOT NULL
	createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL

class Log(models.Model):
	body = models.TextField()
	#body TEXT NOT NULL
	createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL
	idUsers = models.ForeignKey(User, on_delete=models.CASCADE)
	#idUsers INT NOT NULL
	#FOREIGN KEY (idUsers) REFERENCES User(id)
	idPosts = models.ForeignKey(Post, on_delete=models.CASCADE)
	#idPosts INT NOT NULL
	#FOREIGN KEY (idPosts) REFERENCES Post(id)