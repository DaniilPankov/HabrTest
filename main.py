import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import page


class HabrTest(unittest.TestCase):

    def setUp(self):
        url = 'https://habr.com/ru/search/'

        op = Options()


        op.add_argument("--no-sandbox")
        op.add_argument("start-maximized")
        op.add_argument("window-size=1900,1080")
        op.add_argument("disable-gpu")
        op.add_argument("--disable-software-rasterizer")
        op.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=op)
        self.driver.get(url)

    def test_negative_search(self):
        assert page.check_negative_search(self.driver)

    def test_positive_search(self):
        assert page.check_positive_search(self.driver)

    def test_user(self):
        assert page.check_user(self.driver)

    def test_company(self):
        assert page.check_company(self.driver)

    def test_authorization(self):
        assert page.check_authorization(self.driver)

    def tearDown(self):
        self.driver.quit()
