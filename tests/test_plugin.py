import unittest
import warnings

from pybt.plugin import Plugin
from .config import CONFIG


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = Plugin(CONFIG.get("panel_address"), CONFIG.get("api_key"))
        
    def test_deployment(self):
        self.assertIsInstance(self.api.deployment(), dict)
