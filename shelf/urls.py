from django.urls import path
from .views import shelf_view, index

urlpatterns = [
    path('', index, name="index"),
    path('shelf/<slug:shelf>/', shelf_view, name="shelf_view"),
]
