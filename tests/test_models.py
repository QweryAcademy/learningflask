from .import BaseTestCase
from src.models import User


class UserModelTestCase(BaseTestCase):
    def test_firstname_exists_in_user_model(self):
        aa = User(first_name="James", email="james@example.com")
        aa.save()
        self.assertEqual(aa.first_name, "James")
        self.assertEqual(aa.slug, "james")
