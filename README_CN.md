[![Documentation Status](https://readthedocs.org/projects/bt-python-sdk/badge/?version=latest)](https://bt-python-sdk.readthedocs.io/en/latest/?badge=latest)
# About

#### **Pybt** is a BaoTa panel python sdk. 
##
#### **Pybt** 是一个宝塔面板API的Python版本sdk封装库。


# Documentation

* 详见 <a href="https://bt-python-sdk.readthedocs.io/en/latest/?">在线文档/</a>

* 官方API文档： https://www.bt.cn/api-doc.pdf

# Installation
```bash
pip install bt-python-sdk
```
#### or
```bash
git clone https://github.com/adamzhang1987/bt-python-sdk.git
python setup.py install
```

# 配置
SDK使用环境变量进行配置。您可以通过以下两种方式设置：

1. 使用 `.env` 文件（推荐）：
   ```bash
   # 在项目根目录创建 .env 文件
   BT_API_KEY="your-api-key"
   BT_PANEL_HOST="http://localhost:8888"
   DEBUG=False
   TIMEOUT=30
   VERIFY_SSL=False
   ```

2. 直接设置环境变量：
   ```bash
   export BT_API_KEY="your-api-key"
   export BT_PANEL_HOST="http://localhost:8888"
   export DEBUG=False
   export TIMEOUT=30
   export VERIFY_SSL=False
   ```

> 注意：`.env` 文件应该添加到 `.gitignore` 中以保护您的API密钥安全。

# Examples
#### 1.首先需要在 `面板设置-API接口` 中打开API接口，获取 `接口秘钥` 。
#### 2.开启API后，必需在IP白名单列表中的IP才能访问面板API接口。
#### 3.如需本机调用面板API密钥，请添加"127.0.0.1"和本机IP至IP白名单。
> 接口初始化`BT_PANEL_HOST`参数不需要安全入口，只需要填写面板的域名或IP加端口即可，如: `http://192.168.1.168:8888`。
```python
# 系统状态相关接口api
>>> from pybt.api import System
>>> system_api = System()  # 将自动使用环境变量

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
```
```python
# 网站管理相关接口
>>> from pybt.api import Website, WebsiteBackup, Domain, Rewrite, Directory, PasswordAccess, TrafficLimit, DefaultDocument
>>> website_api = Website()  # 将自动使用环境变量

# 获取网站列表
>>> website_api.get_website_list()

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
>>> website_api.get_php_versions()

[{'version': '00', 'name': '纯静态'}, {'version': '56', 'name': 'PHP-56'}]

# 网站备份管理
>>> backup_api = WebsiteBackup()
>>> backup_api.get_backup_list(search=5)  # 获取网站ID为5的备份列表

# 域名管理
>>> domain_api = Domain()
>>> domain_api.get_domain_list(site_id=5)  # 获取网站ID为5的域名列表

# 目录和配置管理
>>> dir_api = Directory()
>>> dir_api.get_root_path(id=5)  # 获取网站ID为5的根目录

# 密码访问控制
>>> pwd_api = PasswordAccess()
>>> pwd_api.set_password_access(id=5, username="admin", password="secret")

# 流量限制管理
>>> traffic_api = TrafficLimit()
>>> traffic_api.set_traffic_limit(id=5, perserver=100, perip=10, limit_rate=1024)

# 默认文档管理
>>> doc_api = DefaultDocument()
>>> doc_api.set_default_document(id=5, index="index.php,index.html")
```

# 功能模块
> 点击小三角展开查看模块方法，具体模块参数见文档目录 <a href="https://bt-python-sdk.readthedocs.io/en/latest/?">在线文档</a>
<details><summary>System: 系统状态相关接口</summary>
<p>

* `get_system_total  获取系统基础统计`
* `get_disk_info  获取磁盘分区信息`
* `get_network  获取实时状态信息(CPU、内存、网络、负载)`
* `get_task_count 检查是否有安装任务`
* `update_panel 检查面板更新`
</details>

<details><summary>Website: 基础网站管理</summary>
<p>

* `get_website_list  获取网站列表`
* `get_site_types  获取网站分类`
* `get_php_versions  获取已安装的 PHP 版本列表`
* `create_website  创建网站`
* `delete_website  删除网站`
* `stop_website  停用网站`
* `start_website  启用网站`
* `set_expiry_date  设置网站有效期`
* `set_website_remark  修改网站备注`
</details>

<details><summary>WebsiteBackup: 网站备份管理</summary>
<p>

* `get_backup_list  获取网站备份列表`
* `create_backup  创建网站备份`
* `delete_backup  删除网站备份`
</details>

<details><summary>Domain: 域名管理</summary>
<p>

* `get_domain_list  获取网站域名列表`
* `add_domain  添加网站域名`
* `delete_domain  删除网站域名`
</details>

<details><summary>Rewrite: 重写规则和配置管理</summary>
<p>

* `get_rewrite_list  获取可用的重写规则`
* `get_rewrite_content  获取重写规则内容`
* `save_rewrite_content  保存重写规则内容`
</details>

<details><summary>Directory: 网站目录和运行时配置</summary>
<p>

* `get_root_path  获取网站根目录`
* `get_directory_config  获取目录配置`
* `toggle_cross_site  切换跨站保护`
* `toggle_access_log  切换访问日志`
* `set_root_path  设置网站根目录`
* `set_run_path  设置网站运行目录`
</details>

<details><summary>PasswordAccess: 密码访问控制</summary>
<p>

* `set_password_access  设置网站密码访问`
* `close_password_access  关闭网站密码访问`
</details>

<details><summary>TrafficLimit: 流量限制管理</summary>
<p>

* `get_traffic_limit  获取流量限制配置`
* `set_traffic_limit  设置流量限制配置`
* `close_traffic_limit  关闭流量限制`
</details>

<details><summary>DefaultDocument: 默认文档管理</summary>
<p>

* `get_default_document  获取默认文档配置`
* `set_default_document  设置默认文档配置`
</details>

# Testing
#### 执行单元测试前，请先在项目根目录创建 `.env` 文件，内容如下：
```bash
BT_API_KEY="your-api-key"
BT_PANEL_HOST="http://localhost:8888"
DEBUG=False
TIMEOUT=30
VERIFY_SSL=False
```

#### 然后执行：
```bash
# 仅运行单元测试
pytest

# 运行单元测试和集成测试
pytest --run-integration

# 仅运行集成测试
pytest -m integration --run-integration
```

> Good Luck! :star:

Powered by [bt APIs](https://www.bt.cn/bbs/thread-20376-1-1.html). 