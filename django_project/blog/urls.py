from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="posts"),
    # http://localhost:8081/post/create
    path("post/create/", views.create_post, name="post-create"),
    # https://www.pythontutorial.net/django-tutorial/django-edit-form/
    path("post/edit/<int:id>/", views.edit_post, name="post-edit"),
    path("post/delete/<int:id>/", views.delete_post, name="post-delete"),
    path("about/", views.about, name="about"),
]
