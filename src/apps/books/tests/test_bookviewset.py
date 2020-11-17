from django.contrib.auth.models import User
from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from src.apps.books.models import Book


class BookViewSetCreateTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = User.objects.create(first_name='John', last_name='Maeda')

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('books:book-list')

    def test_unauthorized(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test(self):
        data = {
            'author': self.author.id,
            'title': 'The Laws of Simplicity',
            'text': 'Simplicity is about subtracting the obvious, and adding the meaningful.',
        }
        self.client.force_authenticate(self.author)
        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        book = Book.objects.get()
        self.assertEqual(response.data, {'id': book.id, **data, })
        self.assertEqual(model_to_dict(book), {'id': book.id, **data})


class BookViewSetListTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = User.objects.create(first_name='test', last_name='test')
        self.books = [Book.objects.create(title=f'book {b}', author=self.author, text=f'text {b}') for b in range(10)]

    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('books:book-list')

    def test_unauthorized(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test(self):
        self.client.force_authenticate(self.author)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            [
                {
                    'id': book.id, 'title': book.title,
                    'text': book.text, 'author': book.author_id
                } for book in self.books
            ]
        )


class BookViewSetRetrieveTestCase(APITestCase):
    def setUp(self) -> None:
        self.author = User.objects.create(first_name='test', last_name='test')
        self.book = Book.objects.create(title=f'book', author=self.author, text=f'text')
        self.url = reverse('books:book-detail', kwargs={'pk': self.book.id})  # url is not static

    def test_unauthorized(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

    def test(self):
        self.client.force_authenticate(self.author)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                'id': self.book.id, 'title': self.book.title,
                'text': self.book.text, 'author': self.book.author_id
            }
        )
