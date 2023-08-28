from django.urls import path
from . import views
urlpatterns=[
    path('list_job', views.list_job,name='list_job'),    
    path('<int:id>', views.jobdetail,name='jobdetail'),
    path('signup',views.register,name='user_register'),
    path('',views.user_login,name="user_login"),
    path('profile',views.user_profile,name='profile'),
    path('logout',views.user_logout,name='user_logout'),
    path('form',views.user_form,name='user_form'),
]
