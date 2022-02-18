# REST API using class based generic viewSets and mixins
# csrf is also exempted in these class based views and view sets by default
# generic viewSets don't have any functionalities but we can add them using mixins
# TO DO SO we just need to convert APIView to generics.APIView with mixins and everything else is same


"""
using viewSet we don't need to create two separate functions for getting id or pk
we need only one class (ArticleViewSet) instead of two (ArticleList and ArticleDetails)
ViewSet will automatically look for the pk when needed
"""
from rest_framework import viewsets, mixins

from .models import Article
from .serializers import ArticleModelSerializer


# Create your views here.
# MODEL VIEW SET
# no need to even inherit mixins because we already have CRUD operations in modelViewSet
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


'''
# GENERIC VIEW SET
# no need to create functions for generic view set but we need to create in genericAPIView
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                     mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
'''
