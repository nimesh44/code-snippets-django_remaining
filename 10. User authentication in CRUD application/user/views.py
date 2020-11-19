from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



# Removing help text

class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None


# Create your views here.
def register_users(request):
    if request.method == 'POST':
        data = UserCreateForm(request.POST)
        if data.is_valid():
            data.save()
            return redirect('home')


    form = UserCreateForm()
    context = {
            'form': form,
    }
    return render(request,'user/user_register.html',context)
