from .models import Student
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html', {'student_lists': Student.objects.all(),'webpage':'http://127.0.0.1:8000/'})
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html', {'student_lists': Student.objects.all(),'webpage':'http://127.0.0.1:8000/'})
def articles(request):
    return render(request, 'articles.html')