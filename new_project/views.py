from django.http import HttpResponse
from django.shortcuts import render
from . import views

def home(request):
	return render(request,'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	l_s = len(user_text.split())
	reversed_text = user_text[::-1] 
	return render(request,'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'ls':l_s})