"""Configuration module for the BaoTa Panel SDK.

This module contains all the configuration settings, API endpoints, and constants
used throughout the SDK.
"""

from typing import Dict, Optional
from dataclasses import dataclass, field


@dataclass
class Config:
    """Configuration class for BaoTa Panel SDK.
    
    This class holds all configuration settings including API endpoints,
    authentication details, and other runtime settings.
    """
    # API endpoints
    endpoints: Dict[str, str] = field(default_factory=lambda: {
        # System status related endpoints
        "GetSystemTotal": "/system?action=GetSystemTotal",
        "GetDiskInfo": "/system?action=GetDiskInfo",
        "GetNetWork": "/system?action=GetNetWork",
        "GetTaskCount": "/ajax?action=GetTaskCount",
        "UpdatePanel": "/ajax?action=UpdatePanel",
        
        # Website basic operations
        "Websites": "/data?action=getData&table=sites",
        "Webtypes": "/site?action=get_site_types",
        "GetPHPVersion": "/site?action=GetPHPVersion",
        "WebAddSite": "/site?action=AddSite",
        "WebDeleteSite": "/site?action=DeleteSite",
        "WebSiteStop": "/site?action=SiteStop",
        "WebSiteStart": "/site?action=SiteStart",
        "WebSetEdate": "/site?action=SetEdate",
        "WebSetPs": "/data?action=setPs&table=sites",
        
        # Website backup management
        "WebBackupList": "/data?action=getData&table=backup",
        "WebToBackup": "/site?action=ToBackup",
        "WebDelBackup": "/site?action=DelBackup",
        
        # Domain management
        "WebDomainList": "/data?action=getData&table=domain",
        "WebAddDomain": "/site?action=AddDomain",
        "WebDelDomain": "/site?action=DelDomain",
        
        # Rewrite and configuration management
        "GetRewriteList": "/site?action=GetRewriteList",
        "GetFileBody": "/files?action=GetFileBody",
        "SaveFileBody": "/files?action=SaveFileBody",
        
        # Website directory and runtime configuration
        "GetDirUserINI": "/site?action=GetDirUserINI",
        "SetDirUserINI": "/site?action=SetDirUserINI",
        "LogsOpen": "/site?action=logsOpen",
        "SetPath": "/site?action=SetPath",
        "SetSiteRunPath": "/site?action=SetSiteRunPath",
        
        # Password access control
        "SetHasPwd": "/site?action=SetHasPwd",
        "CloseHasPwd": "/site?action=CloseHasPwd",
        
        # Traffic limit (nginx only)
        "GetLimitNet": "/site?action=GetLimitNet",
        "SetLimitNet": "/site?action=SetLimitNet",
        "CloseLimitNet": "/site?action=CloseLimitNet",
        
        # Default document management
        "WebGetIndex": "/site?action=GetIndex",
        "WebSetIndex": "/site?action=SetIndex"
    })
    
    # Authentication settings
    api_key: Optional[str] = None
    bt_panel_host: str = None
    
    # Runtime settings
    debug: bool = False
    timeout: int = 30
    verify_ssl: bool = True
    
    def get_endpoint(self, name: str) -> str:
        """Get API endpoint by name.
        
        Args:
            name: Name of the endpoint
            
        Returns:
            Full API endpoint URL
            
        Raises:
            KeyError: If endpoint name is not found
        """
        if name not in self.endpoints:
            raise KeyError(f"Endpoint '{name}' not found in configuration")
        return f"{self.endpoints[name]}"


# Default configuration instance
config = Config() 