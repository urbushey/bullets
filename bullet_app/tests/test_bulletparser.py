from django.test import TestCase
from bullet_app.lib.bulletparser import parse


class BulletParserTest(TestCase):

    def test_parses_signs_out(self):
        text = "+ This should be returned without a sign"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "This should be returned without a sign")
        self.assertEqual(bullet_dict["positive_score"], 1)
        self.assertEqual(bullet_dict["negative_score"], 0)

        text = "+++ This should be returned without a sign also"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "This should be returned without a sign also")
        self.assertEqual(bullet_dict["positive_score"], 3)
        self.assertEqual(bullet_dict["negative_score"], 0)

        text = "-- text"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "text")
        self.assertEqual(bullet_dict["positive_score"], 0)
        self.assertEqual(bullet_dict["negative_score"], 2)

        text = "++/--- text - +"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "text - +")
        self.assertEqual(bullet_dict["positive_score"], 2)
        self.assertEqual(bullet_dict["negative_score"], 3)

        text = "++ / --- text"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "text")
        self.assertEqual(bullet_dict["positive_score"], 2)
        self.assertEqual(bullet_dict["negative_score"], 3)

        text = "This should be returned without a score"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "This should be returned without a score")
        self.assertRaises(KeyError, lambda: bullet_dict["positive_score"])
        self.assertRaises(KeyError, lambda: bullet_dict["negative_score"])

        text = "+++++++ / ------- Only 5 per!"
        bullet_dict = parse(text)
        self.assertEqual(bullet_dict["parsed_text"],
                         "Only 5 per!")
        self.assertEqual(bullet_dict["positive_score"], 5)
        self.assertEqual(bullet_dict["negative_score"], 5)
