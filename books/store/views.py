from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import UpdateModelMixin

from django.shortcuts import render

from .serializers import BookSerializer, UserBookRelationSerializer
from .models import Book, UserBookRelation
from .permissions import IsOwnerOrStaffOrReadOnly


class BookViewSet(ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	permission_classes = [IsOwnerOrStaffOrReadOnly]
	filter_fields = ['price']
	search_fields = ['name', 'author_name']
	ordering_fields = ['price', 'author_name']

	def perform_create(self, serializer):
		serializer.validated_data['owner'] = self.request.user
		serializer.save()


class UserBookRelationView(UpdateModelMixin, GenericViewSet):
	permission_classes = [IsAuthenticated]
	queryset = UserBookRelation.objects.all()
	serializer_class = UserBookRelationSerializer
	lookup_field = 'book'

	def get_object(self):
		obj, _ = UserBookRelation.objects.get_or_create(user=self.request.user,
														book_id=self.kwargs['book'])
		return obj


def auth(request):
	return render(request, 'oauth.html')
