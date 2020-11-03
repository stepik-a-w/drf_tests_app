from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=50,
    )

    text = models.TextField()

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
