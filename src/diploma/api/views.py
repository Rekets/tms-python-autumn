from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from home.models import Articles
from api.serializers import ArticlesSerializer, ProfileSerializer
from user_profile.models import Profile


class ArticlesListAPIView(ListCreateAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ArticlesDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer


class ProfileListAPIView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
