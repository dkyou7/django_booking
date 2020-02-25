from django.db import models
from django.conf import settings

# Create your models here.
class Booking(models.Model):
    # related_name : 불러올 때 어떻게 불러올까?
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