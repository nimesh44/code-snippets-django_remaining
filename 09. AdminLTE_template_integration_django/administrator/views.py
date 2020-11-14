from django.shortcuts import render

# Create your views here.
def administrator(request):
    return render(request,'administrator/admin_home.html')
