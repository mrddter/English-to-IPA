# -*- coding: utf-8 -*-
import stress
import conversion
import unittest


class TestConversion(unittest.TestCase):
    """Simple unit testing for the stress functions."""

    def test_stress_type(self):
        self.assertEqual(stress.stress_type("primary"), {"1": "ˈ"})
        self.assertEqual(stress.stress_type("secondary"), {"2": "ˌ"})
        self.assertEqual(stress.stress_type("all"), {"1": "ˈ", "2": "ˌ"})
        self.assertEqual(stress.stress_type("both"), {"1": "ˈ", "2": "ˌ"})
        self.assertEqual(stress.stress_type("tertiary"), {"1": "ˈ", "2": "ˌ"})

    def test_find_stress(self):
        test_string = "reflect respect recline reduce obsessively demonstrate baseball cloud brother cobblestone " +\
            "complete conspire conflict"
        raw_cmu = conversion.get_cmu(test_string.split(" ")[:-1])
        result = []
        for word_list in raw_cmu:
            for word in word_list:
                stressed = stress.find_stress(word)
                result.append(stressed)
        self.assertEqual(result, ['r ah ˈf l eh k t', 'r ih ˈf l eh k t', 'r ih ˈs p eh k t', 'r iy ˈs p eh k t',
                                  'r ih ˈk l ay n', 'r ih ˈd uw s', 'aa b ˈs eh s ih v l iy',
                                  'ˈd eh m ah n ˌs t r ey t', 'ˈb ey s ˈb ao l', 'k l aw d', 'ˈb r ah dh er',
                                  'ˈk aa b ah l ˌs t ow n', 'k ah m ˈp l iy t', 'k ah n ˈs p ay er'])

        # test the retrieval of only primary stress
        self.assertEqual(stress.find_stress("d eh1 m ah0 n s t r ey2 t", type="primary"), 'ˈd eh m ah n s t r ey t')
        # test the retrieval of only secondary stress
        self.assertEqual(stress.find_stress("d eh1 m ah0 n s t r ey2 t", type="secondary"), 'd eh m ah n ˌs t r ey t')


if __name__ == "__main__":
    unittest.main()
