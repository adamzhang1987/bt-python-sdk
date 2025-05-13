"""Test cases for website-related API classes."""

import os
import pytest
from unittest.mock import patch
from pybt.api.website import (
    Website, WebsiteBackup, Domain, Rewrite, Directory,
    PasswordAccess, TrafficLimit, DefaultDocument
)


@pytest.fixture
def website():
    """Create a Website instance with mocked config."""
    return Website(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def website_backup():
    """Create a WebsiteBackup instance with mocked config."""
    return WebsiteBackup(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def domain():
    """Create a Domain instance with mocked config."""
    return Domain(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def rewrite():
    """Create a Rewrite instance with mocked config."""
    return Rewrite(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def directory():
    """Create a Directory instance with mocked config."""
    return Directory(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def password_access():
    """Create a PasswordAccess instance with mocked config."""
    return PasswordAccess(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def traffic_limit():
    """Create a TrafficLimit instance with mocked config."""
    return TrafficLimit(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def default_document():
    """Create a DefaultDocument instance with mocked config."""
    return DefaultDocument(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


# Skip integration tests if environment variable is not set
def skip_if_no_api_key():
    """Skip test if API key is not set."""
    if not os.getenv('BT_API_KEY') or not os.getenv('BT_PANEL_HOST'):
        pytest.skip("BT_API_KEY and BT_PANEL_HOST environment variables are required")


# Integration test fixtures
@pytest.fixture
def real_website():
    """Create a Website instance with real API credentials."""
    skip_if_no_api_key()
    return Website(
        api_key=os.getenv('BT_API_KEY'),
        bt_panel_host=os.getenv('BT_PANEL_HOST'),
        debug=True,  # Enable debug for real API tests
        timeout=30,
        verify_ssl=False
    )


class TestWebsite:
    """Test cases for Website class."""

    def test_get_website_list(self, website):
        """Test get_website_list method."""
        mock_response = {
            "data": [
                {
                    "status": "1",
                    "ps": "test.com",
                    "domain": 1,
                    "name": "test.com",
                    "addtime": "2024-03-20 10:00:00",
                    "path": "/www/wwwroot/test.com",
                    "backup_count": 0,
                    "edate": "0000-00-00",
                    "id": 1
                }
            ],
            "where": "type_id=0",
            "page": "<div><span class='Pcurrent'>1</span></div>"
        }
        
        with patch.object(website, 'post_data', return_value=mock_response) as mock_post:
            result = website.get_website_list(page=1, limit=15, type_id=0)
            
            assert result == mock_response
            assert len(result["data"]) == 1
            assert result["data"][0]["name"] == "test.com"
            mock_post.assert_called_once_with(
                website.config.get_endpoint("Websites"),
                {"p": 1, "limit": 15, "type": 0, "order": "id desc"}
            )

    def test_get_site_types(self, website):
        """Test get_site_types method."""
        mock_response = [
            {"id": 0, "name": "默认分类"}
        ]
        
        with patch.object(website, 'post_data', return_value=mock_response) as mock_post:
            result = website.get_site_types()
            
            assert result == mock_response
            assert len(result) == 1
            assert result[0]["id"] == 0
            mock_post.assert_called_once_with(website.config.get_endpoint("Webtypes"))

    def test_get_php_versions(self, website):
        """Test get_php_versions method."""
        mock_response = [
            {"version": "00", "name": "纯静态"},
            {"version": "72", "name": "PHP-72"}
        ]
        
        with patch.object(website, 'post_data', return_value=mock_response) as mock_post:
            result = website.get_php_versions()
            
            assert result == mock_response
            assert len(result) == 2
            assert result[0]["version"] == "00"
            mock_post.assert_called_once_with(website.config.get_endpoint("GetPHPVersion"))

    def test_create_website(self, website):
        """Test create_website method."""
        mock_response = {
            "siteStatus": True,
            "ftpStatus": True,
            "ftpUser": "test_com",
            "ftpPass": "password123",
            "databaseStatus": True,
            "databaseUser": "test_com",
            "databasePass": "dbpass123"
        }
        
        webname = {"domain": "test.com", "domainlist": [], "count": 0}
        with patch.object(website, 'post_data', return_value=mock_response) as mock_post:
            result = website.create_website(
                webname=webname,
                path="/www/wwwroot/test.com",
                type_id=0,
                version="72",
                ftp=True,
                ftp_username="test_com",
                ftp_password="password123",
                sql=True,
                datauser="test_com",
                datapassword="dbpass123"
            )
            
            assert result == mock_response
            assert result["siteStatus"] is True
            assert result["ftpStatus"] is True
            assert result["databaseStatus"] is True
            mock_post.assert_called_once()

    def test_delete_website(self, website):
        """Test delete_website method."""
        mock_response = {
            "status": True,
            "msg": "删除成功!"
        }
        
        with patch.object(website, 'post_data', return_value=mock_response) as mock_post:
            result = website.delete_website(
                id=1,
                webname="test.com",
                delete_ftp=True,
                delete_database=True,
                delete_path=True
            )
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                website.config.get_endpoint("WebDeleteSite"),
                {"id": 1, "webname": "test.com", "ftp": 1, "database": 1, "path": 1}
            )


class TestWebsiteBackup:
    """Test cases for WebsiteBackup class."""

    def test_get_backup_list(self, website_backup):
        """Test get_backup_list method."""
        mock_response = {
            "data": [
                {
                    "id": 1,
                    "pid": 1,
                    "name": "test.com",
                    "filename": "test.com_20240320.tar.gz",
                    "addtime": "2024-03-20 10:00:00"
                }
            ],
            "where": "pid=1 and type='0'",
            "page": "<div><span class='Pcurrent'>1</span></div>"
        }
        
        with patch.object(website_backup, 'post_data', return_value=mock_response) as mock_post:
            result = website_backup.get_backup_list(search=1, page=1, limit=5)
            
            assert result == mock_response
            assert len(result["data"]) == 1
            assert result["data"][0]["name"] == "test.com"
            mock_post.assert_called_once_with(
                website_backup.config.get_endpoint("WebBackupList"),
                {"p": 1, "limit": 5, "type": 0, "search": 1}
            )

    def test_create_backup(self, website_backup):
        """Test create_backup method."""
        mock_response = {
            "status": True,
            "msg": "备份成功!"
        }
        
        with patch.object(website_backup, 'post_data', return_value=mock_response) as mock_post:
            result = website_backup.create_backup(id=1)
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                website_backup.config.get_endpoint("WebToBackup"),
                {"id": 1}
            )


class TestDomain:
    """Test cases for Domain class."""

    def test_get_domain_list(self, domain):
        """Test get_domain_list method."""
        mock_response = [
            {
                "port": 80,
                "addtime": "2024-03-20 10:00:00",
                "pid": 1,
                "id": 1,
                "name": "test.com"
            }
        ]
        
        with patch.object(domain, 'post_data', return_value=mock_response) as mock_post:
            result = domain.get_domain_list(site_id=1)
            
            assert result == mock_response
            assert len(result) == 1
            assert result[0]["name"] == "test.com"
            mock_post.assert_called_once_with(
                domain.config.get_endpoint("WebDomainList"),
                {"search": 1, "list": True}
            )

    def test_add_domain(self, domain):
        """Test add_domain method."""
        mock_response = {
            "status": True,
            "msg": "域名添加成功!"
        }
        
        with patch.object(domain, 'post_data', return_value=mock_response) as mock_post:
            result = domain.add_domain(id=1, webname="test.com", domain="sub.test.com")
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                domain.config.get_endpoint("WebAddDomain"),
                {"id": 1, "webname": "test.com", "domain": "sub.test.com"}
            )


class TestRewrite:
    """Test cases for Rewrite class."""

    def test_get_rewrite_list(self, rewrite):
        """Test get_rewrite_list method."""
        mock_response = {
            "rewrite": ["0.当前", "wordpress", "discuz", "typecho"]
        }
        
        with patch.object(rewrite, 'post_data', return_value=mock_response) as mock_post:
            result = rewrite.get_rewrite_list(site_name="test.com")
            
            assert result == mock_response
            assert "wordpress" in result["rewrite"]
            mock_post.assert_called_once_with(
                rewrite.config.get_endpoint("GetRewriteList"),
                {"siteName": "test.com"}
            )

    def test_get_rewrite_content(self, rewrite):
        """Test get_rewrite_content method."""
        mock_response = "location / {\n    try_files $uri $uri/ /index.php?$args;\n}"
        
        with patch.object(rewrite, 'post_data', return_value=mock_response) as mock_post:
            result = rewrite.get_rewrite_content(path="/www/server/panel/vhost/rewrite/nginx/wordpress.conf")
            
            assert result == mock_response
            assert "try_files" in result
            mock_post.assert_called_once_with(
                rewrite.config.get_endpoint("GetFileBody"),
                {"path": "/www/server/panel/vhost/rewrite/nginx/wordpress.conf"}
            )


class TestDirectory:
    """Test cases for Directory class."""

    def test_get_directory_config(self, directory):
        """Test get_directory_config method."""
        mock_response = {
            "pass": False,
            "logs": True,
            "userini": True,
            "runPath": {
                "dirs": ["/"],
                "runPath": "/"
            }
        }
        
        with patch.object(directory, 'post_data', return_value=mock_response) as mock_post:
            result = directory.get_directory_config(id=1, path="/www/wwwroot/test.com")
            
            assert result == mock_response
            assert result["logs"] is True
            assert result["userini"] is True
            mock_post.assert_called_once_with(
                directory.config.get_endpoint("GetDirUserINI"),
                {"id": 1, "path": "/www/wwwroot/test.com"}
            )

    def test_toggle_cross_site(self, directory):
        """Test toggle_cross_site method."""
        mock_response = {"status": True}
        
        with patch.object(directory, 'post_data', return_value=mock_response) as mock_post:
            result = directory.toggle_cross_site(path="/www/wwwroot/test.com")
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                directory.config.get_endpoint("SetDirUserINI"),
                {"path": "/www/wwwroot/test.com"}
            )


class TestPasswordAccess:
    """Test cases for PasswordAccess class."""

    def test_set_password_access(self, password_access):
        """Test set_password_access method."""
        mock_response = {"status": True}
        
        with patch.object(password_access, 'post_data', return_value=mock_response) as mock_post:
            result = password_access.set_password_access(
                id=1,
                username="test",
                password="password123"
            )
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                password_access.config.get_endpoint("SetHasPwd"),
                {"id": 1, "username": "test", "password": "password123"}
            )


class TestTrafficLimit:
    """Test cases for TrafficLimit class."""

    def test_set_traffic_limit(self, traffic_limit):
        """Test set_traffic_limit method."""
        mock_response = {"status": True}
        
        with patch.object(traffic_limit, 'post_data', return_value=mock_response) as mock_post:
            result = traffic_limit.set_traffic_limit(
                id=1,
                perserver=300,
                perip=25,
                limit_rate=512
            )
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                traffic_limit.config.get_endpoint("SetLimitNet"),
                {"id": 1, "perserver": 300, "perip": 25, "limit_rate": 512}
            )


class TestDefaultDocument:
    """Test cases for DefaultDocument class."""

    def test_set_default_document(self, default_document):
        """Test set_default_document method."""
        mock_response = {"status": True}
        
        with patch.object(default_document, 'post_data', return_value=mock_response) as mock_post:
            result = default_document.set_default_document(
                id=1,
                index="index.php,index.html,index.htm"
            )
            
            assert result == mock_response
            assert result["status"] is True
            mock_post.assert_called_once_with(
                default_document.config.get_endpoint("WebSetIndex"),
                {"id": 1, "Index": "index.php,index.html,index.htm"}
            )


# Integration test class
class TestWebsiteIntegration:
    """Integration tests for Website class using real API."""

    @pytest.mark.integration
    def test_get_website_list_real(self, real_website):
        """Test get_website_list method with real API."""
        result = real_website.get_website_list(page=1, limit=15)
        
        # Basic structure validation
        assert isinstance(result, dict)
        assert "data" in result
        assert isinstance(result["data"], list)
        
        # If there are websites, validate their structure
        if result["data"]:
            website = result["data"][0]
            assert "id" in website
            assert "name" in website
            assert "path" in website
            assert "status" in website 