from django.db import models
from django_countries.fields import CountryField
# Create your models here.

class Addclass(models.Model):
    name = models.CharField(max_length=255)
    fees = models.FloatField()

    def __str__(self):
        return self.name

class Subjects(models.Model):
    subjectname = models.CharField(max_length=255)
    marks = models.FloatField()
    name = models.ForeignKey(Addclass,on_delete=models.CASCADE)

class Institute(models.Model):
    InstituteName = models.CharField(max_length=255)
    TargetLine = models.CharField(max_length=255)
    InstituteLogo = models.FileField(upload_to='images/')
    Phone = models.IntegerField()
    Website = models.CharField(max_length=255)
    InstituteAddress = models.CharField(max_length=255)
    country = CountryField()

class Student(models.Model):
    StudentName = models.CharField(max_length=255)
    RegistrtionNo = models.IntegerField()
    Class = models.ForeignKey(Addclass,on_delete=models.CASCADE)
    Picture = models.FileField(upload_to='profile/')
    AdmissionDate = models.DateField()
    DiscountFee = models.IntegerField()
    MobileNo = models.IntegerField()

    def __str__(self):
        return self.StudentName

class Employee(models.Model):
    CHOICESTYPE = (
    ('----Employee Type-------','----Employee Type-------'),
    ('Teaching','Teaching'),
    ('Non Teaching','Non Teaching')
    )
    EmployeeName = models.CharField(max_length=255)
    Picture = models.FileField(upload_to='employees/',blank=True)
    JoiningDate = models.DateField()
    EmployeeType = models.CharField(max_length=255,choices= CHOICESTYPE,default='----Employee Type-------')
    MobileNo = models.IntegerField()
    MonthlySalary = models.FloatField()

class AccountIncome(models.Model):
    Month = models.DateField()
    IncomeDescription = models.CharField(max_length=255)
    IncomeAmount = models.IntegerField()

class AccountExpense(models.Model):
    Month = models.DateField()
    ExpenseDescription = models.CharField(max_length=255)
    ExpenseAmount = models.IntegerField()

class Account(models.Model):
    Month = models.DateField()
    IncomeDescription = models.CharField(max_length=255, default='no description')
    IncomeAmount = models.IntegerField(default=0)
    ExpenseDescription = models.CharField(max_length=255, default='no description')
    ExpenseAmount = models.IntegerField(default=0)

class StudentAttendance(models.Model):
    attendance_choices = (
    ('present', 'P'),
    ('absent', 'A'),
    ('leave', 'L'),
)
    Date = models.DateField()
    Class = models.ForeignKey(Addclass,on_delete=models.CASCADE)
    StudentName = models.ForeignKey(Student,on_delete=models.CASCADE)
    Attendance = models.CharField(max_length=20,choices=attendance_choices,)

    # def __str__(self):
    #     return self.StudentName
class Attendance(models.Model):
    Date = models.DateField()
    Class = models.CharField(max_length=40)
    StudentName = models.CharField(max_length=255)
    Status = models.CharField(max_length=20)

class EmployeeAttendance(models.Model):
    Date = models.DateField()
    EmpId = models.IntegerField()
    EmployeeName = models.CharField(max_length=255)
    EmployeeType = models.CharField(max_length=200)
    Status = models.CharField(max_length=20)

    def __str__(self):
        return self.EmployeeName
