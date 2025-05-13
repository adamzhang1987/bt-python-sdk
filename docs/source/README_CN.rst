关于
========

*Pybt* 是一个用于宝塔面板 API 的 Python SDK。它提供了一套全面的工具，用于管理和自动化运行宝塔面板的服务器上的任务。

文档
========
* 详细文档请访问我们的`在线文档 <https://bt-python-sdk.readthedocs.io/en/latest/?>`_

* 官方 API 文档: https://www.bt.cn/api-doc.pdf

安装
========
.. code-block:: bash

   pip install bt-python-sdk

或者

.. code-block:: bash

   git clone https://github.com/adamzhang1987/bt-python-sdk.git
   python setup.py install

配置
========
SDK 使用环境变量进行配置。您可以通过以下两种方式设置：

1. 使用 `.env` 文件（推荐）：
   .. code-block:: bash

      # 在项目根目录创建 .env 文件
      BT_API_KEY="your-api-key"
      BT_PANEL_HOST="http://localhost:8888"
      DEBUG=False
      TIMEOUT=30
      VERIFY_SSL=False

2. 直接设置环境变量：
   .. code-block:: bash

      export BT_API_KEY="your-api-key"
      export BT_PANEL_HOST="http://localhost:8888"
      export DEBUG=False
      export TIMEOUT=30
      export VERIFY_SSL=False

> 注意：`.env` 文件应该添加到 `.gitignore` 中，以保护您的 API 密钥安全。

示例
========

1. 首先，在``面板设置-API接口``中启用 API 接口并获取您的``API密钥``。

2. 启用 API 后，只有白名单中的 IP 才能访问面板 API 接口。

3. 要从本地机器调用面板 API，请将"127.0.0.1"和您的本地 IP 添加到白名单中。

对于 ``BT_PANEL_HOST`` 参数，您只需要提供面板的域名或 IP 加端口，例如 ``http://192.168.1.168:8888``。

.. code:: python

   # 系统状态相关 API
   >>> from pybt.api import System
   >>> system_api = System()  # 将自动使用环境变量

   # 获取系统基本统计信息
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

   # 获取磁盘分区信息
   >>> system_api.get_disk_info()

   [{'filesystem': '/dev/sda6',
    'type': 'ext4',
    'path': '/',
    'size': ['1.1T', '23G', '1005G', '3%'],
    'inodes': ['72089600', '360084', '71729516', '1%']}]

.. code:: python

   # 网站管理相关 API
   >>> from pybt.api import Website, WebsiteBackup, Domain, Rewrite, Directory, PasswordAccess, TrafficLimit, DefaultDocument
   >>> website_api = Website()  # 将自动使用环境变量

   # 获取网站列表
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

   # 获取 PHP 版本信息
   >>> website_api.get_php_versions()

   [{'version': '00', 'name': 'Static'}, {'version': '56', 'name': 'PHP-56'}]

   # 网站备份管理
   >>> backup_api = WebsiteBackup()
   >>> backup_api.get_backup_list(search=5)  # 获取网站 ID 5 的备份列表

   # 域名管理
   >>> domain_api = Domain()
   >>> domain_api.get_domain_list(site_id=5)  # 获取网站 ID 5 的域名列表

   # 目录和配置管理
   >>> dir_api = Directory()
   >>> dir_api.get_root_path(id=5)  # 获取网站 ID 5 的根目录

   # 密码访问控制
   >>> pwd_api = PasswordAccess()
   >>> pwd_api.set_password_access(id=5, username="admin", password="secret")

   # 流量限制管理
   >>> traffic_api = TrafficLimit()
   >>> traffic_api.set_traffic_limit(id=5, perserver=100, perip=10, limit_rate=1024)

   # 默认文档管理
   >>> doc_api = DefaultDocument()
   >>> doc_api.set_default_document(id=5, index="index.php,index.html")

功能特性
============
点击三角形展开查看模块方法。有关详细模块参数，请参阅`在线文档 <https://bt-python-sdk.readthedocs.io/en/latest/?>`_

System: 系统状态相关 API
--------------------------------
* `get_system_total  获取系统基本统计信息`
* `get_disk_info  获取磁盘分区信息`
* `get_network  获取实时状态信息（CPU、内存、网络、负载）`
* `get_task_count  检查安装任务`
* `update_panel  检查面板更新`

Website: 基础网站管理
--------------------------------
* `get_website_list  获取网站列表`
* `get_site_types  获取网站分类`
* `get_php_versions  获取已安装的 PHP 版本列表`
* `create_website  创建网站`
* `delete_website  删除网站`
* `stop_website  停止网站`
* `start_website  启动网站`
* `set_expiry_date  设置网站到期时间`
* `set_website_remark  修改网站备注`

WebsiteBackup: 网站备份管理
--------------------------------
* `get_backup_list  获取网站备份列表`
* `create_backup  创建网站备份`
* `delete_backup  删除网站备份`

Domain: 域名管理
--------------------------------
* `get_domain_list  获取网站域名列表`
* `add_domain  添加网站域名`
* `delete_domain  删除网站域名`

Rewrite: 重写规则和配置管理
--------------------------------
* `get_rewrite_list  获取可用的重写规则`
* `get_rewrite_content  获取重写规则内容`
* `save_rewrite_content  保存重写规则内容`

Directory: 网站目录和运行时配置
--------------------------------
* `get_root_path  获取网站根目录`
* `get_directory_config  获取目录配置`
* `toggle_cross_site  切换跨站保护`
* `toggle_access_log  切换访问日志`
* `set_root_path  设置网站根目录`
* `set_run_path  设置网站运行目录`

PasswordAccess: 密码访问控制
--------------------------------
* `set_password_access  设置网站密码访问`
* `close_password_access  关闭网站密码访问`

TrafficLimit: 流量限制管理
--------------------------------
* `get_traffic_limit  获取流量限制配置`
* `set_traffic_limit  设置流量限制配置`
* `close_traffic_limit  关闭流量限制`

DefaultDocument: 默认文档管理
--------------------------------
* `get_default_document  获取默认文档配置`
* `set_default_document  设置默认文档配置`

测试
========
在运行单元测试之前，在项目根目录创建 `.env` 文件，内容如下：

.. code-block:: bash

   BT_API_KEY="your-api-key"
   BT_PANEL_HOST="http://localhost:8888"
   DEBUG=False
   TIMEOUT=30
   VERIFY_SSL=False

然后运行：

.. code-block:: bash

   # 仅运行单元测试
   pytest

   # 运行单元测试和集成测试
   pytest --run-integration

   # 仅运行集成测试
   pytest -m integration --run-integration

祝您好运！:star:

由 `bt APIs <https://www.bt.cn/bbs/thread-20376-1-1.html>`_ 提供支持 