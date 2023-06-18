from rest_framework import serializers

from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
    
    extra_kwargs = {
            "created_at": {"read_only": True},
        }

