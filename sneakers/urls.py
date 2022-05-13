from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('boots/',views.boots,name='boots'),
    # path('',views.user,name='user'),
    path('get_sneakers/',views.get_sneakers,name='get_sneakers'),
    path('add_user/',views.add_user,name='add_user'),
    path('login/',views.login,name='login'),
    path('sneaker_brand/<slug:brand>/<int:page>',views.sneaker_brand,name='sneaker_brand')
]