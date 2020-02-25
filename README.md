[toc]

# Rest API 구축하기

## 스마트폰 개발용 API 만들기(MTV 구조)

### 1. Project init script

```
pip install django==2.2
django-admin startproject config .
python manage.py migrate
python manage.py createsuperuser
```

### 2. 앱 만들기

> python manage.py startapp booking

```python
INSTALLED_APPS = [
    'booking',
]
```

## 가. Model

### 3. 모델 만들기

- 필요한 데이터를 모델로 만들어보자

`booking/models.py`

```python
from django.db import models
from django.conf import settings

# Create your models here.
class Booking(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT,related_name='bookings')
    date_from = models.DateField()
    date_to = models.DateField(null=True,blank=True)
    room = models.CharField(max_length=100)
    note = models.TextField()

    # auto_now_add : create 시 적용하는 것이 좋음. 최초 생성 일자
    created = models.DateTimeField(auto_now_add=True)
    # auto_now : update 시 적용하는 것이 좋음. 최종 수정 일자
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subscriber.username + " " + self.room

    class Meta:
        # 예약시간의 내림차순으로 설정
        # 객체들을 어떤 기준으로 정렬할 지 설정하는 옵션
        ordering = ['-date_from']
```

- 모델 작성 후에는 기본적으로 DB에 적용시키기 위해 migrate를 해줘야 한다.

> python manage.py makemigrations booking
>
> python manage.py migrate booking

### 4. 관리자 페이지 등록

- 만든 모델의 관리를 위해 관리자 페이지를 등록해본다.

```python
from django.contrib import admin
from .models import Booking


# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id','subscriber','room','date_from','date_to','created','updated']
    list_editable = ['room','date_from','date_to']
    raw_id_fields = ['subscriber']

admin.site.register(Booking,BookingAdmin)
```

### 5. API 환경 만들기

> pip install djangorestframework==3.9.4

```python
INSTALLED_APPS = [
    'rest_framework',
]
```

### 6. Serializer 클래스 구현

- 요청한 모델을 API 보여줄 때 사용하는 클래스
- GET 방식의 모델에 대한 데이터를 요청 시 Serializer를 활용해 데이터 보여준다.

```python
from .models import Booking
from rest_framework import serializers

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
```

- 직렬화를 쉽게 만들어 준다.

## 나. Template

- 여기서는 없다.

## 다. View

### 7. 뷰 만들기

- 데이터를 주고받을 수 있는 뷰(Controller)를 만들어보자

```python
from django.shortcuts import render
from rest_framework import generics

from .models import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
```

### 8. URL 연결하기

`booking/urls.py`

```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns=[
    path('booking/',BookingList.as_view()),
    path('booking/<int:pk>/',BookingDetail.as_view()),
]
```

`config/urls.py`

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
]
```

### 9. API 문서 만들기

### 10. 인증 추가하기

### 11. 문서에 Token 기능 사용하기

### 12. 추가 권한 설정하기

