"""Stjoseph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import views

from .views import StudentReg, Studentlist ,Studentdetail , StudentUpdate, StudentDelete 

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    # path('studentlist', views.studentlist, name = "studentlist"),
    path('studentlist', views.studentlist, name='studentlist'),
    path('studentdetail/<pk>', views.studentdetail, name='studentdetail'),
   path('studentreg', views.studentreg, name='studentreg'),
   path('studentupdate/<int:id>', views.studentupdate, name = 'studentupdate'),
   path('studentdelete/<int:id>', views.studentdelete, name = 'studentdelete'),

#    CBV

   path('studentreg1', StudentReg.as_view(), name = 'studentreg'),
   path('<pk>/studentdetail1/', Studentdetail.as_view(), name = 'studentdetail'),
   path('',Studentlist.as_view(), name = 'studentlist'),
   path('<pk>/studentupdate1/',StudentUpdate.as_view(),name = 'studentupdate'),
   path('<pk>/studentdelete1/', StudentDelete.as_view(), name = 'studentdelete'),

    
]
