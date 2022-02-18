# REST API with simple view functions

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Article
from .serializers import ArticleModelSerializer


# Create your views here.
@csrf_exempt
def article_list(request):
    # get all articles
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleModelSerializer(article)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    if request.method == 'PATCH':
        data = JSONParser().parse(request)
        serializer = ArticleModelSerializer(article, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    if request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
