from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeerForm
from .models import Employeer







# Create your views here.
def employeer(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        mobile = data['mobile']
        address = data['address']

        # save objects to Employeer model in database
        obj = Employeer.objects.create(first_name= first_name,last_name=last_name,email=email,
              mobile= mobile,address = address)

        # If objects is created then redirect to home page
        if obj:
            return redirect('employeer-home')

    else:
        Employeers = Employeer.objects.all()
        form = EmployeerForm()
        context = {
            'form':form,
            'employeers':Employeers,
        }

    return render(request,'employeer/employeer.html',context)

    # if request.method = request.POST:
    #     data = request.POST
    #     print(data)
    #     # Two ways of accessing dictionary key value pairs
    #     print(data['email'])
    #     print(data.get('email'))
    #     return render(request,'employeer/employeer.html')
    # else:
    #     return render(request,'employeer/employeer.html')
