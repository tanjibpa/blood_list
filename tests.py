from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # ensure that search page load correctly
    def test_search_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Search by blood group' in response.data)


if __name__ == '__main__':
    unittest.main()
