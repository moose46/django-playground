import datetime
from email.policy import default
from typing import Any, Mapping

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import DateField, DateInput, ModelForm

# from django_project.users import forms
from django.forms.utils import ErrorList
from django.utils import timezone

from .models import Post, Project


class PostForm(ModelForm):
    # published_at = forms.DateField(
    #     widget=forms.DateInput(
    #         attrs={"type": "date"},
    #     ),
    # )
    # published_at.initial = default = timezone.now
    # content = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": "40"}))

    class Meta:
        model = Post
        fields = [
            "project",
            "title",
            "content",
        ]
        # https://docs.djangoproject.com/en/5.0/topics/forms/modelforms/
        widgets = {"content": forms.Textarea(attrs={"rows": 4, "cols": "40"})}
        labels = {"content": "Detailed Description"}


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class HomeForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({"class": "form-control"})
        for field in self.fields:
            self.fields["name"].widget.attrs.update({"class": "form-control"})
