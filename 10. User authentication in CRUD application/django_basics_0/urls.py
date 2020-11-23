"""django_basics_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from employeer.views import employeer,employeer_add,employeer_update,employeer_delete
# from employee.views import employee
from django.conf import settings
from django.conf.urls.static import static


# def home(request):
#     return HttpResponse("<h2>This is Home Page</h2>")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',home),
    path('',include('employee.urls')),
    # path('employee/',include('employee.urls')),
    path('employeer/',employeer,name="employeer-home"),
    path('employeer/employeer_add/',employeer_add,name="employeer-add"),
    path('employeer/employeer_update/<int:id>/',employeer_update,name="employeer-update"),
    path('employeer/employeer_delete/<int:id>/',employeer_delete,name="employeer-delete"),
    path('users/',include('user.urls')),

]

# SECURITY WARNING: don't run with debug turned on in production!
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
