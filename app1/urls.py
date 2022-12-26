from django.urls import path
from app1.views import *
app_name='something 1'
urlpatterns=[
    path('dinesh/',dinesh,name='dinesh'),
    path('praveen/',praveen,name='praveen'),
]