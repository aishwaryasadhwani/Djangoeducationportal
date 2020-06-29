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
