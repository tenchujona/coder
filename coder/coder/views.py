from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from app1.models import Data_Users
from django.contrib.auth.models import User

from coder.settings import BASE_DIR

def home(request):
    #return HttpResponse(BASE_DIR/"TEMPLATES")
    InsertId= (User.objects.last()).id
    context = {"id": InsertId}
    return render(request, 'TEMPLATES/index.html', context=context)