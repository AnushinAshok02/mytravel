
from django.urls import path

from inmakesapp import views

urlpatterns = [

    path('',views.demo,name='demo'),

    # path('add/',views.addition,name='addition'),
    # path('contact/',views.contact,name='contact')
]