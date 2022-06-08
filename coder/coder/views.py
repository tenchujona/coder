from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from coder.settings import BASE_DIR

def home(request):
    #return HttpResponse(BASE_DIR/"TEMPLATES")
    return render(request, 'TEMPLATES/index.html')