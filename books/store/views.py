from rest_framework.viewsets import ModelViewSet

from .serializers import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
