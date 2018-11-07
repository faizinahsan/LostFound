from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# <<<<<<< HEAD

class Post(models.Model):
	"""docstring for ClassName"""
	title = models.CharField(max_length=255)
	#title VARCHAR(255) NOT NULL
	latitude = models.FloatField()
	#latitude DOUBLE NOT NULL
	longitude = models.FloatField()
	#longitude DOUBLE NOT NULL
	area = models.CharField(max_length=255)
	#area VARCHAR(255) NOT NULL
	body = models.TextField()
	#body TEXT NOT NULL
	image = models.CharField(max_length=255)
	#image VARCHAR(255) NOT NULL
	createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL
	updatedDate = models.DateTimeField(default=timezone.now)
	#updatedDate DATE NOT NULL
	state = models.BooleanField()
	#state INT NOT NULL
	idUsers = models.ForeignKey(User, on_delete=models.CASCADE)
	#idUsers INT NOT NULL
	#FOREIGN KEY (idUsers) REFERENCES User(id)
	idCategories = models.ForeignKey(Category, on_delete=models.CASCADE)
	#idCategories INT NOT NULL
	#FOREIGN KEY (idCategories) REFERENCES Category(id)
	idTypes = models.ForeignKey(Type, on_delete=models.CASCADE)
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

class User(models.Model):
	name = models.CharField(max_length=255)
	#name VARCHAR(255) NOT NULL
	username = models.CharField(max_length=255)
	#username VARCHAR(255) NOT NULL
	password = models.CharField(max_length=255)
	#password VARCHAR(255) NOT NULL
	createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL
	updatedDate = models.DateTimeField(default=timezone.now)
	#updatedDate DATE NOT NULL
	image = models.CharField(max_length=255)
	#image VARCHAR(255) NOT NULL
	role = models.BooleanField()
	#role INT NOT NULL
	phone = models.CharField(max_length=13)
	#phone VARCHAR(255) NOT NULL
	email = models.CharField(max_length=255)
	#email VARCHAR(255) NOT NULL
	line = models.CharField(max_length=255)
	#line VARCHAR(255) NOT NULL
	
	
# class Registration(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
