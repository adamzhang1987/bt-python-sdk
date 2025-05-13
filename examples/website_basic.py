#!/usr/bin/env python3
"""
Example demonstrating how to use the Website API for basic website operations.
"""

import logging
from pybt.api import Website

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize the Website API
        website_api = Website()

        # Get website list
        logger.info("Getting website list...")
        websites = website_api.get_website_list()
        logger.info(f"Found {len(websites['data'])} websites:")
        for site in websites['data']:
            logger.info(f"\nWebsite: {site['name']}")
            logger.info(f"ID: {site['id']}")
            logger.info(f"Path: {site['path']}")
            logger.info(f"Status: {'Running' if site['status'] == '1' else 'Stopped'}")
            logger.info(f"PHP Version: {site['php_version']}")
            logger.info(f"Domains: {site['domain']}")

        # Get available site types
        logger.info("\nGetting available site types...")
        site_types = website_api.get_site_types()
        logger.info("Available site types:")
        for site_type in site_types:
            logger.info(f"- {site_type}")

        # Get PHP versions
        logger.info("\nGetting available PHP versions...")
        php_versions = website_api.get_php_versions()
        logger.info("Available PHP versions:")
        for version in php_versions:
            logger.info(f"- {version['name']} (version: {version['version']})")

        # Example: Create a new website
        # Uncomment and modify these lines to create a website
        """
        logger.info("\nCreating new website...")
        new_site = website_api.create_website(
            name="example.com",
            path="/www/wwwroot/example.com",
            php_version="74",
            port=80,
            ssl=0
        )
        logger.info(f"Created website: {new_site}")
        """

        # Example: Stop a website
        # Uncomment and modify these lines to stop a website
        """
        site_id = 1  # Replace with actual website ID
        logger.info(f"\nStopping website ID {site_id}...")
        stop_result = website_api.stop_website(site_id)
        logger.info(f"Stop result: {stop_result}")
        """

        # Example: Start a website
        # Uncomment and modify these lines to start a website
        """
        site_id = 1  # Replace with actual website ID
        logger.info(f"\nStarting website ID {site_id}...")
        start_result = website_api.start_website(site_id)
        logger.info(f"Start result: {start_result}")
        """

        # Example: Delete a website
        # Uncomment and modify these lines to delete a website
        """
        site_id = 1  # Replace with actual website ID
        logger.info(f"\nDeleting website ID {site_id}...")
        delete_result = website_api.delete_website(site_id)
        logger.info(f"Delete result: {delete_result}")
        """

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main() 