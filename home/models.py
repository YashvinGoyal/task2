from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length=10)
    email = models.CharField(max_length=20)
    uname = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    img=models.FileField(default="")
    address = models.CharField(max_length=20)
    work = models.CharField(max_length=10)
    
    def __str__(self):
        return self.uname

class bloggg(models.Model):
    sno=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,default="")
    title=models.CharField(max_length=15)
    draft=models.BooleanField(default=False)
    img=models.FileField(default="")
    cat=models.CharField(max_length=15)
    summ=models.TextField(max_length=50)
    con=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.user.username