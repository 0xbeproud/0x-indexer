from django.urls import path, include

from .views import CollectionListView

urlpatterns = [
    path("", CollectionListView.as_view()),
]
