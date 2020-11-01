from django.forms import ModelForm
from employeer.models import Employeer
from django.core.validators import RegexValidator
from django import forms


class EmployeeForm(ModelForm):
    # mobile = forms.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    address = forms.CharField(max_length=30)
    class Meta:
        model = Employeer
        fields = ['first_name','last_name','email','mobile','address']
