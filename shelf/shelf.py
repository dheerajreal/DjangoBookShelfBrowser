from typing import List
import bs4
import requests


def get_shelf_url(shelf: str = None) -> str:
    return f"https://www.goodreads.com/shelf/show/{shelf}"


def get_url_contents(url: str = None) -> str:
    if url is not None:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    return ""


def parse_bookshelf_from_markup(markup: str = None) -> List:
    if markup is None or markup == "":
        return []
    page = bs4.BeautifulSoup(markup, features="lxml")
    list_container = page.find(class_="leftContainer")
    list_container = list_container.find_all(class_="elementList")
    book_list = []
    for item in list_container:
        book = item.find(class_="bookTitle")
        author = item.find(class_="authorName")
        shelf_description = item.find(class_="smallText").text[1:-1]
        image_url = item.find(class_="leftAlignedImage").find("img").get("src")

        book_dict = {
            "name": book.text,
            "url": "https://www.goodreads.com" + book.get("href"),
            "author": author.text,
            "author_url": author.get("href"),
            "shelf_description": shelf_description,
            "image": image_url,
        }
        book_list.append(book_dict)

    return book_list


def get_book_list_from_shelf(shelf: str = None) -> List:
    shelf_url = get_shelf_url(shelf=shelf)
    shelf_page = get_url_contents(shelf_url)
    book_list = parse_bookshelf_from_markup(shelf_page)
    return book_list


if __name__ == "__main__":
    # for debugging
    print(get_book_list_from_shelf("clasics")[0])
