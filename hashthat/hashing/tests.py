from django.test import TestCase
from selenium import webdriver

class FunctionalTestCase(TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome()

    def homePage_exist(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('install', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()
    