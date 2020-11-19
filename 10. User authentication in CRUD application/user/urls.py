from django.urls import path
from . import views


urlpatterns = [
        path('register/',views.user_register,name="user-register"),
        path('login/',views.user_login,name="user-login")
]