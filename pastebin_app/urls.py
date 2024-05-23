from django.urls import path
from .views import postText, renderSuccess, deleteText

urlpatterns = [
    path("", postText, name="postText"),
    path("delete/", deleteText, name="deleteText"),
    path("<str:link>/", renderSuccess, name="renderSuccess"),
]
