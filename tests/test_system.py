"""Test cases for System API class."""

import os
import pytest
from unittest.mock import patch
from pybt.api.system import System


@pytest.fixture
def system():
    """Create a System instance with mocked config."""
    return System(
        api_key="test_api_key",
        bt_panel_host="http://test.example.com",
        debug=False,
        timeout=30,
        verify_ssl=False
    )


@pytest.fixture
def mock_response():
    """Create a mock response for system total."""
    return {
        "system": "CentOS Linux 7.5.1804 (Core)",
        "version": "6.8.2",
        "time": "0天23小时45分钟",
        "cpuNum": 2,
        "cpuRealUsed": 2.01,
        "memTotal": 1024,
        "memRealUsed": 300,
        "memFree": 724,
        "memCached": 700,
        "memBuffers": 100
    }


@pytest.fixture
def mock_disk_info():
    """Create a mock response for disk info."""
    return [
        {
            "path": "/",
            "inodes": ["8675328", "148216", "8527112", "2%"],
            "size": ["8.3G", "4.0G", "4.3G", "49%"]
        },
        {
            "path": "/www",
            "inodes": ["655360", "295093", "360267", "46%"],
            "size": ["9.8G", "3.7G", "5.6G", "40%"]
        }
    ]


@pytest.fixture
def mock_network():
    """Create a mock response for network info."""
    return {
        "downTotal": 446326699,
        "upTotal": 77630707,
        "downPackets": 1519428,
        "upPackets": 175326,
        "down": 36.22,
        "up": 72.81,
        "cpu": [1.87, 6],
        "mem": {
            "memFree": 189,
            "memTotal": 1741,
            "memCached": 722,
            "memBuffers": 139,
            "memRealUsed": 691
        },
        "load": {
            "max": 12,
            "safe": 9.0,
            "one": 0.01,
            "five": 0.02,
            "limit": 12,
            "fifteen": 0.05
        }
    }


# Skip integration tests if environment variable is not set
def skip_if_no_api_key():
    """Skip test if API key is not set."""
    if not os.getenv('BT_API_KEY') or not os.getenv('BT_PANEL_HOST'):
        pytest.skip("BT_API_KEY and BT_PANEL_HOST environment variables are required")


# Integration test fixtures
@pytest.fixture
def real_system():
    """Create a System instance with real API credentials."""
    skip_if_no_api_key()
    return System(
        api_key=os.getenv('BT_API_KEY'),
        bt_panel_host=os.getenv('BT_PANEL_HOST'),
        debug=True,  # Enable debug for real API tests
        timeout=30,
        verify_ssl=False
    )


class TestSystem:
    """Test cases for System class."""

    def test_get_system_total(self, system, mock_response):
        """Test get_system_total method."""
        with patch.object(system, 'post_data', return_value=mock_response):
            result = system.get_system_total()
            
            assert result == mock_response
            assert result["system"] == "CentOS Linux 7.5.1804 (Core)"
            assert result["version"] == "6.8.2"
            assert result["cpuNum"] == 2
            assert result["memTotal"] == 1024
            system.post_data.assert_called_once_with(system.config.get_endpoint("GetSystemTotal"))

    def test_get_disk_info(self, system, mock_disk_info):
        """Test get_disk_info method."""
        with patch.object(system, 'post_data', return_value=mock_disk_info):
            result = system.get_disk_info()
            
            assert result == mock_disk_info
            assert len(result) == 2
            assert result[0]["path"] == "/"
            assert result[1]["path"] == "/www"
            assert "inodes" in result[0]
            assert "size" in result[0]
            system.post_data.assert_called_once_with(system.config.get_endpoint("GetDiskInfo"))

    def test_get_network(self, system, mock_network):
        """Test get_network method."""
        with patch.object(system, 'post_data', return_value=mock_network):
            result = system.get_network()
            
            assert result == mock_network
            assert "cpu" in result
            assert "mem" in result
            assert "load" in result
            assert result["down"] == 36.22
            assert result["up"] == 72.81
            assert result["cpu"][0] == 1.87
            assert result["cpu"][1] == 6
            system.post_data.assert_called_once_with(system.config.get_endpoint("GetNetWork"))

    def test_get_task_count(self, system):
        """Test get_task_count method."""
        with patch.object(system, 'post_data', return_value=0):
            result = system.get_task_count()
            
            assert result == 0
            system.post_data.assert_called_once_with(system.config.get_endpoint("GetTaskCount"))

    def test_update_panel_check(self, system):
        """Test update_panel method with check parameter."""
        mock_response = {
            "status": True,
            "version": "6.8.2",
            "updateMsg": "升级说明"
        }
        with patch.object(system, 'post_data', return_value=mock_response) as mock_post:
            result = system.update_panel(check=True)
            
            assert result == mock_response
            assert result["status"] is True
            assert result["version"] == "6.8.2"
            mock_post.assert_called_once_with(
                system.config.get_endpoint("UpdatePanel"),
                {"check": True}
            )

    def test_update_panel_force(self, system):
        """Test update_panel method with force parameter."""
        mock_response = {
            "status": True,
            "version": "6.8.2",
            "updateMsg": "升级说明"
        }
        with patch.object(system, 'post_data', return_value=mock_response) as mock_post:
            result = system.update_panel(force=True)
            
            assert result == mock_response
            assert result["status"] is True
            assert result["version"] == "6.8.2"
            mock_post.assert_called_once_with(
                system.config.get_endpoint("UpdatePanel"),
                {"force": True}
            )

    def test_update_panel_both_params(self, system):
        """Test update_panel method with both check and force parameters."""
        mock_response = {
            "status": True,
            "version": "6.8.2",
            "updateMsg": "升级说明"
        }
        with patch.object(system, 'post_data', return_value=mock_response) as mock_post:
            result = system.update_panel(check=True, force=True)
            
            assert result == mock_response
            assert result["status"] is True
            assert result["version"] == "6.8.2"
            mock_post.assert_called_once_with(
                system.config.get_endpoint("UpdatePanel"),
                {"check": True, "force": True}
            )


