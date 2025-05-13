About
=========

*Pybt* is a Python SDK for the BT Panel API. It provides a comprehensive set of tools for managing and automating tasks on servers running the BaoTa Panel.

> This SDK was developed to address the challenges of managing multiple servers running BaoTa Panel. As the number of servers grew, manual maintenance became increasingly difficult. The SDK enables the creation of a unified operations platform to monitor server status and perform routine maintenance tasks.

Documentation
================
* For detailed documentation, please visit our `online documentation <https://bt-python-sdk.readthedocs.io/en/latest/?>`_

* Official API Documentation: https://www.bt.cn/api-doc.pdf

Installation
================
.. code-block:: bash

   pip install bt-python-sdk

or

.. code-block:: bash

   git clone https://github.com/adamzhang1987/bt-python-sdk.git
   python setup.py install

Configuration
================
The SDK uses environment variables for configuration. You can set these up in two ways:

1. Using a `.env` file (recommended):

.. code-block:: bash

   # Create a .env file in your project root
   BT_API_KEY="your-api-key"
   BT_PANEL_HOST="http://localhost:8888"
   DEBUG=False
   TIMEOUT=30
   VERIFY_SSL=False

1. Setting environment variables directly:

.. code-block:: bash

   export BT_API_KEY="your-api-key"
   export BT_PANEL_HOST="http://localhost:8888"
   export DEBUG=False
   export TIMEOUT=30
   export VERIFY_SSL=False

> Note: The `.env` file should be added to your `.gitignore` to keep your API key secure.

Examples
================

1. First, enable the API interface in ``Panel Settings-API Interface`` and obtain your ``API Key``.

2. After enabling the API, only IPs in the whitelist can access the panel API interface.

3. To call the panel API from your local machine, add "127.0.0.1" and your local IP to the whitelist.

For the ``BT_PANEL_HOST`` parameter, you only need to provide the panel's domain or IP with port, e.g., ``http://192.168.1.168:8888``.

.. code:: python

   # System status related APIs
   >>> from pybt.api import System
   >>> system_api = System()  # Will automatically use environment variables

   # Get system basic statistics
   >>> system_api.get_system_total()

   {'memTotal': 31700,
    'memFree': 18403,
    'memBuffers': 1020,
    'memCached': 8444,
    'memRealUsed': 3833,
    'cpuNum': 12,
    'cpuRealUsed': 4.9,
    'time': '36 days',
    'system': 'Ubuntu 20.04.3 LTS x86_64(Py3.7.9)',
    'isuser': 0,
    'isport': True,
    'version': '7.7.0'}

   # Get disk partition information
   >>> system_api.get_disk_info()

   [{'filesystem': '/dev/sda6',
    'type': 'ext4',
    'path': '/',
    'size': ['1.1T', '23G', '1005G', '3%'],
    'inodes': ['72089600', '360084', '71729516', '1%']}]

.. code:: python

   # Website management related APIs
   >>> from pybt.api import Website, WebsiteBackup, Domain, Rewrite, Directory, PasswordAccess, TrafficLimit, DefaultDocument
   >>> website_api = Website()  # Will automatically use environment variables

   # Get website list
   >>> website_api.get_website_list()

   {'where': '',
    'page': "<div><span class='Pcurrent'>1</span><span class='Pcount'>Total: 1</span></div>",
    'data': [{'id': 5,
      'name': '10.10.11.181',
      'path': '/www/wwwroot/webSiteDir',
      'status': '1',
      'ps': '10_10_11_181',
      'addtime': '2021-06-12 22:57:32',
      'edate': '0000-00-00',
      'backup_count': 0,
      'domain': 2,
      'ssl': {'issuer': 'R3',
       'notAfter': '2022-03-09',
       'notBefore': '2021-12-09',
       'dns': ['*.*.com'],
       'subject': '*.*.com',
       'endtime': 73},
     'php_version': 'Static'}]}

   # Get PHP version information
   >>> website_api.get_php_versions()

   [{'version': '00', 'name': 'Static'}, {'version': '56', 'name': 'PHP-56'}]

   # Website backup management
   >>> backup_api = WebsiteBackup()
   >>> backup_api.get_backup_list(search=5)  # Get backups for website ID 5

   # Domain management
   >>> domain_api = Domain()
   >>> domain_api.get_domain_list(site_id=5)  # Get domains for website ID 5

   # Directory and configuration management
   >>> dir_api = Directory()
   >>> dir_api.get_root_path(id=5)  # Get root path for website ID 5

   # Password access control
   >>> pwd_api = PasswordAccess()
   >>> pwd_api.set_password_access(id=5, username="admin", password="secret")

   # Traffic limit management
   >>> traffic_api = TrafficLimit()
   >>> traffic_api.set_traffic_limit(id=5, perserver=100, perip=10, limit_rate=1024)

   # Default document management
   >>> doc_api = DefaultDocument()
   >>> doc_api.set_default_document(id=5, index="index.php,index.html")

