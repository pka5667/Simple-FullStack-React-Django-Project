from .views1_function_based import article_list, article_details
from django.urls import path

urlpatterns = [
    path('articles', article_list, name="article_list"),
    path('articles/<int:pk>', article_details, name="article_details"),
]
