"""Website management API classes."""

from typing import Dict, Any, List, Optional
from ..core.client import Client


class Website(Client):
    """Website basic operations API.
    
    This class provides methods for managing websites, including creating,
    deleting, starting, stopping, and modifying website properties.
    """
    
    def get_website_list(self, page: int = 1, limit: int = 15, type_id: int = -1,
                        order: str = "id desc", tojs: Optional[str] = None,
                        search: Optional[str] = None) -> Dict[str, Any]:
        """Get list of websites.
        
        Args:
            page: Current page number
            limit: Number of items per page
            type_id: Category ID (-1 for all categories, 0 for default)
            order: Sort order (e.g., "id desc", "name desc")
            tojs: JS callback for pagination
            search: Search keyword
            
        Returns:
            Dict containing website list and pagination info
        """
        data = {
            "p": page,
            "limit": limit,
            "type": type_id,
            "order": order
        }
        if tojs:
            data["tojs"] = tojs
        if search:
            data["search"] = search
            
        endpoint = self.config.get_endpoint("Websites")
        return self.post_data(endpoint, data)
    
    def get_site_types(self) -> List[Dict[str, Any]]:
        """Get list of website categories.
        
        Returns:
            List of category dictionaries with id and name
        """
        endpoint = self.config.get_endpoint("Webtypes")
        return self.post_data(endpoint)
    
    def get_php_versions(self) -> List[Dict[str, str]]:
        """Get list of installed PHP versions.
        
        Returns:
            List of PHP version dictionaries with version and name
        """
        endpoint = self.config.get_endpoint("GetPHPVersion")
        return self.post_data(endpoint)
    
    def create_website(self, webname: Dict[str, Any], path: str, type_id: int,
                      version: str, port: int = 80, ps: str = "",
                      ftp: bool = False, ftp_username: Optional[str] = None,
                      ftp_password: Optional[str] = None, sql: bool = False,
                      codeing: str = "utf8", datauser: Optional[str] = None,
                      datapassword: Optional[str] = None) -> Dict[str, Any]:
        """Create a new website.
        
        Args:
            webname: Dict containing domain and domainlist
            path: Website root directory
            type_id: Category ID
            version: PHP version
            port: Website port
            ps: Website description
            ftp: Whether to create FTP account
            ftp_username: FTP username
            ftp_password: FTP password
            sql: Whether to create database
            codeing: Database character set
            datauser: Database username
            datapassword: Database password
            
        Returns:
            Dict containing creation status for site, FTP, and database
        """
        data = {
            "webname": webname,
            "path": path,
            "type_id": type_id,
            "type": "PHP",
            "version": version,
            "port": port,
            "ps": ps,
            "ftp": ftp,
            "sql": sql
        }
        
        if ftp and ftp_username and ftp_password:
            data.update({
                "ftp_username": ftp_username,
                "ftp_password": ftp_password
            })
            
        if sql and datauser and datapassword:
            data.update({
                "codeing": codeing,
                "datauser": datauser,
                "datapassword": datapassword
            })
            
        endpoint = self.config.get_endpoint("WebAddSite")
        return self.post_data(endpoint, data)
    
    def delete_website(self, id: int, webname: str, delete_ftp: bool = False,
                      delete_database: bool = False, delete_path: bool = False) -> Dict[str, Any]:
        """Delete a website.
        
        Args:
            id: Website ID
            webname: Website name
            delete_ftp: Whether to delete associated FTP
            delete_database: Whether to delete associated database
            delete_path: Whether to delete website directory
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "webname": webname
        }
        
        if delete_ftp:
            data["ftp"] = 1
        if delete_database:
            data["database"] = 1
        if delete_path:
            data["path"] = 1
            
        endpoint = self.config.get_endpoint("WebDeleteSite")
        return self.post_data(endpoint, data)
    
    def stop_website(self, id: int, name: str) -> Dict[str, Any]:
        """Stop a website.
        
        Args:
            id: Website ID
            name: Website name (main domain)
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "name": name
        }
        endpoint = self.config.get_endpoint("WebSiteStop")
        return self.post_data(endpoint, data)
    
    def start_website(self, id: int, name: str) -> Dict[str, Any]:
        """Start a website.
        
        Args:
            id: Website ID
            name: Website name (main domain)
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "name": name
        }
        endpoint = self.config.get_endpoint("WebSiteStart")
        return self.post_data(endpoint, data)
    
    def set_expiry_date(self, id: int, edate: str) -> Dict[str, Any]:
        """Set website expiry date.
        
        Args:
            id: Website ID
            edate: Expiry date (format: YYYY-MM-DD, use "0000-00-00" for permanent)
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "edate": edate
        }
        endpoint = self.config.get_endpoint("WebSetEdate")
        return self.post_data(endpoint, data)
    
    def set_website_remark(self, id: int, ps: str) -> Dict[str, Any]:
        """Set website remark/description.
        
        Args:
            id: Website ID
            ps: Remark content
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "ps": ps
        }
        endpoint = self.config.get_endpoint("WebSetPs")
        return self.post_data(endpoint, data)


class WebsiteBackup(Client):
    """Website backup management API."""
    
    def get_backup_list(self, search: int, page: int = 1, limit: int = 5) -> Dict[str, Any]:
        """Get website backup list.
        
        Args:
            search: Website ID
            page: Current page number
            limit: Number of items per page
            
        Returns:
            Dict containing backup list and pagination info
        """
        data = {
            "p": page,
            "limit": limit,
            "type": 0,
            "search": search
        }
        endpoint = self.config.get_endpoint("WebBackupList")
        return self.post_data(endpoint, data)
    
    def create_backup(self, id: int) -> Dict[str, Any]:
        """Create website backup.
        
        Args:
            id: Website ID
            
        Returns:
            Dict containing operation status and message
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("WebToBackup")
        return self.post_data(endpoint, data)
    
    def delete_backup(self, id: int) -> Dict[str, Any]:
        """Delete website backup.
        
        Args:
            id: Backup ID
            
        Returns:
            Dict containing operation status and message
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("WebDelBackup")
        return self.post_data(endpoint, data)


class Domain(Client):
    """Domain management API."""
    
    def get_domain_list(self, site_id: int) -> List[Dict[str, Any]]:
        """Get list of domains for a website.
        
        Args:
            site_id: Website ID
            
        Returns:
            List of domain dictionaries
        """
        data = {
            "search": site_id,
            "list": True
        }
        endpoint = self.config.get_endpoint("WebDomainList")
        return self.post_data(endpoint, data)
    
    def add_domain(self, id: int, webname: str, domain: str) -> Dict[str, Any]:
        """Add domain to website.
        
        Args:
            id: Website ID
            webname: Website name
            domain: Domain to add (with port if not 80)
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "webname": webname,
            "domain": domain
        }
        endpoint = self.config.get_endpoint("WebAddDomain")
        return self.post_data(endpoint, data)
    
    def delete_domain(self, id: int, webname: str, domain: str, port: int = 80) -> Dict[str, Any]:
        """Delete domain from website.
        
        Args:
            id: Website ID
            webname: Website name
            domain: Domain to delete
            port: Domain port
            
        Returns:
            Dict containing operation status and message
        """
        data = {
            "id": id,
            "webname": webname,
            "domain": domain,
            "port": port
        }
        endpoint = self.config.get_endpoint("WebDelDomain")
        return self.post_data(endpoint, data)


