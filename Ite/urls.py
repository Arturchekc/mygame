import os

from django.urls import path
from myite import settings
from . import views
from django.views.static import serve

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('secret/', views.secret_page, name='secret'),
    path('register/', views.register, name='register'),
    path('post_comment/', views.post_comment, name='post_comment'),
    path('sitemap.xml', views.sitemap),

]