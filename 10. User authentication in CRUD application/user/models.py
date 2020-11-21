from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    phone = models.CharField(max_length = 20)

















"""
# Create your models here.
class Profile(User):
    class Meta:
        proxy = True

    # Proxy model is used if we need to apply method on the model fields
    def get_full_name(self):
        return self.first_name + self.last_name
"""
