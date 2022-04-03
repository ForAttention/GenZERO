import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
global browser


class XKom:

    def __init__(self, password="Bartosz.123", **kwargs):
        self.mail = kwargs
        self.password = password
        self.first_name = kwargs
        self.last_name = kwargs

    def register(self=None):
        """Od wersji 4.0 (jakoś po nowym roku) nie można już używać klasycznego find_element_by_class_name ;_;"""
        time.sleep(5)
        a = browser.find_elements(By.CLASS_NAME, "sc-15ih3hi-0 sc-1p1bjrl-8 hdctio")
        print(len(a))
        # tu jest problem, bo nie może znaleźć elementu z klasą, aby go kliknąć (zamknąć)
        # browser.find_element(By.CLASS_NAME, "sc-15ih3hi-0 sc-1p1bjrl-8 hdctio").click()
        browser.find_element(By.CLASS_NAME, "fz2r3r-1 UXhQi").click()
        browser.find_element(By.CLASS_NAME, "sc-1h16fat-0 rpxbpj-6 rpxbpj-7 dbQHIr sc-153gokr-0 gtqbUj").click()
        time.sleep(5)
        pass


if __name__ == "__main__":
    """Wystarczy nam sam ChromeDriverManager z install, zapewne każdy korzysta lub ma przeglądarkę Google Chrome
        W przypadku przykładu - nie chcę wrzucać na gita plików .exe (chromedriver.exe)"""

    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.set_page_load_timeout(10)  # dajemy 10 sekund na załadowanie
    browser.implicitly_wait(10)
    browser.get("https://www.x-kom.pl")
    browser.maximize_window()
    User = XKom
    User.register()




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