from django.shortcuts import render, redirect, reverse
from django.core.cache import cache
from django.utils.text import slugify
from .shelf import get_book_list_from_shelf
from .forms import SearchForm


def index(request):
    form = SearchForm(request.POST or None)
    template = "shelf/home.html"
    if form.is_valid():
        shelf_name = form.cleaned_data.get("shelf_name", None)
        shelf_name = slugify(shelf_name)
        if shelf_name:
            return redirect(
                reverse(
                    "shelf_view",
                    kwargs={"shelf": shelf_name}
                )
            )
    context = {
        "form": form
    }
    return render(request, template, context)


def shelf_view(request, shelf):
    template = "shelf/shelf.html"
    cached_list = cache.get(shelf, None)
    book_list = cached_list
    if cached_list is None:
        book_list = get_book_list_from_shelf(shelf=shelf)
        cache.set(shelf, book_list)
    context = {
        "shelf_name": shelf,
        "book_list": book_list
    }
    return render(request, template, context)
