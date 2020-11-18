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


def employeer_add(request):
    form = EmployeerForm()
    if request.method == 'POST':
        employeer_data = EmployeerForm(request.POST)
        if employeer_data.is_valid():
            employeer_data.save()
            return redirect('employeer-home')

    context = {
    'form':form,
    'action':'Add New employeer'
    }
    return render(request,'employeer/employeer_add.html',context)

def employeer_update(request,id):
    instance  = Employeer.objects.get(id=id)
    form = EmployeerForm(instance=instance)
    if request.method == 'POST':
        form_data = EmployeerForm(request.POST,instance = instance)
        if form_data.is_valid():
            form_data.save()
            return redirect('employeer-home')
    context = {
    'form':form,
    'action':'Update Employeer Details'
    }
    # Using template similar to add for update employeer
    return render(request,'employeer/employeer_add.html',context)

def employeer_delete(request,id):
    employeer_instance = Employeer.objects.get(id=id)
    if request.method == 'POST':
        employeer_instance.delete()
        return redirect('employeer-home')

    context ={
        'employeer': employeer_instance,
        }
    return render(request,'employeer/employeer_delete.html',context)
