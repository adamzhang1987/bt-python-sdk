import unittest
import warnings

from pybt.sites import Sites
from .config import CONFIG


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = Sites(CONFIG.get("panel_address"), CONFIG.get("api_key"))
        
    def test_websites(self):
        self.assertIsInstance(self.api.websites(), dict)
        self.assertIn("where", self.api.websites())
        self.assertIn("page", self.api.websites())
        self.assertIn("data", self.api.websites())
        
    def test_webtypes(self):
        self.assertIsInstance(self.api.webtypes(), list)
        
    def test_get_php_version(self):
        self.assertIsInstance(self.api.get_php_version(), list)
        
    def test_get_site_php_version(self):
        self.assertIsInstance(self.api.get_site_php_version(), dict)
