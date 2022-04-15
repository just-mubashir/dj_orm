# from django import forms
# # from . models import Employee
# # from django.core import validators

# class add_emp_form(forms.Form):
#     avatar = forms.FileField(required=False)
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     age = forms.IntegerField(required=True)
#     gender_choices = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('X', 'Don`t want to disclose')
#     )
#     gender = forms.ChoiceField(choices=gender_choices)
#     phone = forms.CharField(required=True)
#     email = forms.EmailField(required=True)
#     department = forms.CharField(required=True)
#     designation = forms.CharField(required=True)
#     date_join = forms.DateField(required=True)
#     salary = forms.IntegerField(required=True)
#     HRA_variables = forms.IntegerField(required=True)
#     incentives = forms.IntegerField(required=True)
#     address = forms.Textarea()



# # INSTEAD OF REPEATING ALLCODE JUST USE MODEL FORM

# class add_emp_form(forms.ModelForm):
#     class Meta:
#         model = Employee
#         # fields = ('__all__')    
#         fields = (
#             'avatar',
#             'first_name',
#             'last_name',
#             'age',
#             'gender',
#             'phone',
#             'email',
#             'department',
#             'designation',
#             'date_join',
#             'salary',
#             'HRA_variables',
#             'incentives',
#             'address'
#         )    
