from django.urls import path
from .views import shelf_view
urlpatterns = [
    path('shelf/<slug:shelf>/', shelf_view, name="shelf_view"),
]
