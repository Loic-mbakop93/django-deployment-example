from django.conf.urls import url
from django.urls import path
from basic_app import views

#TEMPLATE TAGGING
app_name ='base_app' #django recognises this
urlpatterns =[
 path('relative/', views.relative, name ='relative'),
 path('other/',views.other, name ='other'),
]
