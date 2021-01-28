from django.test import TestCase

from store.serializers import BookSerializer
from store.models import Book


class BookSerializerTestCase(TestCase):
	def setUp(self):
		Book.objects.create(name='Test book 1', price=1000.00)
		Book.objects.create(name='Test book 2', price=1250.00)

	def test_ok(self):
		book_1 = Book.objects.get(name='Test book 1')
		book_2 = Book.objects.get(name='Test book 2')
		data = BookSerializer([book_1, book_2], many=True).data
		expected_data = [
		{
			'id': book_1.id,
			'name': 'Test book 1',
			'price': '1000.00'
		},
		{
			'id': book_2.id,
			'name': 'Test book 2',
			'price': '1250.00'
		}
		]

		self.assertEqual(data, expected_data)
