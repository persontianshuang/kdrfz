from rest_framework import serializers
from kindle.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ('content','book_from')
