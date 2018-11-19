from django.db import models
from django.contrib.auth.models import User
from labMat.models import Center


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    
class User_Center(models.Model):
    center = models.OneToOneField(Center, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) + " - " + str(self.center)
