from django.shortcuts import render
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication, )    # 어떤 인증방식으로 인증해야할지 설정하는 옵션
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)    # 인증을 해야만 볼 수 있는 옵션
    
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


