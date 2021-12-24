import unittest
import warnings

from pybt.ftp import Ftp
from .config import CONFIG


class ClientTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        self.api = Ftp(CONFIG.get("panel_address"), CONFIG.get("api_key"))
        
    def test_web_ftp_list(self):
        self.assertIsInstance(self.api.web_ftp_list(), dict)
        self.assertIn("where", self.api.web_ftp_list())
        self.assertIn("page", self.api.web_ftp_list())
        self.assertIn("data", self.api.web_ftp_list())