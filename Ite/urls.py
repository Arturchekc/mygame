
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('secret/', views.secret_page, name='secret'),
    path('register/', views.register, name='register'),
    path('post_comment/', views.post_comment, name='post_comment'),
]