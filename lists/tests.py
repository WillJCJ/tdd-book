from django.test import TestCase
from lists.views import home_page
from django.core.urlresolvers import resolve

class SmokeTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)