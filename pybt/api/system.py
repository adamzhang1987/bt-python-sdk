"""System management API."""

from typing import Dict, Any, List
from ..core.client import Client
from pybt.utils.logger import logger


class System(Client):
    """System management API class.
    
    This class provides methods for managing system status, disk information,
    network status, and panel updates.
    """
    
    def get_system_total(self) -> Dict[str, Any]:
        """Get basic system statistics.
        
        Returns:
            Dict containing system statistics:
            - system: Operating system information
            - version: Panel version
            - time: Time since last boot
            - cpuNum: Number of CPU cores
            - cpuRealUsed: CPU usage percentage
            - memTotal: Total physical memory (MB)
            - memRealUsed: Used physical memory (MB)
            - memFree: Available physical memory (MB)
            - memCached: Cached memory (MB)
            - memBuffers: System buffer (MB)
        """
        logger.debug("Getting system total statistics")
        endpoint = self.config.get_endpoint("GetSystemTotal")
        return self.post_data(endpoint)

    def get_disk_info(self) -> List[Dict[str, Any]]:
        """Get disk partition information.
        
        Returns:
            List of dictionaries containing disk information for each partition:
            - path: Partition mount point
            - inodes: List of inode information [total, used, available, usage%]
            - size: List of size information [total, used, available, usage%]
        """
        logger.debug("Getting disk information")
        endpoint = self.config.get_endpoint("GetDiskInfo")
        return self.post_data(endpoint)

    def get_network(self) -> Dict[str, Any]:
        """Get real-time status information (CPU, memory, network, load).
        
        Returns:
            Dict containing real-time system status:
            - downTotal: Total received bytes
            - upTotal: Total sent bytes
            - downPackets: Total received packets
            - upPackets: Total sent packets
            - down: Downstream traffic (KB)
            - up: Upstream traffic (KB)
            - cpu: List of CPU info [usage%, core count]
            - mem: Dict of memory info
                - memFree: Free memory
                - memTotal: Total memory
                - memCached: Cached memory
                - memBuffers: Buffer memory
                - memRealUsed: Actually used memory
            - load: Dict of load info
                - max: Maximum load
                - safe: Safe load threshold
                - one: 1-minute load average
                - five: 5-minute load average
                - limit: Load limit
                - fifteen: 15-minute load average
        """
        logger.debug("Getting network and system status")
        endpoint = self.config.get_endpoint("GetNetWork")
        return self.post_data(endpoint)

    def get_task_count(self) -> int:
        """Check for installation tasks.
        
        Returns:
            int: Number of pending installation tasks (0 if none)
        """
        logger.debug("Checking for installation tasks")
        endpoint = self.config.get_endpoint("GetTaskCount")
        return self.post_data(endpoint)

    def update_panel(self, check: bool = False, force: bool = False) -> Dict[str, Any]:
        """Check for panel updates.
        
        Args:
            check: Force check for updates
            force: Execute update if available
            
        Returns:
            Dict containing update information:
            - status: Update status (true/false)
            - version: Latest version number
            - updateMsg: Update description
        """
        logger.debug("Checking for panel updates")
        endpoint = self.config.get_endpoint("UpdatePanel")
        data = {}
        if check:
            data['check'] = True
        if force:
            data['force'] = True
        return self.post_data(endpoint, data)