from django.test import SimpleTestCase
from reviews.forms import ReviewForm


class TestForms(SimpleTestCase):
    """ test reviews forms configured correctly"""
    def test_Review_Form_valid_data(self):
        form = ReviewForm(data={
            'rating': 3,
            'title': 'test title',
            'comment': 'test'
        })

        self.assertTrue(form.is_valid())

    def test_review_form_invalid(self):
        form = ReviewForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)