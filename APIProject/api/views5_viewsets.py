# REST API using class based viewSets
# viewSet is nothing but just a simple way to implement rest api
# Using ViewSet you don't have to create separate views for getting a list of objects and detail of one object.
# ViewSet will handle for you in a consistent way both list and detail.
# https://stackoverflow.com/questions/32589087/difference-between-views-and-viewsets
# TO DO SO we just need to convert generics.APIView to viewSet and change the function names


"""
using viewSet we don't need to create two separate functions for getting id or pk
we need only one class (ArticleViewSet) instead of two (ArticleList and ArticleDetails)
ViewSet will automatically look for the pk when needed
"""
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Article
from .serializers import ArticleModelSerializer


# Create your views here.
# viewSets have functions like-> list, retrieve, create, destroy // names are same as mixins
class ArticleViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query_set = Article.objects.all()
        article = get_object_or_404(query_set, pk=pk)
        serializer = ArticleModelSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        article = Article.objects.get(pk=pk)
        serializer = ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
