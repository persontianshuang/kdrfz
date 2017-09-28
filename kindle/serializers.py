from rest_framework import serializers
from kindle.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        # 'book_from'
        # fields = ('content',)  即使只有一个后面的逗号不能少
        fields = ('content',)
