from django.urls import path
from shelf import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shelf/<slug:shelf>/", views.shelf_view, name="shelf_view"),
]
