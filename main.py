import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from data.xkom import XKom
from data.personal import CreatePerson
global browser
import re
from  bs4 import BeautifulSoup

if __name__ == "__main__":
    User = XKom(email_instance_user=CreatePerson.mail())
    User.start_convert()
    # User.all_in_class()
    time.sleep(10)

# import unittest
#
# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
#     def test_math(self):
#         a = 4
#         b = 4
#         self.assertEqual(a+b, 9)
#
#     def test_math1(self):
#         a = 4
#         b = 8
#         self.assertEqual(a + b, 12)
#
#     def test_math2(self):
#         a = 41
#         b = 4
#         self.assertEqual(a + b, 44)
#
#
# if __name__ == '__main__':
#     unittest.main()
