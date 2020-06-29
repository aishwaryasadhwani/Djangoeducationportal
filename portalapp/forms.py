from django import forms
from django.forms import modelformset_factory
from portalapp.models import Addclass,Subjects,Institute,Student,Employee
from functools import partial


class AddclassForm(forms.ModelForm):
    class Meta:
        model = Addclass
        fields = '__all__'

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields ='__all__'

class InstituteForm(forms.ModelForm):
    class Meta:
        model = Institute
        fields ='__all__'

# class DateInput(forms.DateInput):
#     input_type = 'date'

# DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= '__all__'
        widgets = {'AdmissionDate':forms.DateInput(attrs={'class':'datepicker'})}

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {'JoiningDate':forms.DateInput(attrs={'class':'datepicker'})}
