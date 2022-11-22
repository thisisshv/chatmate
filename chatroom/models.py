from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class chatRoom(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
