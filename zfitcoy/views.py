from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zfitcoy.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from fitcoy.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User

def HOME(request):

    return render(request, 'index.html')

def ABOUT(request):

    return render(request, 'about.html')

def SERVICES(request):
    ser = Services.objects.all()
    d = {"ser":ser}
    return render(request, 'service.html',d)

def BLOGS(request):
    pop = Blogs.objects.all().order_by('id')
    p = pop[:3]
    ca = Blog_category.objects.all()
    blog = Blogs.objects.all()
    d = {"blog":blog,"ca":ca,"p":p}
    return render(request, 'blogs.html',d)

def CONTACT(request):

    return render(request, 'contact.html')

def TEAMS(request):
    te = Team.objects.all()
    d = {"te":te}
    return render(request, 'team.html',d)