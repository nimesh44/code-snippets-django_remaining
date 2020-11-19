from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register_users(request):
    form = UserCreationForm()
    context = {
            'form': form,
    }
    return render(request,'user/user_register.html',context)
