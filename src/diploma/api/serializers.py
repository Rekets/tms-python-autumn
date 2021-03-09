from django.urls import reverse

from home.models import Articles
from rest_framework import serializers

from user_profile.models import Profile


class ArticlesSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields = ["id", "title", "content", "author", "link", 'avatar']

    def get_link(self, obj):
        uri = reverse("get-articles", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated and instance.author_id == user.id:
            return super(ArticlesSerializer, self).update(instance,
                                                          validated_data)
        raise Exception("No credentials")


class ProfileSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ["user", "country", "height", "weight", "birth_date",
                  'avatar', 'link', 'user']

    def get_link(self, obj):
        uri = reverse("get-articles", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated and instance.author_id == user.id:
            return super(ProfileSerializer, self).update(instance,
                                                         validated_data)
        raise Exception("No credentials")
