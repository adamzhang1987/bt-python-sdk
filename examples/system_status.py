#!/usr/bin/env python3
"""
Example demonstrating how to use the System API to get system information and statistics.
"""

import logging
from pybt.api import System

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize the System API
        system_api = System()

        # Get system basic statistics
        logger.info("Getting system total statistics...")
        system_total = system_api.get_system_total()
        logger.info("System Statistics:")
        logger.info(f"Memory Total: {system_total['memTotal']}MB")
        logger.info(f"Memory Free: {system_total['memFree']}MB")
        logger.info(f"Memory Used: {system_total['memRealUsed']}MB")
        logger.info(f"CPU Cores: {system_total['cpuNum']}")
        logger.info(f"CPU Usage: {system_total['cpuRealUsed']}%")
        logger.info(f"System Uptime: {system_total['time']}")
        logger.info(f"System Version: {system_total['system']}")
        logger.info(f"Panel Version: {system_total['version']}")

        # Get disk information
        logger.info("\nGetting disk information...")
        disk_info = system_api.get_disk_info()
        for disk in disk_info:
            logger.info(f"\nDisk: {disk['filesystem']}")
            logger.info(f"Type: {disk['type']}")
            logger.info(f"Mount Point: {disk['path']}")
            logger.info(f"Size: {disk['size'][0]}")
            logger.info(f"Used: {disk['size'][1]}")
            logger.info(f"Available: {disk['size'][2]}")
            logger.info(f"Usage: {disk['size'][3]}")

        # Get network information
        logger.info("\nGetting network information...")
        network_info = system_api.get_network()
        logger.info(f"Network Status: {network_info}")

        # Check for installation tasks
        logger.info("\nChecking for installation tasks...")
        task_count = system_api.get_task_count()
        logger.info(f"Active Tasks: {task_count}")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main() 