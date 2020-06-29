"""portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from portalapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('login/', views.login),
    path('accounts/',include('django.contrib.auth.urls')),
    path('addclass/',views.Addclasses),
    path('all/',views.Allclasses),
    path('update/<int:pk>',views.UpdateClasses.as_view()),
    path('delete/<int:pk>',views.Deleteclasses),
    path('viewclasses/',views.ViewClasses),
    path('addsubject/',views.AddSubjects),
    path('viewsubject/',views.ViewSubjects),
    path('createinfo/',views.AddInstitute),
    path('viewinfo/',views.ViewInstitute),
    path('createstudent/',views.CreateStudent),
    path('updatestudent/<int:pk>',views.UpdateStudents.as_view()),
    path('deletestudent/<int:pk>',views.DeleteStudents),
    path('viewstudent/',views.ViewStudents,name='viewstudent'),
    path('view/<int:pk>',views.ViewOne),
    path('searchstudent/<int:pk>',views.SearchStudent),
    path('admission/',views.Admission),
    path('print/<int:pk>',views.PrintLetter),
    path('createemp/',views.CreateEmp),
    path('allemp/',views.AllEmp,name='allemp'),
    path('searchemp/<int:pk>',views.SearchEmp),
    path('updateemp/<int:pk>',views.UpdateEmployee.as_view()),
    path('deleteemp/<int:pk>',views.DeleteEmployee),
    path('filter/<int:pk>',views.Filter),
    # path('create/',views.Create.as_view())
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
