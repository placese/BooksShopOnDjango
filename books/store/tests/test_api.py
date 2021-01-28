from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
	def setUp(self):
		Book.objects.create(name='Test book 1', price=1000.00)
		Book.objects.create(name='Test book 2', price=1250.00)

	def test_get(self):
		book_1 = Book.objects.get(name='Test book 1')
		book_2 = Book.objects.get(name='Test book 2')

		url = reverse('book-list')
		response = self.client.get(url)
		serializer_data = BookSerializer([book_1, book_2], many=True).data

		self.assertEqual(status.HTTP_200_OK, response.status_code)
		self.assertEqual(serializer_data, response.data)