class TestSystemIntegration:
    """Integration tests for System class using real API."""

    @pytest.mark.integration
    def test_get_system_total_real(self, real_system):
        """Test get_system_total method with real API."""
        result = real_system.get_system_total()
        
        # Basic structure validation
        assert isinstance(result, dict)
        assert "system" in result
        assert "version" in result
        assert "cpuNum" in result
        assert "memTotal" in result
        assert "memRealUsed" in result
        assert "memFree" in result
        assert "memCached" in result
        assert "memBuffers" in result
        
        # Type validation
        assert isinstance(result["cpuNum"], int)
        assert isinstance(result["memTotal"], int)
        assert isinstance(result["memRealUsed"], (int, float))
        assert isinstance(result["memFree"], int)
        assert isinstance(result["memCached"], int)
        assert isinstance(result["memBuffers"], int)

    @pytest.mark.integration
    def test_get_disk_info_real(self, real_system):
        """Test get_disk_info method with real API."""
        result = real_system.get_disk_info()
        
        # Basic structure validation
        assert isinstance(result, list)
        assert len(result) > 0
        
        # Validate first disk entry
        disk = result[0]
        assert "path" in disk
        assert "inodes" in disk
        assert "size" in disk
        assert isinstance(disk["inodes"], list)
        assert isinstance(disk["size"], list)
        assert len(disk["inodes"]) == 4  # [total, used, free, usage%]

    @pytest.mark.integration
    def test_get_network_real(self, real_system):
        """Test get_network method with real API."""
        result = real_system.get_network()
        
        # Basic structure validation
        assert isinstance(result, dict)
        assert "downTotal" in result
        assert "upTotal" in result
        assert "down" in result
        assert "up" in result
        assert "cpu" in result
        assert "mem" in result
        assert "load" in result
        
        # Type validation
        assert isinstance(result["downTotal"], int)
        assert isinstance(result["upTotal"], int)
        assert isinstance(result["down"], (int, float))
        assert isinstance(result["up"], (int, float))
        assert isinstance(result["cpu"], list)
        assert isinstance(result["mem"], dict)
        assert isinstance(result["load"], dict)
        
        # Memory structure validation
        mem = result["mem"]
        assert "memFree" in mem
        assert "memTotal" in mem
        assert "memCached" in mem
        assert "memBuffers" in mem
        assert "memRealUsed" in mem
        
        # Load structure validation
        load = result["load"]
        assert "max" in load
        assert "safe" in load
        assert "one" in load
        assert "five" in load
        assert "fifteen" in load

    @pytest.mark.integration
    def test_get_task_count_real(self, real_system):
        """Test get_task_count method with real API."""
        result = real_system.get_task_count()
        
        # Basic validation
        assert isinstance(result, int)
        assert result >= 0  # Task count should never be negative 