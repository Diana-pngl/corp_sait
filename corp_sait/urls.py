from corp_sait import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.abra_k, name='glavnaya'),
    path('accounts/login/', views.abra_login, name ='login'),
    path('accounts_udalit/', views.abra_k_udalit, name ='ne_login'),
    path('form_E/', views.abra_E, name ='abra_E'),
    path('events/', views.abra_Events, name ='Events'),
    path('event/<int:chislo>/', views.abra_Event, name ='Event'),
    path('employees/', views.abra_Employees, name ='employees'),
    path('employee/<int:chislo>/', views.abra_Employee, name ='employee'),
    path('teams/', views.abra_Teams, name ='teams'),
    path('fdck/', views.abra_Fdck, name ='fdck'),
]
