from curses import REPORT_MOUSE_POSITION
from django.forms import ModelForm
from django import Forms
from .models import Hotel

class Formss(Modelsform):
    room = Forms.NumberInput() 
    amount =Forms.NumberInput()
    name = Forms.NumberInput()  
    email =Forms.TextInput() 
    occupation =Forms.TextInput()
    noofnight =Forms.NumberInput() 
    startdate = Forms.NumberInput() 
    enddate  =Forms.NumberInput() 
    class Meta:
        modell=Hotel 
        fieldd=['room', 'amount', 'name', 'email', 'occopation', 'noofnight', 'startdate', 'enddate']
    
    
    