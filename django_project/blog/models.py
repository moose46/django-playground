# Create your models here.
from email.policy import default
from tkinter import CASCADE
from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

"""
Base model representing common fields for other models.

Explanation:
This class serves as a base model with common fields like published_at, updated_at, and author. It is meant to be inherited by other models.

Args:
- author: ForeignKey to the User model.

Returns:
None.

Raises:
None.
"""


class Base(models.Model):
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Project(Base):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=120)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        #     db_table = "posts"
        ordering = ["-published_at"]
