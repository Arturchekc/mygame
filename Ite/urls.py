import os
from django.urls import path
from django.views.generic import TemplateView
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
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]