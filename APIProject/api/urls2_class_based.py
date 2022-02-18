from .views4_class_based_mixins import ArticleList, ArticleDetails
from django.urls import path

urlpatterns = [
    path('articles', ArticleList.as_view(), name="article_list"),
    path('articles/<int:id>', ArticleDetails.as_view(), name="article_details"),
]
