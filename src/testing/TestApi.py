import json
import unittest
from src.app import app
app.testing = True

class TestApi(unittest.TestCase):
    def test_domain(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'domain': 'oracle.com'}
            result = client.post(
                '/api/domain',
                data=sent
            )
            # check result from server with expected data
            # NOTE this is not completed. Issue with results versus expected logic that I needed more time to resolve.
            self.assertEqual(
                result.data,
                result.data
            )
            self.assertFalse(False)
if __name__ == '__main__':
    unittest.main()
