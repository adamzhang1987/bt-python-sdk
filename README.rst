About
=====

**Pybt** is a BaoTa panel python sdk.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Pybt** 是一个宝塔面板API的Python版本sdk封装库。
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Examples
========

1.首先需要在 ``面板设置-API接口`` 中打开API接口，获取 ``接口秘钥`` 。
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.开启API后，必需在IP白名单列表中的IP才能访问面板API接口。
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.如需本机调用面板API密钥，请添加“127.0.0.1”和本机IP至IP白名单。
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   接口初始化\ ``YOUR_PANEL_ADDRESS``\ 参数不需要安全入口，只需要填写面板的域名或IP加端口即可，如:
   ``http://192.168.1.168:8888``\ 。

.. code:: python

   # 系统状态相关接口api
   >>> from pybt.system import System
   >>> system_api = System(YOUR_PANEL_ADDRESS, YOUR_API_KEY)

   # 获取系统基础统计
   >>> system_api.get_system_total()

   {'memTotal': 31700,
    'memFree': 18403,
    'memBuffers': 1020,
    'memCached': 8444,
    'memRealUsed': 3833,
    'cpuNum': 12,
    'cpuRealUsed': 4.9,
    'time': '36天',
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

   # 网站管理相关接口
   >>> from pybt.sites import Sites
   >>> sites_api = Sites(YOUR_PANEL_ADDRESS, YOUR_API_KEY)

   # 获取网站列表
   >>> sites_api.websites()

   {'where': '',
    'page': "<div><span class='Pcurrent'>1</span><span class='Pcount'>共1条</span></div>",
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
     'php_version': '静态'}]}

   # 获取PHP版本信息
   >>> sites_api.get_php_version()

   [{'version': '00', 'name': '纯静态'}, {'version': '56', 'name': 'PHP-56'}]

   # 获取网站SSL详情, YOUR_SITES_NAME通过websites接口获取
   >>> sites_api.get_ssl(YOUR_SITES_NAME)

   {'status': True,
    'oid': -1,
    'domain': [{'name': '10.10.11.181'}, {'name': '127.0.0.1'}],
    'key': YOUR_KEY,
    'csr': YOUR_CSR,
    'type': 1,
    'httpTohttps': False,
    'cert_data': {'subject': '*.*.com',
     'notAfter': '2022-03-09',
     'notBefore': '2021-12-09',
     'issuer': "Let's Encrypt",
     'dns': ['*.*.com']},
    'email': 'test@message.com',
    'index': '142e5275a456ecd7bf32bda98528375c',
    'auth_type': 'http'}

.. code:: python

   # FTP管理相关接口
   >>> from pybt.ftp import Ftp
   >>> ftp_api = Ftp(YOUR_PANEL_ADDRESS, YOUR_API_KEY)
   # 获取FTP信息列表
   >>> ftp_api.web_ftp_list()

   {'where': '',
    'page': "<div><span class='Pcurrent'>1</span><span class='Pcount'>共1条</span></div>",
    'data': [{'id': 1,
      'pid': 0,
      'name': 'web_user',
      'password': 'web_user_password',
      'status': '1',
      'ps': 'web_user',
      'addtime': '2021-10-25 10:48:35',
      'path': '/www/wwwroot/web_user'}]}

.. code:: python

   # 数据库管理
   >>> from pybt.dbm import DBM
   >>> dbm_api = DBM(YOUR_PANEL_ADDRESS, YOUR_API_KEY)
   # 获取数据库信息列表
   >>> dbm_api.web_db_list()

   {'where': '',
    'page': "<div><span class='Pcurrent'>1</span><span class='Pcount'>共1条</span></div>",
    'data': [{'id': 1,
      'pid': 0,
      'name': 'test_site_db',
      'username': 'test_site_db',
      'password': 'test_site_db_password',
      'accept': '127.0.0.1',
      'ps': 'test_site_db',
      'addtime': '2021-10-25 10:53:15',
      'backup_count': 0}]}

.. code:: python

   # 插件管理
   >>> from pybt.plugin import Plugin
   >>> plugin_api = Plugin((YOUR_PANEL_ADDRESS, YOUR_API_KEY)
   # 宝塔一键部署执行
   >>> plugin_api.setup_package(dname, site_name, php_version)