class Rewrite(Client):
    """Rewrite and configuration management API."""
    
    def get_rewrite_list(self, site_name: str) -> Dict[str, List[str]]:
        """Get list of available rewrite rules.
        
        Args:
            site_name: Website name
            
        Returns:
            Dict containing list of rewrite rule names
        """
        data = {"siteName": site_name}
        endpoint = self.config.get_endpoint("GetRewriteList")
        return self.post_data(endpoint, data)
    
    def get_rewrite_content(self, path: str) -> str:
        """Get rewrite rule content.
        
        Args:
            path: Path to rewrite rule file
            
        Returns:
            Rewrite rule content
        """
        data = {"path": path}
        endpoint = self.config.get_endpoint("GetFileBody")
        return self.post_data(endpoint, data)
    
    def save_rewrite_content(self, path: str, content: str) -> Dict[str, Any]:
        """Save rewrite rule content.
        
        Args:
            path: Path to rewrite rule file
            content: Rewrite rule content
            
        Returns:
            Dict containing operation status
        """
        data = {
            "path": path,
            "data": content,
            "encoding": "utf-8"
        }
        endpoint = self.config.get_endpoint("SaveFileBody")
        return self.post_data(endpoint, data)


class Directory(Client):
    """Website directory and runtime configuration API."""
    
    def get_root_path(self, id: int) -> str:
        """Get website root directory.
        
        Args:
            id: Website ID
            
        Returns:
            Website root directory path
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("GetDirUserINI")
        return self.post_data(endpoint, data)
    
    def get_directory_config(self, id: int, path: str) -> Dict[str, Any]:
        """Get directory configuration.
        
        Args:
            id: Website ID
            path: Website root directory
            
        Returns:
            Dict containing directory configuration
        """
        data = {
            "id": id,
            "path": path
        }
        endpoint = self.config.get_endpoint("GetDirUserINI")
        return self.post_data(endpoint, data)
    
    def toggle_cross_site(self, path: str) -> Dict[str, Any]:
        """Toggle cross-site protection.
        
        Args:
            path: Website root directory
            
        Returns:
            Dict containing operation status
        """
        data = {"path": path}
        endpoint = self.config.get_endpoint("SetDirUserINI")
        return self.post_data(endpoint, data)
    
    def toggle_access_log(self, id: int) -> Dict[str, Any]:
        """Toggle access log.
        
        Args:
            id: Website ID
            
        Returns:
            Dict containing operation status
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("LogsOpen")
        return self.post_data(endpoint, data)
    
    def set_root_path(self, id: int, path: str) -> Dict[str, Any]:
        """Set website root directory.
        
        Args:
            id: Website ID
            path: New root directory path
            
        Returns:
            Dict containing operation status
        """
        data = {
            "id": id,
            "path": path
        }
        endpoint = self.config.get_endpoint("SetPath")
        return self.post_data(endpoint, data)
    
    def set_run_path(self, id: int, run_path: str) -> Dict[str, Any]:
        """Set website run directory.
        
        Args:
            id: Website ID
            run_path: Run directory relative to root
            
        Returns:
            Dict containing operation status
        """
        data = {
            "id": id,
            "runPath": run_path
        }
        endpoint = self.config.get_endpoint("SetSiteRunPath")
        return self.post_data(endpoint, data)


