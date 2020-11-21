from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email    = models.EmailField(max_length = 20)
    mobile = models.CharField(unique = True,max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    address = models.CharField(max_length =30)

    # To return name of employee of each objects/row in table in admin panel
    def __str__(self):
        return self.first_name +' '+ self.last_name
