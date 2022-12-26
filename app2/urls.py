from django.urls import path
from app2.views import *
app_name='something 2'
urlpatterns=[
    path('sujitha/',sujitha,name='sujitha'),
    path('meena/',meena,name='meena')

]