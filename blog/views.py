from rest_framework import filters, viewsets

from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    http_method_names = ["get", "post", "delete", "patch","put"]
    serializer_class = BlogSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["published"]
    search_fields = ["title", "body"]
    ordering_fields = [
        "created_at",
    ]

