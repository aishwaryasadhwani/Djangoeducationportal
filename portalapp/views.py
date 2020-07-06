from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Addclass,Subjects,Institute,Student,Employee,AccountIncome,AccountExpense,Account
from .forms import AddclassForm,SubjectForm,InstituteForm,StudentForm,EmployeeForm,AddIncomeForm,AddExpenseForm
# from bootstrap_datepicker_plus import DateTimePickerInput
from django.views.generic import UpdateView,CreateView
from .filters import StudentFilter
from django.db.models import Sum


# Create your views here.
def dashboard(request):
    return render(request,'portalapp/index.html')

def login(request):
    return render(request,'registration/login.html')

def Addclasses(request):
    form = AddclassForm()
    dict = {'form':form}
    if request.method == 'POST':
        obj = AddclassForm(request.POST)
        obj.save()
        dict.update({'msg':" Class Added Successfully"})
    return render(request,'portalapp/addclass_form.html',dict)

def Allclasses(request):
    allclass = Addclass.objects.all()
    if request.method == 'POST' and 'delete' in request.POST:
        dropdown_val = request.POST.get('dropdownlist')
        print("true")
        print(dropdown_val)
        return HttpResponseRedirect("/delete/"+dropdown_val)
    elif request.method == 'POST' and 'update' in request.POST:
        dropdown_val = request.POST.get('dropdownlist')
        print("true")
        print(dropdown_val)
        return HttpResponseRedirect('/update/'+dropdown_val)

    return render(request,'portalapp/allclasses.html',{'allclass':allclass})

def ViewClasses(request):
    obj = Addclass.objects.all()
    return render(request,'portalapp/viewclasses.html',{'obj':obj})

class UpdateClasses(UpdateView):
    model = Addclass
    fields = '__all__'

def Deleteclasses(request,pk):
        obj = Addclass.objects.get(id = pk)
        if request.method == 'POST':
            obj.delete()
            return HttpResponseRedirect('/dashboard')
        return render(request,'portalapp/delete.html')


def AddSubjects(request):
    obj = SubjectForm()
    dict = {'obj':obj}
    if request.method == 'POST':
        obj = SubjectForm(request.POST)
        obj.save()
        dict.update({'msg':" Class Added Successfully"})
    return render(request,'portalapp/addsubject.html',dict)


def ViewSubjects(request):
    obj = Addclass.objects.all()
    return render(request,'portalapp/subject.html',{'obj':obj})


def AddInstitute(request):
    institute= InstituteForm()
    if request.method == 'POST':
        Instituteform= InstituteForm(request.POST,request.FILES)
        if Instituteform.is_valid():
            # print(InstituteForm.errors)
            print("helllo")
            Instituteform.save(commit=True)
            # data.save(commit=True)
            return HttpResponseRedirect('/viewinfo')
    return render(request,'portalapp/addinstitute_form.html',{'obj':institute})

def ViewInstitute(request):
    obj = Institute.objects.last()
    return render(request,'portalapp/viewinstitute.html',{'obj':obj})

def CreateStudent(request):
    student = StudentForm()
    if request.method == 'POST':
        studentform = StudentForm(request.POST,request.FILES)
        if studentform.is_valid():
            studentform.save(commit=True)
            return HttpResponseRedirect('/all')
        else:
            print("helllllo",studentform.errors)
    return render(request,'portalapp/student_form.html',{'form':student})

class UpdateStudents(UpdateView):
    model = Student
    fields = '__all__'
    def get_success_url(self):
            return reverse('viewstudent')

def DeleteStudents(request,pk):
        obj = Student.objects.get(id = pk)
        if request.method == 'POST':
            obj.delete()
            return HttpResponseRedirect('/dashboard')
        return render(request,'portalapp/delete.html')

def SearchStudent(request,pk):
    obj = Student.objects.get(id=pk)
    return render(request,'portalapp/searchstudent.html',{'obj':obj})

def ViewStudents(request):
    obj = Student.objects.all()
    if request.method == 'POST' and 'search' in request.POST:
        val = request.POST.get('search')
        return HttpResponseRedirect("/view/"+val)



    # if request.method == 'POST' and 'name' in request.POST:
    #     print('jjjjjjjjjjjjjjjjjjjjjjjjjjjjj')
    #     val = request.POST.get('name')
    #     print("heyyyyyyyyyyyyyyyyyy",val)
    #     # print(val.id)
    #     # id1 = val.id
    #     obj = Student.objects.filter(StudentName=val)
    #     print("helllllllllllllloooooooooo",obj)
    #     return HttpResponseRedirect("/view/"+obj)

    return render(request,'portalapp/viewstudent.html',{'obj':obj})

