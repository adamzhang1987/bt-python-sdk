#!/usr/bin/env python3
"""
Example demonstrating advanced website management operations including domain management,
directory configuration, password protection, traffic limits, and default documents.
"""

import logging
from pybt.api import (
    Website, Domain, Rewrite, Directory,
    PasswordAccess, TrafficLimit, DefaultDocument
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize APIs
        website_api = Website()
        domain_api = Domain()
        rewrite_api = Rewrite()
        directory_api = Directory()
        password_api = PasswordAccess()
        traffic_api = TrafficLimit()
        default_doc_api = DefaultDocument()

        logger.info(f"rewrite_api: {rewrite_api}")
        logger.info(f"directory_api: {directory_api}")
        logger.info(f"password_api: {password_api}")
        logger.info(f"traffic_api: {traffic_api}")
        logger.info(f"default_doc_api: {default_doc_api}")

        # Get website list
        logger.info("Getting website list...")
        websites = website_api.get_website_list()
        if not websites['data']:
            logger.info("No websites found")
            return

        # Use the first website for examples
        site = websites['data'][0]
        site_id = site['id']
        logger.info(f"\nUsing website: {site['name']} (ID: {site_id})")

        # Domain Management
        logger.info("\n=== Domain Management ===")
        domains = domain_api.get_domain_list(site_id)
        logger.info(f"Current domains: {domains['data']}")

        # Example: Add a new domain
        # Uncomment and modify these lines to add a domain
        """
        new_domain = "example.com"
        logger.info(f"\nAdding domain: {new_domain}")
        add_result = domain_api.add_domain(site_id, new_domain)
        logger.info(f"Add domain result: {add_result}")
        """

        # Directory Configuration
        logger.info("\n=== Directory Configuration ===")
        dir_config = directory_api.get_directory_config(site_id)
        logger.info(f"Current directory config: {dir_config}")

        # Example: Toggle cross-site access
        # Uncomment and modify these lines to toggle cross-site access
        """
        logger.info("\nToggling cross-site access...")
        toggle_result = directory_api.toggle_cross_site(site_id)
        logger.info(f"Toggle result: {toggle_result}")
        """

        # Password Protection
        logger.info("\n=== Password Protection ===")
        # Example: Set password access
        # Uncomment and modify these lines to set password protection
        """
        username = "admin"
        password = "secure_password"
        logger.info(f"\nSetting password protection for user: {username}")
        password_result = password_api.set_password_access(site_id, username, password)
        logger.info(f"Password protection result: {password_result}")
        """

        # Traffic Limits
        logger.info("\n=== Traffic Limits ===")
        # Example: Set traffic limit
        # Uncomment and modify these lines to set traffic limit
        """
        limit = 1024  # 1GB in MB
        logger.info(f"\nSetting traffic limit to {limit}MB")
        traffic_result = traffic_api.set_traffic_limit(site_id, limit)
        logger.info(f"Traffic limit result: {traffic_result}")
        """

        # Default Documents
        logger.info("\n=== Default Documents ===")
        # Example: Set default document
        # Uncomment and modify these lines to set default document
        """
        default_doc = "index.php"
        logger.info(f"\nSetting default document to: {default_doc}")
        doc_result = default_doc_api.set_default_document(site_id, default_doc)
        logger.info(f"Default document result: {doc_result}")
        """

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main() 