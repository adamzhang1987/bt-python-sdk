import unittest
import warnings

from pybt.system import System
from pybt.exceptions import InvalidAPIKey
from .config import CONFIG


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = System(CONFIG.get("panel_address"), CONFIG.get("api_key"))
        
    def test_api_key_error(self):
        with self.assertRaises(InvalidAPIKey):
            api_err_key = System(CONFIG.get("panel_address"), "somewords"+CONFIG.get("api_key"))
            api_err_key.get_system_total()
        
    def test_get_system_total(self):
        self.assertIsInstance(self.api.get_system_total(), dict)
        self.assertIn("system", self.api.get_system_total())
        self.assertIn("version", self.api.get_system_total())
        
    def test_get_disk_info(self):
        self.assertIsInstance(self.api.get_disk_info(), list)
        self.assertIn("filesystem", self.api.get_disk_info()[0])
        self.assertIn("type", self.api.get_disk_info()[0])
        
    def test_get_net_work(self):
        self.assertIsInstance(self.api.get_net_work(), dict)
        self.assertIn("network", self.api.get_net_work())
        
    def test_get_task_count(self):
        self.assertIsInstance(self.api.get_task_count(), int)
        
    def test_update_panel(self):
        self.assertIsInstance(self.api.update_panel(), dict)
        self.assertIn("status", self.api.update_panel())
        self.assertIn("version", self.api.update_panel().get('msg'))