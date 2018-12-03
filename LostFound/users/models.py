from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
	# name = models.CharField(max_length=255)
	# createdDate = models.DateTimeField(default=timezone.now)
	#createdDate DATE NOT NULL
    udpdateDate = models.DateTimeField(default=timezone.now)
	#updatedDate DATE NOT NULL
    image = models.ImageField(default ='imgProfileDefault.jpg',upload_to='profile_pics')
	#image VARCHAR(255) NOT NULL
	# role = models.BooleanField(default = 0)
	#role INT NOT NULL
    phone = models.CharField(max_length=13)
	#phone VARCHAR(255) NOT NULL
	# email = models.CharField(max_length=255)
	#email VARCHAR(255) NOT NULL
    line = models.CharField(max_length=255)