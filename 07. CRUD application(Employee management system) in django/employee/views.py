from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee


# Create your views here.


def home(request):
    return render(request,'home.html')

# context = {
#     'ceo':{
#                 'name':'Netra Prasad Neupane',
#                 'gender':'Male'
#     },
#     'hr':{
#                 'name':'Hari Neupane',
#                 'gender':'Female'
#     }
# }

def employee(request):
    if request.method == 'POST':
        # Getting data from form
        data = request.POST
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        mobile = data['mobile']
        address = data['address']

        # adding data to database/model
        obj = Employee.objects.create(first_name = first_name, last_name = last_name,email = email,
               mobile = mobile, address = address)

        if obj:# If object is created then redirect to /employee
            # redirect is alternative of render
            return redirect('employee-home')

    else:
        Employees = Employee.objects.all()
        form = EmployeeForm()
        context ={
            'form':form,
            'employees': Employees,
        }
    return render(request,'employee/employee.html',context)



def broker(request):
    form = EmployeeForm()
    context ={
        'form':form,
    }
    return render(request,'broker.html',context)


def about(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data['email']
        address = data.get('address')

        context_ ={
            'title':'employeer',
            'first_name':first_name,
            'last_name':last_name,
            'email': email,
            'address':address,

        }


    else:
        context_ ={
            'title':'employeer',
            'first_name':'None',
            'last_name':None,
            'email':'None',
            'address':'None',
            }

    return render(request,'about.html',context_)




def contact(request):
    return render(request,'contact.html')


# one way of of getting id/any other info is
# def employee_update(request,**kwar):
# Alternative way
def employee_update(request,id):
    employee_obj = Employee.objects.get(id=id)
    # print(id)
    # print(employee_obj.first_name)
    if request.method == 'POST':
        employee_obj.first_name = request.POST['first_name']
        employee_obj.last_name = request.POST['last_name']
        employee_obj.email = request.POST['email']
        employee_obj.mobile = request.POST['mobile']
        employee_obj.address = request.POST['address']
        employee_obj.save()
        # print(employee_obj.first_name)
        return redirect('employee-home')

    context={
        'employee':employee_obj,
    }



    return render(request,'employee/employee_update.html',context)
