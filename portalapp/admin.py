from django.contrib import admin
from portalapp.models import Addclass,Subjects,Institute,Student,Employee,AccountIncome,AccountExpense,Account,StudentAttendance,Attendance,EmployeeAttendance,Fee,FeeSubmission
# Register your models here.
admin.site.register(Addclass)
admin.site.register(Subjects)
admin.site.register(Institute)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(AccountIncome)
admin.site.register(AccountExpense)
admin.site.register(Account)
admin.site.register(StudentAttendance)
admin.site.register(EmployeeAttendance)
admin.site.register(Attendance)
admin.site.register(Fee)
admin.site.register(FeeSubmission)
