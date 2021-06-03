from django.core.cache import cache

from .shelf import get_book_list_from_shelf


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
