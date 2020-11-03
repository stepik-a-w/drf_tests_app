from rest_framework.viewsets import ModelViewSet

from src.apps.books.models import Book
from src.apps.books.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
