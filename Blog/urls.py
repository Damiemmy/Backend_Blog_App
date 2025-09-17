from django.urls import path
from . import views

urlpatterns=[
    path('MYBlogs/',views.MYBlogs,name='MYBlogs'),
    path('Blogpage/<slug:slug>/',views.Blogpage,name='Blogpage'),
    path('Getcategory/',views.Getcategory,name='Getcategory'),
    path('GetCurrentUser/',views.GetCurrentUser,name='GetCurrentUser'),
    path("register/", views.register_user, name="register"),

]