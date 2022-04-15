from django.http import HttpResponseBadRequest
from django.shortcuts import render, HttpResponse
from . models import Department, Role, Employee
from datetime import datetime
from django.db.models import Q
# from . forms import add_emp_form
# Create your views here.
def index(request):
    return render (request, 'index.html')

def all_emp(request):
    employee_all = Employee.objects.all()
    params = {'employee_all' : employee_all}
    return render (request, 'all_emp.html', params)

def delete_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Deleted Successfully')
        except:
            return HttpResponseBadRequest
    employee_all = Employee.objects.all()
    params = {'employee_all' : employee_all}
    return render (request, 'delete_emp.html', params)

def add_emp(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        gender = request.POST['gender']
        phone = request.POST['phone']
        email = request.POST['email']
        department = request.POST['department']
        designation = request.POST['designation']
        date_join = request.POST['date_join']
        salary = request.POST['salary']
        HRA_variables = request.POST['HRA_variables']
        incentives = request.POST['incentives']
        address = request.POST['address']
        new_emp = Employee(
            first_name = first_name,
            last_name = last_name,
            age = age,
            gender = gender,
            phone = phone,
            email = email,
            department_id = department,
            designation_id = designation,
            date_join = datetime.now(),
            salary = salary,
            HRA_variables = HRA_variables,
            incentives = incentives,
            address = address
                            )
        new_emp.save()
        return HttpResponse('Saved Successfully')

    elif request.method == 'GET':
        return render (request, 'add_emp.html')

    else:
        return HttpResponseBadRequest

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        department = request.POST['department']
        designation = request.POST['designation']
        employee_all = Employee.objects.all()
        if name:
            employee_all.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        else:
            return HttpResponse("NO EMPLOYEE FOUND")
        if department:
            employee_all.filter(department__name__icontains = department)
        if designation:
            employee_all.filter(designation__name__icontains = designation)
        
        params = {'employee_all' : employee_all}
        return render(request, 'all_emp.html', params )
    elif request.method == 'GET':
        return render (request, 'filter_emp.html')
    else:
        return HttpResponse("UNEXPECTED ERROR OCCURED !! TRY AGAIN !!")




















# def adding_emp_form(request):
#     User_Input_Form = add_emp_form()
# adding forms
# def add_emp(request):
#     if request.method == 'POST':
#         forms = add_emp_form(request.POST)
#         if forms.is_valid():
#             avatar_db= forms.cleaned_data['avatar']
#             first_name_db= forms.cleaned_data['first_name']
#             last_name_db= forms.cleaned_data['last_name']
#             age_db= forms.cleaned_data['age']
#             gender_db= forms.cleaned_data['gender']
#             phone_db= forms.cleaned_data['phone']
#             email_db= forms.cleaned_data['email']
#             department_db= forms.cleaned_data['department']
#             designation_db= forms.cleaned_data['designation']
#             date_join_db= forms.cleaned_data['date_join']
#             salary_db= forms.cleaned_data['salary']
#             HRA_variables_db= forms.cleaned_data['HRA_variables']
#             incentives_db= forms.cleaned_data['incentives']
#             address_db= forms.cleaned_data['address']

#             save_forms = add_emp_form(
#                 avatar = avatar_db,
#                 first_name = first_name_db,
#                 last_name = last_name_db,
#                 age = age_db,
#                 gender = gender_db,
#                 phone = phone_db,
#                 email = email_db,
#                 department = department_db,
#                 designation = designation_db,
#                 date_join = date_join_db,
#                 salary = salary_db,
#                 HRA_variables = HRA_variables_db,
#                 incentives = incentives_db,
#                 address = address_db
#             )
#         save_forms.save()
#         forms = add_emp_form()
#     else:
#         forms = add_emp_form()

#     return render (request, 'add_emp.html',{'form': forms})