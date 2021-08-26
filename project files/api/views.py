# Create your views here.
from django.shortcuts import render
from website.models import Student
def api(request):
    return render(request, 'api.html', {'student_lists': Student.objects.all()})
