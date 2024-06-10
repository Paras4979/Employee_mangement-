from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')



def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept_id=int(request.POST['dept_id'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        role=int(request.POST['role'])
        new_emp=Employee(first_name=first_name,last_name=last_name,dept_id=dept_id,role_id=role,salary=salary,bonus=bonus,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
        

    elif request.method=='GET':
        return render(request,'add.html')
    else:
        return HttpResponse('Failed to add Employee')
         




    


def view_emp(request):
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request,'view.html',context)


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_r=Employee.objects.get(id=emp_id)
            emp_r.delete()
            return HttpResponse('Deleted successfuly')
        except:
            return HttpResponse('Enter valid details')
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove.html',context)


def filter_emp(request):
    if request.method=='POST':
        name=request.POST['first_name']
        dep=request.POST['dept_id']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dep:
            emps=emps.filter(dept_id__name=dep)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request,'view.html',context)
    elif request.method=='GET':
        return render(request,'filter.html') 
    else:
        HttpResponse('Error Occured')

       

    


