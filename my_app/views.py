from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from . import forms

# Create your views here.

def home(request):
   student_list = Student.objects.order_by('name')
   diction = {'Student':student_list}
   return render(request,'my_app/index.html',context=diction)

def form(request):
   new_form = forms.studentForm()
   if request.method == "POST":
          new_form = forms.studentForm(request.POST)
          
          if new_form.is_valid():
                 new_form.save(commit=True)
   
   diction = {'test_form':new_form}
   return render(request,'my_app/form.html',context=diction)