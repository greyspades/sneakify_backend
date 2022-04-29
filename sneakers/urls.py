from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('',views.boots,name='boots'),
    path('<string:id>/',views.user,name='user')
]