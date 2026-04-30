# api/urls.py
from django.urls import path
from blogs import api_views

urlpatterns = [
    path('blogs/', api_views.blog_list_api),
    path('comments/', api_views.comment_list_api),
]