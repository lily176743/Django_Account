from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# welcome
def welcome(request):
    template = loader.get_template('page/welcome.html')
    return HttpResponse(template.render())

# login
def login(request):
    template = loader.get_template('account/login.html')
    return HttpResponse(template.render())

# signin
def signup(request):
    template = loader.get_template('account/signup.html')
    return HttpResponse(template.render())
