import unittest

from django.test import TestCase

class HomePagetTest(TestCase):
    """ Testing the  home page. """
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
