from django.db import models
# Create a user authentication and referal system using Django.

# Create your models here.

class User(models.Model):
    username = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    
    
    def __str__(self):
        return self.username
    