def ViewOne(request,pk):
    obj = Student.objects.get(id=pk)
    return render(request,'portalapp/view.html',{'obj':obj})


def Admission(request):
    if request.method == 'POST' and 'adminid' in request.POST:
        val = request.POST.get('adminid')
        obj = Student.objects.get(id=val)
        return HttpResponseRedirect('/print/'+val)
    return render(request,'portalapp/admission.html')

def PrintLetter(request,pk):
    obj = Student.objects.get(id=pk)
    return render(request,'portalapp/print.html',{'obj':obj})

# def search(request):
#     user_list = Student.objects.all()
#     user_filter = UserFilter(request.GET, queryset=user_list)
#     return render(request, 'portalapp/viewstudent.html', {'filter': user_filter})


# class Create(CreateView):
#     model = Student
#     form_class = StudentForm
#     def get_success_url(self):
#         return reverse('/all')

def CreateEmp(request):
    obj = EmployeeForm()
    if request.method == 'POST':
        empform = EmployeeForm(request.POST,request.FILES)
        if empform.is_valid():
            empform.save(commit=True)
            return HttpResponseRedirect('/allemp')
        else:
            print("helllllo",studentform.errors)
    return render(request,'portalapp/employee_form.html',{'form':obj})

def AllEmp(request):
    obj = Employee.objects.all()
    if request.method == 'POST' and 'search' in request.POST:
        val = request.POST.get('search')
        obj = Employee.objects.get(id=val)
        return HttpResponseRedirect('/filter/'+val)
    return render(request,'portalapp/allemp.html',{'obj':obj})

def SearchEmp(request,pk):
    obj = Employee.objects.get(id=pk)
    return render(request,'portalapp/searchemp.html',{'obj':obj})

class UpdateEmployee(UpdateView):
    model = Employee
    fields = '__all__'
    def get_success_url(self):
            return reverse('allemp')

def DeleteEmployee(request,pk):
        obj = Employee.objects.get(id = pk)
        if request.method == 'POST':
            obj.delete()
            return HttpResponseRedirect('/dashboard')
        return render(request,'portalapp/delete.html')

def FilterEmp(request):
    if request.method == 'POST' and 'search' in request.POST:
        val = request.POST.get('search')
        obj = Employee.objects.get(id=val)
        return HttpResponseRedirect('/filter/'+val)

def Filter(request,pk):
    obj = Employee.objects.get(id=pk)
    return render(request,'portalapp/filteremp.html',{'obj':obj})

def AddIncome(request):
    obj = AddIncomeForm()
    if request.method == 'POST':
        addform = AddIncomeForm(request.POST)
        if addform.is_valid():
            addform.save(commit=True)
            return HttpResponseRedirect('/dashboard')
    return render(request,'portalapp/addincome.html',{'obj':obj})


def AddExpense(request):
    obj = AddExpenseForm()
    if request.method == 'POST':
        addform = AddExpenseForm(request.POST)
        if addform.is_valid():
            addform.save(commit=True)
            return HttpResponseRedirect('/dashboard')
    return render(request,'portalapp/addexpense.html',{'obj':obj})

def AccountStatement(request):
    obj_income = AccountIncome.objects.all()
    obj_expense = AccountExpense.objects.all()

    if len(obj_expense) > 0 and len(obj_income) > 0 :
            sum_credit = list(AccountIncome.objects.aggregate(Sum('IncomeAmount')).values())[0]
            sum_debt = list(AccountExpense.objects.aggregate(Sum('ExpenseAmount')).values())[0]
            net = sum_credit - sum_debt

    elif len(obj_income)>0:
        sum_credit = list(AccountIncome.objects.aggregate(Sum('IncomeAmount')).values())[0]
        net = sum_credit - 0

    elif len(obj_expense)>0:
        sum_debt = list(AccountExpense.objects.aggregate(Sum('ExpenseAmount')).values())[0]
        net = 0 - sum_debt

    else:
        net = 0

    return render(request,'portalapp/accountstate.html',{'obj_income':obj_income,'obj_expense':obj_expense,'net':net})


def Accounts(request):
    obj = Account.objects.all()
    return render(request,'portalapp/accounts.html',{'obj':obj})
