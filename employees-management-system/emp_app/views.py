from django.shortcuts import render, HttpResponse
from emp_app.models import Employee

# Create your views here.

def index(request):
    return render(request, "index.html")

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, "all_emp.html", context)

def add_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        role = request.POST['role']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        new_emp = Employee(name=name, role=role, salary=salary, bonus=bonus, phone=phone)
        new_emp.save()
        return HttpResponse("Added Successfully")
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("Error")

def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Removed")
        except:
            return HttpResponse("enter valid id")
    emps=Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context)
