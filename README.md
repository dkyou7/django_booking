[toc]

# Rest API 구축하기

- 스마트폰 개발용 API 만들기

### 1. Project init script

```
pip install django
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

### 3. 모델 만들기

- 필요한 데이터를 모델로 만들어보자

