"""This module contains tests for the task0

It demonstrates behaviour of the app and how it should be used.
Besides it checks for special acts which probably never wouldn't
be performed.
Task:
    Translate russian text to transliteration and vice versa
"""
import locale
import unittest
import string
from unittest import mock
from day1.task0 import get_user_env_lang as us_lan, transliteration, \
                   get_user_prompt


class TransliterateTest(unittest.TestCase):

    def test_environment_exist(self):
        """This test checks whether users locale contain in real locales
        """
        exist_locales = locale.locale_alias
        self.assertIn(
            us_lan().split('.')[0].lower(), exist_locales.keys()
        )

    @mock.patch('builtins.input', side_effect=[''])
    def test_user_prompt_is_string(self, user_input):
        """This test checks whether prompt by user is instance of str or not
        """
        user_prompt = get_user_prompt(us_lan())
        self.assertIsInstance(user_prompt, str)

    def test_check_transliteration_is_successful(self):
        """This test checks whether transliteration works or pass
        """
        self.assertEqual(transliteration('Строка'), 'Stroka')
        self.assertEqual(transliteration('Privet'), 'Привет')
        self.assertEqual(transliteration('Privet строка'), 'Привет stroka')

    def test_check_transliteration_special_symbols(self):
        """This test checks whether special symbols can pass through or not
        """
        output_string = transliteration(string.punctuation)
        self.assertEqual(output_string, string.punctuation)

    def test_check_transliteration_not_capitalise_prompt(self):
        """This test checks whether output is the same capitalisation with
           prompt or not
        """
        test_string = 'mimamo'
        output_string = transliteration(test_string)

        def is_lower_check(sequence):
            """Function for checking whole sequence on islower() == True

            Args:
                sequence (seq): Any iterable object to check

            Returns:
                False: If any char is upper
                True: If every char is lower
            """
            for each_char in sequence:
                if str(each_char).isupper():
                    return False
                return True

        self.assertEqual(
            is_lower_check(test_string), is_lower_check(output_string)
        )

    def test_check_adding_alt_symbols(self):
        """Function that checks whether it is possible to input
           any alternative symbols
        """
        prompt = transliteration('i -!漢')
        self.assertEqual(prompt, 'и -!漢')
