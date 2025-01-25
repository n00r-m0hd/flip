from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    is_active = models.BooleanField(default=True)


class Book(Base):
    name = models.CharField(max_length=300,null=True,blank=True)
    author = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Student(Base):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    books = models.ManyToManyField(Book, related_name='students') 

    def __str__(self):
        return self.user.first_name if self.user is not None else "None"
