from django import forms
from django.forms import ModelForm
from .models import Employeer

class EmployeerForm(ModelForm):
    # first_name = models.CharField(max_length = 10)
    # last_name = models.CharField(max_length = 10)
    # username = forms.CharField(max_length=10)
    # email = forms.EmailField(max_length=20)
    # password = forms.CharField(max_length=20)
    address = forms.CharField(max_length=30)

    class Meta:
        model = Employeer
        fields = ['first_name','last_name','email','mobile','address']
        # To get all fields do
        # fields = '__all__'
