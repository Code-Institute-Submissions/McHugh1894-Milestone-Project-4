from django.test import TestCase
from reviews import apps


class ReviewsAppTests(TestCase):

    def test_reviews_apps_config(self):
        """ test reviews app configured correctly"""

        self.assertEqual(apps.ReviewsConfig.name, 'reviews')