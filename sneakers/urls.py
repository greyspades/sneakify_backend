from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('boots/',views.boots,name='boots'),
    path('',views.user,name='user'),
    path('get_sneakers/',views.get_sneakers,name='get_sneakers')
]