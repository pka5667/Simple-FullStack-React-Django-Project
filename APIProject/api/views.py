"""
using viewSet we don't need to create two separate functions for getting id or pk
we need only one class (ArticleViewSet) instead of two (ArticleList and ArticleDetails)
ViewSet will automatically look for the pk when needed
"""
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated  # we can specify this in settings by default

from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleModelSerializer, UserSerializer


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


