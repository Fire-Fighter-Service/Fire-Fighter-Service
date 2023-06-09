from django.contrib import admin
from django.urls import path
from firereport.views import *
from django.conf import settings
from django.conf.urls.static import static
#all member 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('reporting2', reporting, name='reporting'),
    path('viewStatus', viewStatus, name='viewStatus'),
    path('viewStatusDetails/<int:pid>', viewStatusDetails, name='viewStatusDetails'),
    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='Dashboard'),
    path('addTeam', addTeam, name='addteam'),
    path('manageTeam', manageTeam, name='manageteam'),
    path('edit_Team/<int:pid>', editTeam, name='editteam'),
    path('deleteTeam/<int:pid>', deleteTeam, name='deleteteam'),
    path('newRequest', newRequest, name='newRequest'),
    path('assignRequest', assignRequest, name='assignRequest'),
    
    path('teamontheway', teamontheway, name='teamontheway'),
    path('workinprogress', workinprogress, name='workinprogress'),
    path('completeRequest', completeRequest, name='completeRequest'),
    path('allRequest', allRequest, name='allRequest'),
    path('deleteRequest/<int:pid>', deleteRequest, name='deleteRequest'),
    path('viewRequestDetails/<int:pid>', viewRequestDetails, name='viewRequestDetails'),
    path('dateReport', dateReport, name='dateReport'),
    path('search', search, name='search'),
    path('changePassword', changePassword, name='changePassword'),
    
    path('logout/', Logout, name='logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

