from .import BaseTestCase


class LoginViewTestCase(BaseTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        import pdb; pdb.set_trace()
        # self.assert200(response)

    def test_login_functionality_works(self):
        response = self.client.post('/login/', data=dict(
            email="gbozee@example.com",
            password="johndoe"
        ), follow_redirects=True)
        # self.assert200(response)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.url, "/")
