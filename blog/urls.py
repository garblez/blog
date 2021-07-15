from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    path('articles/', views.ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', views.ArticleDetail.as_view(), name='article-detail'),
    path('comments/', views.CommentList().as_view(), name='comment-list'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)