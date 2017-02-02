"""
Testing - How to test credit.py

"""


import unittest
from lists import credit


class TestCardValidity(unittest.TestCase):

    def test_good_card_number_is_valid(self):
        good_acct_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]
        self.assertTrue(credit.validate(good_acct_num))


    def test_bad_card_number_is_invalid(self):
        bad_acct_num = [6, 5, 1, 6, 4, 3, 7, 5, 1, 6, 4, 9, 3, 8, 5, 4]
        self.assertTrue(credit.validate(bad_acct_num))


class TestCreditFunctions(unittest.TestCase):

    def setUp(self):
        self.good_acct_num = [4, 5, 5, 6, 7, 3, 7, 5, 8, 6, 8, 9, 9, 8, 5, 5]

    def test_validate(self):
        self.assertTrue(credit.validate(self.good_acct_num),
                        "Account Num Wrong Length")


    def test_check_digit(self):
        self.assertTrue(credit.check_digit(self.good_acct_num),
                        "Check Digit broken")


    def test_reverse_digits(self):
        self.assertTrue(credit.reverse_digits(self.good_acct_num),
                        "Reverse Digits broken")

    def test_double_every_other_digit(self):
        self.assertTrue(credit.double_every_other_digit(self.good_acct_num),
                        "Double Every Other Digit broken")


    def test_second_digit(self):
        self.assertTrue(credit.second_digit(self.good_acct_num),
                        "Second Digit broken")


    def test_run_program(self):
        self.assertEqual(credit.run_program(self.good_acct_num), "Valid!",
                        "Run Program broken")


if __name__ == '__main__':
    unittest.main()