from django.shortcuts import render,redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserLoginForm,ProfileForm
from django.contrib.auth import authenticate,login,logout



# Removing help text
# To avoid help text use UserCreateForm modelForm instead of UserCreationForm
class UserCreateForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None


def user_register(request):
    if request.method == 'POST':
        data = UserCreateForm(request.POST)
        if data.is_valid():
            # To remove help text
            data = data.cleaned_data
            user = User.objects.create(username = data['username'])
            # To hash password
            user.set_password(data['password1'])
            user.save()

            return redirect('user-login')
    form = UserCreateForm()
    context = {
            'form': form,
    }
    return render(request,'user/user_register.html',context)



# # views to avoid removing help text
# def user_register(request):
#     if request.method == 'POST':
#         data = UserCreationForm(request.POST)
#         if data.is_valid():
#             # without removing help text
#             data.save()
#             return redirect('home')
#     form = UserCreationForm()
#     context = {
#             'form': form,
#     }
#     return render(request,'user/user_register.html',context)



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print(form)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request,username = data['username'],password = data['password'])
            print(user)
            # IF USER EXIST IN MODEL
            if user is not None:
                login(request,user)
                return redirect('home')

    form = UserLoginForm()
    context = {
        'form': form,
    }
    return render(request,'user/user_login.html',context)


def user_logout(request):
    # To logout user
    logout(request)
    return redirect('user-login')


def user_profile(request):
    form = ProfileForm(initial = {
                    'first_name':'Netra Prasad',
                    'last_name': 'Neupane',
                    'email':'npn@company.com',
                })
    context = {
        'form':form
    }
    return render(request,'user/user_profile.html',context)
