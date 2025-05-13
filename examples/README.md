# Examples

This directory contains example code demonstrating how to use the BT Python SDK. Each example focuses on a specific aspect of the API.

## Prerequisites

Before running the examples, make sure you have:

1. Installed the SDK:
   ```bash
   pip install bt-python-sdk
   ```

2. Created a `.env` file in your project root with your BT Panel credentials:
   ```bash
   BT_API_KEY="your-api-key"
   BT_PANEL_HOST="http://localhost:8888"
   DEBUG=False
   TIMEOUT=30
   VERIFY_SSL=False
   ```

## Available Examples

### System Management
- `system_status.py`: Demonstrates how to get system information and statistics
- `system_disk.py`: Shows how to manage disk information and monitor disk usage

### Website Management
- `website_basic.py`: Basic website operations (create, list, delete)
- `website_backup.py`: Website backup operations
- `website_domain.py`: Domain management for websites
- `website_config.py`: Website configuration management (PHP version, SSL, etc.)

### Advanced Features
- `website_security.py`: Security features (password protection, traffic limits)
- `website_rewrite.py`: URL rewrite rules management
- `website_directory.py`: Website directory and path management

## Running Examples

To run an example:

```bash
python examples/system_status.py
```

## Notes

- All examples include error handling and logging
- Examples use environment variables for configuration
- Each example is self-contained and can be run independently
- Comments are provided to explain the code and API usage
