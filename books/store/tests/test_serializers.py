from django.test import TestCase

from django.contrib.auth.models import User

from store.serializers import BookSerializer
from store.models import Book


class BookSerializerTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create(username='test_username')
		self.book_1 = Book.objects.create(name='Test book 1', price=1000.00, author_name='Author 1', owner=self.user)
		self.book_2 = Book.objects.create(name='Test book 2', price=1250.00, author_name='Author 2', owner=self.user)


	def test_ok(self):
		self.client.force_login(self.user)
		data = BookSerializer([self.book_1, self.book_2], many=True).data
		expected_data = [
		{
			'id': self.book_1.id,
			'name': 'Test book 1',
			'price': '1000.00',
			'author_name': 'Author 1',
			'owner': self.user.id
		},
		{
			'id': self.book_2.id,
			'name': 'Test book 2',
			'price': '1250.00',
			'author_name': 'Author 2',
			'owner': self.user.id
		}
		]
		
		self.assertEqual(data, expected_data)
