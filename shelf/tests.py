from django.test import SimpleTestCase
from django.urls import reverse
from django.utils.text import slugify


class ShelfTest(SimpleTestCase):
    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("shelf/home.html")

    def test_index2(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "form")
        self.assertContains(response, "Bookshelf browser")

    def test_index_form(self):
        search_term = "dog"
        response = self.client.post(
            reverse("index"), data={"shelf_name": search_term}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse(
                "shelf_view", kwargs={"shelf": search_term}
            )
        )
        response = self.client.get(response.url)
        self.assertContains(response, search_term)
        self.assertContains(response, "Bookshelf browser")

    def test_index_form2(self):
        search_term = "modern classics"
        response = self.client.post(
            reverse("index"), data={"shelf_name": search_term}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse(
                "shelf_view", kwargs={"shelf": slugify(search_term)}
            )
        )
        response = self.client.get(response.url)
        self.assertContains(response, slugify(search_term))
        self.assertContains(response, "Bookshelf browser")

    def test_shelf(self):
        shelf_name = "classics"
        response = self.client.get(
            reverse(
                "shelf_view", kwargs={"shelf": shelf_name}
            )
        )
        self.assertContains(response, shelf_name)
        self.assertContains(response, "Bookshelf browser")

    def test_shelf2(self):
        shelf_name = "sknfclzknfckdnfekiehgvfedkighfekbefejubgtoueljgb"
        response = self.client.get(
            reverse(
                "shelf_view", kwargs={"shelf": shelf_name}
            )
        )
        self.assertContains(response, shelf_name)
        self.assertContains(response, "Bookshelf browser")
        self.assertContains(response, "Empty Bookshelf")
