import unittest
import warnings

from pybt.dbm import DBM
from .config import CONFIG


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = DBM(CONFIG.get("panel_address"), CONFIG.get("api_key"))
        
    def test_web_db_list(self):
        self.assertIsInstance(self.api.web_db_list(), dict)
        self.assertIn("where", self.api.web_db_list())
        self.assertIn("page", self.api.web_db_list())
        self.assertIn("data", self.api.web_db_list())