from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app1.models import Data_Users
from django.contrib.auth.models import User

from coder.settings import BASE_DIR

def home(request):
    return render(request, 'index.html')