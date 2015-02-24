from django.test import TestCase
from bullet_app.lib.bulletparser import parse


class BulletParserTest(TestCase):

    def test_parses_signs_out(self):
        text = "+ This should be returned without a sign"
        self.assertEqual(parse(text)["parsedtext"],
                         "This should be returned without a sign")

        text = "+++ This should be returned without a sign also"
        self.assertEqual(parse(text)["parsedtext"],
                         "This should be returned without a sign also")

        text = "-- text"
        self.assertEqual(parse(text)["parsedtext"],
                         "text")

        text = "++/--- text - +"
        self.assertEqual(parse(text)["parsedtext"],
                         "text - +")

        text = "++ / --- text"
        self.assertEqual(parse(text)["parsedtext"],
                         "text")
