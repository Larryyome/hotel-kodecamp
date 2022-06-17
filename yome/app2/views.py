import email
from unicodedata import name
from django.shortcuts import render

from app2.form import Formss
from .models import Hotel

# Create your views here.

#taking the data and saving it
def signup(request):
    if request.post:
         form=Formss(request.POST)
         if form.is_valid():
             form.save
         return redirect(signup)
    return render(request, 'mov/index.html', {'ff' : form} )
    