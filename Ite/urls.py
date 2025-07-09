import os

from django.urls import path
from myite import settings
from . import views
from django.views.static import serve

from .views import delete_comment


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('secret/', views.secret_page, name='secret'),
    path('register/', views.register, name='register'),
    path('post_comment/', views.post_comment, name='post_comment'),
    path('sitemap.xml', views.sitemap),
    path('comments/delete/<int:comment_id>/', delete_comment, name='delete_comment'),
]
