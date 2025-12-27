from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.utils.dateparse import parse_date
from corp_sait import form
from corp_sait import models

@login_required
def abra_k(request):
    otvet = render(request, 'k.html')
    return otvet

def abra_login(request):
    if request.method == "GET":
        otvet = render(request,'k_login.html')
        return otvet
    else:
        name = request.POST['name']
        parol = request.POST['password']
        proshol = authenticate(request, username=name, password=parol)
        if proshol != None:
            login(request, proshol)
            k_otvet = redirect('glavnaya')
            return k_otvet
        else :
            otvet = redirect('login')
            return otvet
        
def abra_k_udalit(request):
    logout(request)
    otvet = redirect('login')
    return otvet

def abra_E(request):
    if request.method == 'GET':
        forma_dce = form.Forma_dlia_cozdania_e()
        otvet = render(request,'form_E.html',{'forma':forma_dce})
        return otvet
    else:
        forma_dce = form.Forma_dlia_cozdania_e(request.POST)
        if forma_dce.is_valid() == True:
            forma_dce.save()
            forma_dce = form.Forma_dlia_cozdania_e()
            otvet = render(request,'form_E.html',{'forma':forma_dce})
            return otvet
        else:
            otvet = render(request,'form_E.html',{'forma':forma_dce})
            return otvet  
        
def abra_Events(request):
    if request.GET == {}:
        vse = models.Event.objects.all()
        otvet = render(request,'event_list.html',{'vse':vse})
        return otvet
    else:
        tcv = request.GET['date']
        tcv = parse_date(tcv)
        f_tcv = models.Event.objects.filter(date=tcv)
        otvet = render(request,'event_list.html',{'vse':f_tcv})
        return otvet
        

def abra_Event(request,chislo):
    event = models.Event.objects.get(id=chislo)
    otvet = render(request,'event.html',{'event':event})
    return otvet

def abra_Employees(request):
    vse = models.Employee.objects.all()
    otvet = render(request,'Employees.html',{'vse':vse})
    return otvet     

def abra_Employee(request,chislo):
    employee = models.Employee.objects.get(id=chislo)
    otvet = render(request,'employee.html',{'employee':employee})
    return otvet

def abra_Teams(request):
    vse = models.Team.objects.all()
    otvet = render(request,'Teams.html',{'vse':vse})
    return otvet

def abra_Fdck(request):
    if request.method == 'GET':
        forma_fdck = form.Forma_dlia_coedinenia_k()
        otvet = render(request,'form_E.html',{'forma':forma_fdck})
        return otvet
    else:
        forma_fdck = form.Forma_dlia_coedinenia_k(request.POST)
        if forma_fdck.is_valid() == True:
            team = forma_fdck.cleaned_data['team']
            event = forma_fdck.cleaned_data['event']
            team.event = event
            team.save()
            otvet = redirect('Events')
            return otvet
        else:
            otvet = render(request,'form_E.html',{'forma':forma_fdck})
            return otvet            