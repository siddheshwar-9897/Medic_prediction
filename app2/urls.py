from django.urls import path,include
from . import views

urlpatterns=[
    path('register/',views.register,name='register'),
     path('login_view',views.login_view,name='login_view'),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('form/',views.form,name='form'),
    path('result',views.result,name='result'),
    path('logout1/',views.logout1,name='logout1')

 
]
# urlpatterns=[
#        path('',views.index2,name='index2')
# ]