from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import View,TemplateView


class home(TemplateView):
    template_name = 'main.html'

class ad(TemplateView):
    template_name = 'login.html'

class donor(TemplateView):
    template_name = 'Donors/register.html'

class orgs(TemplateView):
    template_name = 'main.html'

class visit(TemplateView):
    template_name = 'main.html'


def login(requst):
    if requst.POST.get('uname')=='admin':
        if requst.POST.get('password')=='Farooq@123':
            return render(requst,'admin/admin_home.html')
        else:
            return render(requst,'login.html',{"user":"Wrong User Name Provided"})
    else:
        return render(requst,'login.html',{"pass":"Wrong Password Provided"})
