from django.http import JsonResponse

from rest_framework.generics import ListAPIView

from home.models import Articles
from api.serializers import ArticlesSerializer


def test_api(request):
    return JsonResponse(
        {
            'date': '2020-03-08',
            'group': 'z38'
        }
    )


class ArticleListAPIView(ListAPIView):
    model = Articles
    serializer_class = ArticlesSerializer
