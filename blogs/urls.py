from django.urls import path
from . import views
from . import api_views


urlpatterns = [
  path('<int:category_id>/', views.posts_by_category, name = 'posts_by_category'),
  path('blogs/', api_views.blog_list_api, name='api_blogs'),
  path('comments/', api_views.comment_list_api, name='api_comments'),
]