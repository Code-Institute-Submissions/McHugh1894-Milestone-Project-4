from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reviews.views import add_review, edit_review, delete_review


class Test_urls(SimpleTestCase):
    """ test reviews urls configured correctly"""
    def test_add_review_resolves(self):
        url = reverse('add_review', args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_review)

    def test_edit_review_resolves(self):
        url = reverse('edit_review', args=[2, 4])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_review)

    def test_delete_review_resolves(self):
        url = reverse('delete_review', args=[2, 4])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_review)