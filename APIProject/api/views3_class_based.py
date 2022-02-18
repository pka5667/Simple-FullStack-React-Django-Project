# REST API using class based APIView
# TO DO SO we just need to convert function to class and everything else is same

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView

from .models import Article
from .serializers import ArticleModelSerializer


# Create your views here.
class ArticleList(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    def get_object(self, id):
        try:
            return Article.objects.get(pk=id)
        except:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, id):
        serializer = ArticleModelSerializer(self.get_object(id))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        serializer = ArticleModelSerializer(self.get_object(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        serializer = ArticleModelSerializer(self.get_object(id), data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        self.get_object(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
