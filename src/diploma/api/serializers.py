from django.urls import reverse

from home.models import Articles
from rest_framework import serializers


class ArticlesSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields = ["id", "title", "content", "author", "link", "image"]

    def get_link(self, obj):
        uri = reverse("articles-detail", kwargs={"pk": obj.pk})
        return self.context["request"].build_absolute_uri(uri)

    def update(self, instance, validated_data):
        request = self.context.get("request")
        user = request.user
        if user.is_authenticated and instance.author_id == user.id:
            return super(ArticleSerializer, self).update(instance, validated_data)
        raise Exception("No credentials")