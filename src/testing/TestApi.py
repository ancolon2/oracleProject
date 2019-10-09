import json
import unittest
from lxml import html
from src.app import app

app.testing = True


class TestApi(unittest.TestCase):
    def test_domain_oracle(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'domain': 'oracle.com'}
            result = client.post(
                '/api/domain',
                data=sent
            )
            content = html.fromstring(result.data)
            domain_result = content.xpath('//p/text()')
            print(domain_result)
            expected = ['{"20 aserp2020.oracle.com.": "aserp2020.oracle.com.", "20 aserp2030.oracle.com.": "aserp2030.oracle.com.", "20 aserp2040.oracle.com.": "aserp2040.oracle.com.", "20 aserp2050.oracle.com.": "aserp2050.oracle.com.", "20 aserp2060.oracle.com.": "aserp2060.oracle.com.", "20 userp2020.oracle.com.": "userp2020.oracle.com.", "20 userp2030.oracle.com.": "userp2030.oracle.com.", "20 userp2040.oracle.com.": "userp2040.oracle.com.", "20 userp2050.oracle.com.": "userp2050.oracle.com.", "20 userp2060.oracle.com.": "userp2060.oracle.com."}']
            self.assertEqual(
                expected,
                domain_result
            )

    def test_domain_google(self):
        with app.test_client() as client:
            # send data as POST form to endpoint
            sent = {'domain': 'google.com'}
            result = client.post(
                '/api/domain',
                data=sent
            )
            content = html.fromstring(result.data)
            domain_result = content.xpath('//p/text()')
            print(domain_result)
            expected = ['{"10 aspmx.l.google.com.": "aspmx.l.google.com.", "20 alt1.aspmx.l.google.com.": "alt1.aspmx.l.google.com.", "30 alt2.aspmx.l.google.com.": "alt2.aspmx.l.google.com.", "40 alt3.aspmx.l.google.com.": "alt3.aspmx.l.google.com.", "50 alt4.aspmx.l.google.com.": "alt4.aspmx.l.google.com."}']
            self.assertEqual(
                expected,
                domain_result
            )

if __name__ == '__main__':
    unittest.main()