class PasswordAccess(Client):
    """Password access control API."""
    
    def set_password_access(self, id: int, username: str, password: str) -> Dict[str, Any]:
        """Set password access for website.
        
        Args:
            id: Website ID
            username: Access username
            password: Access password
            
        Returns:
            Dict containing operation status
        """
        data = {
            "id": id,
            "username": username,
            "password": password
        }
        endpoint = self.config.get_endpoint("SetHasPwd")
        return self.post_data(endpoint, data)
    
    def close_password_access(self, id: int) -> Dict[str, Any]:
        """Close password access for website.
        
        Args:
            id: Website ID
            
        Returns:
            Dict containing operation status
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("CloseHasPwd")
        return self.post_data(endpoint, data)


class TrafficLimit(Client):
    """Traffic limit management API (nginx only)."""
    
    def get_traffic_limit(self, id: int) -> Dict[str, Any]:
        """Get traffic limit configuration.
        
        Args:
            id: Website ID
            
        Returns:
            Dict containing traffic limit configuration
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("GetLimitNet")
        return self.post_data(endpoint, data)
    
    def set_traffic_limit(self, id: int, perserver: int, perip: int,
                         limit_rate: int) -> Dict[str, Any]:
        """Set traffic limit configuration.
        
        Args:
            id: Website ID
            perserver: Concurrent connection limit
            perip: Single IP limit
            limit_rate: Traffic limit (KB/s)
            
        Returns:
            Dict containing operation status
        """
        data = {
            "id": id,
            "perserver": perserver,
            "perip": perip,
            "limit_rate": limit_rate
        }
        endpoint = self.config.get_endpoint("SetLimitNet")
        return self.post_data(endpoint, data)
    
    def close_traffic_limit(self, id: int) -> Dict[str, Any]:
        """Close traffic limit.
        
        Args:
            id: Website ID
            
        Returns:
            Dict containing operation status
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("CloseLimitNet")
        return self.post_data(endpoint, data)


class DefaultDocument(Client):
    """Default document management API."""
    
    def get_default_document(self, id: int) -> Dict[str, Any]:
        """Get default document configuration.
        
        Args:
            id: Website ID
            
        Returns:
            Dict containing default document configuration
        """
        data = {"id": id}
        endpoint = self.config.get_endpoint("WebGetIndex")
        return self.post_data(endpoint, data)
    
    def set_default_document(self, id: int, index: str) -> Dict[str, Any]:
        """Set default document configuration.
        
        Args:
            id: Website ID
            index: Comma-separated list of default documents
            
        Returns:
            Dict containing operation status
        """
        data = {
            "id": id,
            "Index": index
        }
        endpoint = self.config.get_endpoint("WebSetIndex")
        return self.post_data(endpoint, data) 