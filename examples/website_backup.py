#!/usr/bin/env python3
"""
Example demonstrating how to use the WebsiteBackup API for managing website backups.
"""

import logging
from pybt.api import WebsiteBackup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize the WebsiteBackup API
        backup_api = WebsiteBackup()

        # Get backup list for a specific website
        site_id = 1  # Replace with actual website ID
        logger.info(f"Getting backup list for website ID {site_id}...")
        backups = backup_api.get_backup_list(search=site_id)
        logger.info(f"Found {len(backups['data'])} backups:")
        for backup in backups['data']:
            logger.info(f"\nBackup: {backup['name']}")
            logger.info(f"Size: {backup['size']}")
            logger.info(f"Created: {backup['addtime']}")
            logger.info(f"Type: {backup['type']}")

        # Example: Create a new backup
        # Uncomment and modify these lines to create a backup
        """
        logger.info(f"\nCreating backup for website ID {site_id}...")
        backup_result = backup_api.create_backup(site_id)
        logger.info(f"Backup creation result: {backup_result}")
        """

        # Example: Delete a backup
        # Uncomment and modify these lines to delete a backup
        """
        backup_id = 1  # Replace with actual backup ID
        logger.info(f"\nDeleting backup ID {backup_id}...")
        delete_result = backup_api.delete_backup(backup_id)
        logger.info(f"Delete result: {delete_result}")
        """

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main() 