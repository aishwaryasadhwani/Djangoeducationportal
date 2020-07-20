from django import forms
from django.forms import modelformset_factory
from portalapp.models import Addclass,Subjects,Institute,Student,Employee,AccountIncome,AccountExpense,Account,StudentAttendance
from functools import partial
 # from bootstrap_datepicker_plus import DatePickerInput

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
class DateInput(forms.DateInput):
    input_type = 'date'

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

class AddIncomeForm(forms.ModelForm):
    class Meta:
        model = AccountIncome
        fields = '__all__'
        widgets = {
            'Month': DateInput(),
        }


class AddExpenseForm(forms.ModelForm):
    class Meta:
        model = AccountExpense
        fields = '__all__'
        widgets = {
            'Month': DateInput(),
        }

class StudentAttendanceForm(forms.ModelForm):
    class Meta:
        model = StudentAttendance
        fields = '__all__'
        widgets = {
        'Date':DateInput(),
        }
