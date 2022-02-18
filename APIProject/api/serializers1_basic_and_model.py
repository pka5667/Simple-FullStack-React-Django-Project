from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=400)

    def create(self, validated_data):
        return Article.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.desctiption)
        return super().update(instance, validated_data)


# create and update methods are already available in this
class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']



# >>> from api.models import Article
# >>> from api.serializers import ArticleSerializer
# >>> from rest_framework.renderers import JSONRenderer
# >>> from rest_framework.parsers import JSONParser

# create an object and then deserialize it
# >>> a = Article(title="ti", description="di") 
# >>> a.save()
# >>> serializer = ArticleSerializer(a)
# >>> serializer.data
# {'title': 'ti', 'description': 'di'}

# serialize the json data 
# >>> json = JSONRenderer().render(serializer.data) 
# >>> json
# b'{"title":"ti","description":"di"}'
# >>> import io
# >>> stream = io.BytesIO(json)
# >>> stream
# <_io.BytesIO object at 0x000001536DBF70E0>
# >>> data = JSONParser().parse(stream)
# >>> data
# {'title': 'ti', 'description': 'di'}
# >>> serializer = ArticleSerializer(data=data) 
# >>> serializer.is_valid()
# True
# >>> serializer.validated_data 
# OrderedDict([('title', 'ti'), ('description', 'di')])


# to find representation
# print(repr(ArticleModelSerializer()))
