from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request --> response 
def say_hello(request):
    return render(request,'hello.html')

def email_gen(request):
    #print("This is an email generator")
    return render(request,"""<html><script>/Users/macuser/django/trydjango/playground/ChatGPT_Email.py;</script></html>""")

