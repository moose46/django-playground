# Create your models here.
from email.policy import default
from tkinter import CASCADE
from typing import Any

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=32)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=120)
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        #     db_table = "posts"
        ordering = ["-published_at"]
