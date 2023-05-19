from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from reservation.views import *
urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('customer',customer_reg.as_view()),
    path('buslist',Bus_listview.as_view()),
    path('reservation',Reservation_view.as_view()),

    
]