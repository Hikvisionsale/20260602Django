#from django.shortcuts import render
#
# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django World! Vincent")

def register(request):
    return HttpResponse("This is the <bold>Registration</bold> page.")

def login(request):
    return HttpResponse("This is the <bold>Login</bold> page.")

def forgot_password(request):
    return HttpResponse("This is the <bold>Forgot Password</bold> page.")