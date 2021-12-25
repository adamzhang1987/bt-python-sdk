# About

#### **Pybt** is a BaoTa panel python sdk. 
##
#### **Pybt** 是一个宝塔面板API的Python版本sdk封装库。
##
> 公司很多服务器都装了宝塔面板，通过宝塔来部署、安装、维护一些服务，服务器的数量上以后，导致了维护的不方便，这个时候就想使用宝塔提供的API来开发一个运维平台，通过平台来统一监听服务器状态和执行一些简单运维操作。网上找了一下，没有特别满意的Python封装，干脆自己撸了一套。

# 感谢
#### 编写的时候参考了两位老哥的代码
* Abudu： https://github.com/am-abudu/BtPanel-API-Python-SDK
* meimz：https://github.com/meimz/mbt
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

# Examples
#### 1.首先需要在 `面板设置-API接口` 中打开API接口，获取 `接口秘钥` 。
#### 2.开启API后，必需在IP白名单列表中的IP才能访问面板API接口。
#### 3.如需本机调用面板API密钥，请添加"127.0.0.1"和本机IP至IP白名单。
> 接口初始化`YOUR_PANEL_ADDRESS`参数不需要安全入口，只需要填写面板的域名或IP加端口即可，如: `http://192.168.1.168:8888`。
```python
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
```
```python
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
```
```python
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
```
```python
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
```
```python
# 插件管理
>>> from pybt.plugin import Plugin
>>> plugin_api = Plugin((YOUR_PANEL_ADDRESS, YOUR_API_KEY)
# 宝塔一键部署执行
>>> plugin_api.setup_package(dname, site_name, php_version)
```

# 功能模块
> 点击小三角展开查看模块方法，具体模块参数见文档目录 <a href="https://github.com/adamzhang1987/bt-python-sdk/tree/main/docs">docs/</a>
<details><summary>System: 系统状态相关接口</summary>
<p>

* `get_system_total  获取系统基础统计`
* `get_disk_info  获取磁盘分区信息`
* `get_net_work  获取实时状态信息(CPU、内存、网络、负载)`
* `get_task_count 检查是否有安装任务`
* `update_panel 检查面板更新`
</details>

<details><summary>Sites: 网站管理相关接口</summary>
<p>

* `websites  获取网站列表`
* `webtypes  获取网站分类`
* `get_site_id  获取指定站点ID若站点不存在则返回-1`
* `get_php_version  获取已安装的 PHP 版本列表`
* `get_site_php_version  获取指定网站运行的PHP版本`
* `set_php_version  修改指定网站的PHP版本`
* `get_type_id     获取分类ID若分类不存在则返回0`
* `set_has_pwd  开启并设置网站密码访问`
* `close_has_pwd  关闭网站密码访问`
* `get_dir_user_ini  获取网站几项开关（防跨站、日志、密码访问）`
* `web_add_site   创建网站`
* `web_delete_site  删除网站`
* `web_site_stop  停用网站`
* `web_site_start  启用网站`
* `web_set_end_date  设置网站有效期`
* `web_set_ps  修改网站备注`
* `web_backup_list  获取网站备份列表`
* `web_to_backup  创建网站备份`
* `web_del_backup  删除网站备份`
* `web_domain_list  获取网站域名列表`
* `get_dir_binding  获取网站域名绑定二级目录信息`
* `add_dir_binding  添加网站子目录域名`
* `del_dir_binding  删除网站绑定子目录`
* `get_dir_rewrite  获取网站子目录伪静态规则`
* `web_add_domain  添加网站域名`
* `web_del_domain  删除网站域名 `
* `get_site_logs  获取网站日志`
* `get_security  获取网站盗链状态及规则信息`
* `set_security  设置网站盗链状态及规则信息`
* `get_ssl  获取SSL状态及证书详情`
* `http_to_https  强制HTTPS`
* `close_to_https 关闭强制HTTPS`
* `set_ssl  设置SSL证书`
* `close_ssl_conf  关闭SSL`
* `web_get_index  获取网站默认文件`
* `web_set_index  设置网站默认文件`
* `get_limit_net  获取网站流量限制信息`
* `set_limit_net  设置网站流量限制信息`
* `close_limit_net  关闭网站流量限制`
* `get_301_status  获取网站301重定向信息`
* `set_301_status  设置网站301重定向信息`
* `get_rewrite_list 获取可选的预定义伪静态列表`
* `get_file_body  获取指定预定义伪静态规则内容(获取文件内容)`
* `save_file_body  保存伪静态规则内容(保存文件内容)`
* `get_proxy_list  获取网站反代信息及状态`
* `create_proxy  添加网站反代信息`
* `modify_proxy  修改网站反代信息`
</details>

<details><summary>Ftp: Ftp管理</summary>
<p>

* `web_ftp_list 获取FTP信息列表`
* `set_user_password  修改FTP账号密码`
* `get_ftp_id  根据Ftp_Username获取FTPID`
* `set_status  启用/禁用FTP`
</details>

<details><summary>DBM: 数据库管理</summary>
<p>

* `web_db_list 获取SQL信息列表`
* `get_db_id 修改SQL账号密码`
* `res_database_pass 根据数据库名获取SQLID`
* `db_to_backup  创建sql备份`
* `db_del_backup  删除sql备份`
</details>

<details><summary>Plugin: 插件管理 </summary>
<p>

* `deployment  宝塔一键部署列表`
* `setup_package 部署任务`
</details>

# Documentation
#### 详见 <a href="https://github.com/adamzhang1987/bt-python-sdk/tree/main/docs">docs/</a>

# Testing
#### 执行单元测试前，请先在 `tests` 目录下新建一个 `config.py` 的文件，文件内容如下：
```python
# config.py
CONFIG = {
    "panel_address": YOUR_PANEL_ADDRESS,
    "api_key": YOUR_API_KEY
}
```
#### 然后执行：
```bash
python -m unittest
```
#### 或者
```bash
pytest
```
> 祝您好运! :star:

# TODO
* 完善测试用例
* 完善文档
* 完善exapmles

Powered by [bt APIs](https://www.bt.cn/bbs/thread-20376-1-1.html).
