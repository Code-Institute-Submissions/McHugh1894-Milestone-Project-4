from django.test import TestCase
from reviews.models import Review
from products.models import Category, Product
from django.contrib.auth.models import User


class TestModels(TestCase):
    """ test reviews model configured correctly"""
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='testpassword'
        )
        self.category = Category.objects.create(
            name="test_category",
            friendly_name="Test Category",
        )
        self.product = Product.objects.create(
            sku=1,
            name="tests item",
            description="test description",
            price="11.99",
            image="testimg.jpg",
            category=self.category,
        )
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            title='Test Title',
            comment="Test Review",
            rating=3,
        )

    def test_review_model(self):
        """ test reviews model"""
        self.assertEqual(str(self.review), "Review on tests item by testuser")