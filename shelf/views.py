from django.shortcuts import render

from .shelf import get_book_list_from_shelf


def shelf_view(request, shelf):
    template = "shelf/shelf.html"
    book_list = get_book_list_from_shelf(shelf=shelf)
    context = {
        "shelf_name": shelf,
        "book_list": book_list
    }
    return render(request, template, context)
