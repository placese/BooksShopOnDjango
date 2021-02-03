from django.test import TestCase

from store.serializers import BookSerializer
from store.models import Book


class BookSerializerTestCase(TestCase):
	def setUp(self):
		self.book_1 = Book.objects.create(name='Test book 1', price=1000.00, author_name='Author 1')
		self.book_2 = Book.objects.create(name='Test book 2', price=1250.00, author_name='Author 2')


	def test_ok(self):
		data = BookSerializer([self.book_1, self.book_2], many=True).data
		expected_data = [
		{
			'id': self.book_1.id,
			'name': 'Test book 1',
			'price': '1000.00',
			'author_name': 'Author 1'
		},
		{
			'id': self.book_2.id,
			'name': 'Test book 2',
			'price': '1250.00',
			'author_name': 'Author 2'
		}
		]

		self.assertEqual(data, expected_data)
