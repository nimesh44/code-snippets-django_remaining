from django.urls import path
from . import views

urlpatterns =[
            path('',views.home,name="home"),
            path('home/',views.home,name="home"),
            path('employee/',views.employee,name="employee-home"),
            path('broker/',views.broker,name ="broker-home"),
            path('about/',views.about,name="about"),
            path('contact/',views.contact,name="contact"),
            path('employee_update/<int:id>/',views.employee_update,name="employee-update"),
            path('employee_delete/<int:id>/',views.employee_delete,name="employee-delete"),

]
