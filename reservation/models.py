from django.db import models
from django.utils import timezone
from datetime import datetime

# 1. Model for customer

class Customer_details(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True,null=True)
    password=models.CharField(max_length=30)
    def __str__(self):
      return self.name

    @property
    def is_staff(self):
        return self.name

#2. Model for Bus List
class Bus_list(models.Model):
    
    bnumber=models.PositiveIntegerField()
    bname=models.CharField(max_length=30)
    bus_from=models.CharField(max_length=30)
    bus_to=models.CharField(max_length=30)

    distance_category = (
        ('short','short'),
        ('long','long'),
        ('medium','medium'))
    distance_type = models.CharField(choices=distance_category, default="short", max_length=20)
    price=models.FloatField(blank=True,null=True)   
    total_seats=models.PositiveIntegerField(null=True)
    available_seats=models.PositiveIntegerField(null=True)   



    # def __str__(self):
    #     return self.room_type
    class Meta:
        unique_together=("distance_type",)

#3. Model for Bus reservation        

class Reservations(models.Model):
    
    busid=models.ForeignKey(Bus_list,on_delete=models.CASCADE)
    custid=models.ForeignKey(Customer_details, on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)
    rdate=models.DateTimeField(default=timezone.now)
   

    no_seats=models.PositiveIntegerField(null=True)
    total_amount = models.FloatField(blank=True,null=True)
    booking_status = (
        ('BOOKED','BOOKED'),
        ('CANCELLD','CANCELLD'))
    booking_sts = models.CharField(choices=booking_status, default="BOOKED", max_length=20)
  
    
    class Meta:
        unique_together=("custid","busid")
    @property
    def is_staff(self):
        return self.busid 
    def get_total(self):
      bus=self.busid

      total_amount=0
      total_amount+=bus.price*self.no_seats
      print("total price:......................",total_amount)
      return total_amount



#4. Model for Price

# class Bustype(models.Model):
#   busid=models.ForeignKey(Bus_list,on_delete=models.CASCADE)
#   distance_category = (
#         ('short','short'),
#         ('long','long'),
#         ('medium','medium'))
#   distance_type = models.CharField(choices=distance_category, default="short", max_length=20)
#   price=models.FloatField(blank=True,null=True)   
#   total_seats=models.PositiveIntegerField()
#   available_seats=models.PositiveIntegerField()     
#   def __str__(self):
#         return self.room_type
#   class Meta:
#         unique_together=("room_type",)