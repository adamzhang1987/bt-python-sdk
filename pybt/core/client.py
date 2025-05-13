"""Base client module for BaoTa Panel SDK.

This module provides the base client class that handles API communication
and authentication.
"""

from typing import Dict, Any, Optional
import requests
import time 
import os
from dotenv import load_dotenv, find_dotenv
from .config import Config
from .token import get_token
from pybt.utils.logger import logger
from pybt.utils.exceptions import InvalidAPIKey

load_dotenv(find_dotenv())


class Client:
    """Base client class for BaoTa Panel API.
    
    This class provides the core functionality for making API requests to the
    BaoTa Panel, including authentication and request handling.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        bt_panel_host: Optional[str] = None,
        debug: Optional[bool] = None,
        timeout: Optional[int] = None,
        verify_ssl: Optional[bool] = None
    ) -> None:
        """Initialize the client with configuration.
        
        Args:
            api_key: API key for authentication
            secret_key: Secret key for authentication
            host: API host URL
            debug: Enable debug mode
            timeout: Request timeout in seconds
            verify_ssl: Whether to verify SSL certificates
        """
        self.session = requests.Session()
        self.__cookies = None
        self.config = Config()
        
        # Override default config with provided values
        if api_key is None:
            self.config.api_key = os.getenv("BT_API_KEY")
        else:
            self.config.api_key = api_key
        if bt_panel_host is None:
            self.config.bt_panel_host = os.getenv("BT_PANEL_HOST")
        else:
            self.config.bt_panel_host = bt_panel_host
        if debug is None:
            debug_env = os.getenv("DEBUG")
            self.config.debug = debug_env.lower() == "true" if debug_env else False
        else:
            self.config.debug = debug
        if timeout is None:
            timeout_env = os.getenv("TIMEOUT")
            self.config.timeout = int(timeout_env) if timeout_env else self.config.timeout
        else:
            self.config.timeout = timeout
        if verify_ssl is None:
            verify_ssl_env = os.getenv("VERIFY_SSL")
            self.config.verify_ssl = verify_ssl_env.lower() == "true" if verify_ssl_env else True
        else:
            self.config.verify_ssl = verify_ssl
            
        if not self.config.api_key:
            raise InvalidAPIKey("API key is required")
    
    def __get_key(self) -> str:
        """Get API key for request"""
        now_time = time.time()
        p_data = {
            "request_token": get_token(now_time, self.config.api_key),
            "request_time": now_time
        }
        return p_data
    
    def post_data(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Make a POST request to the API.
        
        Args:
            endpoint: API endpoint name or full URL
            data: Request data to send
            
        Returns:
            API response data
            
        Raises:
            requests.RequestException: If the request fails
        """ 
        body = self.__get_key()
        url = self.config.bt_panel_host + endpoint
        
        if data:
            body.update(data)
        
        logger.debug(f"Making POST request to {endpoint}")
        logger.debug(f"Request data: {data}")
        
        try:
            if self.__cookies:
                response = self.session.post(
                    url,
                    body,
                    timeout=self.config.timeout,
                    verify=self.config.verify_ssl,
                    cookies=self.__cookies
                )
            else:
                response = self.session.post(
                    url,
                    body,
                    timeout=self.config.timeout,
                    verify=self.config.verify_ssl
                )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise
