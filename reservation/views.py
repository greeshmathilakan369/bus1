from django.shortcuts import render

# Create your views here.
from reservation.models import *
from .serializers import customer_serializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from . serializers import *
import email

# Create your views here.
class customer_reg(APIView):
    serializer_class=customer_serializer
    def get(self,request,*args,**kwargs):
        user4=Customer_details.objects.all()
        serializer=customer_serializer(user4,many=1)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        print("serializer class..........",serializer)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'customer successfully registered!',
                'user': serializer.data
            }
            return Response(response, status=status_code)  

#2 view for bus list
class Bus_listview(APIView):
    serializer_class=buslist_seriializer
    def get(self,request,*args,**kwargs):
        user1=Bus_list.objects.all()
        serializer=buslist_seriializer(user1,many=1)
        return Response(serializer.data)            
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'Bus successfully registered!',
                'user': serializer.data
            }
            return Response(response, status=status_code)  

#3 view for reservation
class Reservation_view(APIView):
    serializer_class=reservation_serializer
    

    # bus_price=Bus_list.objects.
    

    def get(self,request,*args,**kwargs):
        user2=Reservations.objects.all()
        serializer=reservation_serializer(user2,many=1)
        return Response(serializer.data)
    def post(self,request):
        


        serializer=reservation_serializer(data=request.data)
    
        busid=request.data['busid']
        
        bus=Bus_list.objects.get(id=busid)
        print("price........",bus.price)
        
        # rdate = request.data["total_amount"] 
        # print("total_amount........................",total_amount)
        # total_amount = request.data["total_amount"]    
        # print("total amount:",total_amount)
        # print("bus price:",bus.buslist_id.price)



        # valid=serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            print("hello..............................")
            res_object=serializer.save()
            res_object.total_amount=res_object.get_total()
            print("res obj.........................",res_object)
            res_object.save()
            status_code=status.HTTP_201_CREATED
            response={
                'success':True,
                'statusCode':status_code,
                'message':'Bus Reserved sucessfully!',
                'user':serializer.data
            }
            return Response(response,status=status_code)