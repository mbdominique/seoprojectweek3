import unittest, sys

sys.path.append('../seoprojectweek3') # imports python file from parent directory
from app import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    def test_home_page(self):
        response = self.app.get('/home', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register_page_get(self):
        response = self.app.get('/register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Add a test for POST request to register
    def test_register_page_post(self):
        response = self.app.post('/register', data=dict(
            username='testuser',
            email='test@example.com',
            password='testpassword',
            confirm_password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account created for testuser!', response.data)

if __name__ == "__main__":
    unittest.main()