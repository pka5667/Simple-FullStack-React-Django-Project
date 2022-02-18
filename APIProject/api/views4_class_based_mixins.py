# REST API using class based APIView -> generic APIView
# in this class based view all the code for functions for get put post delete are already written
# and we don't need to rewrite them
# TO DO SO we just need to convert APIView to generics.APIView with mixins and everything else is same

from rest_framework import generics, mixins

from .models import Article
from .serializers import ArticleModelSerializer


# Create your views here.
# ListModelMixin -> for getting data from queryset and serializer_class
# CreateModelMixin -> for creating object using serializer_class
class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# mixins for retrieving data, update data and delete object respectively
class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
    lookup_field = "id"

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def patch(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
