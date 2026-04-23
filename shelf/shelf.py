import bs4
import requests


class BookShelf:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_url(self) -> str:
        return f"https://www.goodreads.com/shelf/show/{self.name}"

    def fetch_text(self) -> str:
        user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/109.0.0.0 Safari/537.36"
        )
        headers = {"User-Agent": user_agent}
        response = requests.get(self.get_url(), headers=headers)
        if response.status_code == 200:
            return response.text
        return ""

    def parse(self) -> list[dict[str, str]]:
        shelf_page = self.fetch_text()
        book_list = _parse_bookshelf_from_markup(shelf_page)
        return book_list


def _parse_bookshelf_from_markup(markup: str) -> list[dict[str, str]]:
    book_list: list[dict[str, str]] = []
    if not markup:
        return book_list
    page = bs4.BeautifulSoup(markup, features="lxml")
    list_container = page.find(class_="leftContainer")
    list_container = list_container.find_all(class_="elementList")
    for item in list_container:
        book = item.find(class_="bookTitle")
        author = item.find(class_="authorName")
        shelf_description = str(item.find(class_="smallText").text[1:-1])
        image_url = str(item.find(class_="leftAlignedImage").find("img").get("src"))
        author_url = str(author.get("href"))
        book_url = str("https://www.goodreads.com" + book.get("href"))
        book_name = str(book.text)
        author_name = str(author.text)

        book_dict = {
            "name": book_name,
            "author": author_name,
            "url": book_url,
            "author_url": author_url,
            "shelf_description": shelf_description,
            "image": image_url,
        }
        book_list.append(book_dict)

    return book_list


if __name__ == "__main__":
    # for debugging
    print(BookShelf("clasics").parse()[0])
