from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Employeer(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email    = models.EmailField(max_length = 20)
    mobile = models.CharField(unique=True,max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    address = models.CharField(max_length =30)

    # To show employeer name  for each object in table in admin panel
    def __str__(self):
        return self.first_name +" "+ self.last_name
