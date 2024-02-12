from django.urls import path, include

from api import views

urlpatterns = [
    path("", views.index, name="index"),
    path('collections/', include("api.collections.urls")),
]
