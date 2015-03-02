from django.test import TestCase
from bullet_app.lib.bulletparser import parse


class BulletParserTest(TestCase):

    def test_parses_signs_out(self):
        text = "+ This should be returned without a sign"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "This should be returned without a sign")
        self.assertEqual(bullet_dict["positive"], 1)
        self.assertEqual(bullet_dict["negative"], 0)

        text = "+++ This should be returned without a sign also"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "This should be returned without a sign also")
        self.assertEqual(bullet_dict["positive"], 3)
        self.assertEqual(bullet_dict["negative"], 0)

        text = "-- text"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "text")
        self.assertEqual(bullet_dict["positive"], 0)
        self.assertEqual(bullet_dict["negative"], 2)

        text = "++/--- text - +"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "text - +")
        self.assertEqual(bullet_dict["positive"], 2)
        self.assertEqual(bullet_dict["negative"], 3)

        text = "++ / --- text"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "text")
        self.assertEqual(bullet_dict["positive"], 2)
        self.assertEqual(bullet_dict["negative"], 3)

        text = "This should be returned without a sign"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "This should be returned without a sign")
        self.assertEqual(bullet_dict["positive"], 1)
        self.assertEqual(bullet_dict["negative"], 0)

        text = "+++++++ / ------- Only 5 per!"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "Only 5 per!")
        self.assertEqual(bullet_dict["positive"], 5)
        self.assertEqual(bullet_dict["negative"], 5)