Features
============
Click the triangle to expand and view module methods. For detailed module parameters, see the `online documentation <https://bt-python-sdk.readthedocs.io/en/latest/?>`_

System: System Status Related APIs
--------------------------------------
* `get_system_total  Get system basic statistics`
* `get_disk_info  Get disk partition information`
* `get_network  Get real-time status information (CPU, memory, network, load)`
* `get_task_count  Check for installation tasks`
* `update_panel  Check panel updates`

Website: Basic Website Management
-------------------------------------
* `get_website_list  Get website list`
* `get_site_types  Get website categories`
* `get_php_versions  Get installed PHP version list`
* `create_website  Create website`
* `delete_website  Delete website`
* `stop_website  Stop website`
* `start_website  Start website`
* `set_expiry_date  Set website expiration date`
* `set_website_remark  Modify website remarks`

WebsiteBackup: Website Backup Management
-------------------------------------------
* `get_backup_list  Get website backup list`
* `create_backup  Create website backup`
* `delete_backup  Delete website backup`

Domain: Domain Management
--------------------------------
* `get_domain_list  Get website domain list`
* `add_domain  Add website domain`
* `delete_domain  Delete website domain`

Rewrite: Rewrite and Configuration Management
-------------------------------------------------
* `get_rewrite_list  Get available rewrite rules`
* `get_rewrite_content  Get rewrite rule content`
* `save_rewrite_content  Save rewrite rule content`

Directory: Website Directory and Runtime Configuration
-------------------------------------------------------
* `get_root_path  Get website root directory`
* `get_directory_config  Get directory configuration`
* `toggle_cross_site  Toggle cross-site protection`
* `toggle_access_log  Toggle access log`
* `set_root_path  Set website root directory`
* `set_run_path  Set website run directory`

PasswordAccess: Password Access Control
-----------------------------------------
* `set_password_access  Set password access for website`
* `close_password_access  Close password access for website`

TrafficLimit: Traffic Limit Management
----------------------------------------
* `get_traffic_limit  Get traffic limit configuration`
* `set_traffic_limit  Set traffic limit configuration`
* `close_traffic_limit  Close traffic limit`

DefaultDocument: Default Document Management
---------------------------------------------------
* `get_default_document  Get default document configuration`
* `set_default_document  Set default document configuration`

Testing
================
Before running unit tests, create a `.env` file in the project root with the following content:

.. code-block:: bash

   BT_API_KEY="your-api-key"
   BT_PANEL_HOST="http://localhost:8888"
   DEBUG=False
   TIMEOUT=30
   VERIFY_SSL=False

Then run:

.. code-block:: bash

   # Run unit tests only
   pytest

   # Run both unit and integration tests
   pytest --run-integration

   # Run only integration tests
   pytest -m integration --run-integration

Good luck! :star:

Powered by `bt APIs <https://www.bt.cn/bbs/thread-20376-1-1.html>`_
