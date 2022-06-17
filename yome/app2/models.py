from django.db import models

# Create your models here.


    

#creating a table hotel
class Hotel(models.Model):
    room = models.CharField(max_length=222)
    amount = models.CharField
    name= models.CharField(max_length=222)
    email= models.EmailField()
    occupation= models.CharField(max_length=222)
    noofnight=models.CharField (_max_length=20)
    startdate=models.CharField
    enddate=models.CharField
    time = models.DateTimeField(auto_now_add=True)

#returning the name 
    def __str__(self):
        return self.name
    
    