from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # update_date = models.DateTimeField(default=timezone.now)
    id_user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    