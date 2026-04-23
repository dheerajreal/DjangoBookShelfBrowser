from django.http import HttpRequest
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.utils.text import slugify
from .shelf import get_book_list_from_shelf
from .forms import SearchForm


def index(request: HttpRequest):
    form = SearchForm(request.POST or None)
    template = "shelf/home.html"
    if form.is_valid():
        shelf_name = form.cleaned_data.get("shelf_name") or ""
        shelf_name = slugify(shelf_name)
        if shelf_name:
            return redirect(to=reverse("shelf_view", kwargs={"shelf": shelf_name}))
    context = {"form": form}
    return render(request, template, context)


def shelf_view(request: HttpRequest, shelf: str):
    template = "shelf/shelf.html"
    cached_list = cache.get(shelf, None)
    book_list = cached_list
    if cached_list is None:
        book_list = get_book_list_from_shelf(shelf=shelf)
        cache.set(shelf, book_list)
    context: dict[str, object] = {"shelf_name": shelf, "book_list": book_list}
    return render(request, template, context)
