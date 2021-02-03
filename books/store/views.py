from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import render

from .serializers import BookSerializer
from .models import Book


class BookViewSet(ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	permission_classes = [IsAuthenticatedOrReadOnly]
	filter_fields = ['price']
	search_fields = ['name', 'author_name']
	ordering_fields = ['price', 'author_name']


def auth(request):
	return render(request, 'oauth.html')
