import json
from .client import Client


class Sites(Client):
    """网站管理相关接口
    """
    def websites(self):
        """获取网站列表
        """
        endpoint = self.config["Websites"]
        return self.post_data(endpoint)

    def webtypes(self): 
        """获取网站分类
        """
        endpoint = self.config["Webtypes"]
        return self.post_data(endpoint)

    def get_php_version(self):
        """获取已安装的 PHP 版本列表
        """
        endpoint = self.config["GetPHPVersion"]
        return self.post_data(endpoint)

    def get_site_php_version(self):
        """获取指定网站运行的PHP版本
        """
        endpoint = self.config["GetSitePHPVersion"]
        return self.post_data(endpoint)

    def set_php_version(self, site, php):  # 
        """修改指定网站PHP版本

        Args:
            site (string): 网站名
            php (string): PHP版本如73
        """
        data = {}
        data["siteName"] = site
        data["version"] = php
        endpoint = self.config["SetPHPVersion"]
        return self.post_data(endpoint, data=data)

    def get_site_id(self, site):
        """获取指定站点ID 若站点不存在则返回-1

        Args:
            site (string): 网站名
        """
        data = self.websites()["data"]
        for i in data:
            if i["name"] == site:
                return i["id"]
        return -1

    def get_site_path(self, site):
        """获取指定站点目录 若站点不存在则返回-1
        """
        data = self.websites()["data"]
        for i in data:
            if i["name"] == site:
                return i["path"]
        return -1

    def set_has_pwd(self, site, username, passwd):
        """开启并设置网站密码访问

        Args:
            site (string): 网站名
            username (string): 用户名
            passwd (string): 密码
        """
        data = {}
        data["id"] = self.get_site_id(site)
        data["username"] = username
        data["password"] = passwd
        endpoint = self.config["SetHasPwd"]
        return self.post_data(endpoint, data=data)

    def close_has_pwd(self, site):
        """关闭网站密码访问

        Args:
            site (string): 网站名
        """
        data = {}
        data["id"] = self.get_site_id(site)
        endpoint = self.config["CloseHasPwd"]
        return self.post_data(endpoint, data=data)

    def get_dir_user_ini(self, site):
        """获取网站几项开关（防跨站、日志、密码访问)

        Args:
            site (string): 网站名
        """
        data = {}
        data["id"] = self.get_site_id(site)
        data["path"] = self.get_site_path(site)
        endpoint = self.config["GetDirUserINI"]
        return self.post_data(endpoint, data=data)

    def get_type_id(self, _type):
        """获取分类ID，若不存在则返回0

        Args:
            _type (string): 分类名
        """
        data = self.webtypes()
        for i in data:
            if i["name"] == _type:
                return i["id"]
        return 0

    def web_add_site(self, site, _type, ps, ftp="false", ftp_username=None,ftp_password=None, sql="false", sql_codeing="utf8mb4", datauser=None, datapassword=None):
        """创建网站

        Args:
            site (string): 网站主域名
            _type (string): 网站分类名
            ps (string): 网站备注
            ftp (str, optional): 是否开启FTP (true/false). Defaults to "false".
            ftp_username (string, optional): FTP用户名. Defaults to None.
            ftp_password (string, optional): FTP密码 . Defaults to None.
            sql (str, optional): 是否开启SQL (true/false). Defaults to "false".
            sql_codeing (str, optional): MySQL数据库格式,默认为utf8mb4. Defaults to "utf8mb4".
            datauser (string, optional): 数据库用户名. Defaults to None.
            datapassword (string, optional): 数据库密码. Defaults to None.
        """
        data = {}
        data["webname"] = json.dumps({"domain":site,"domainlist":[],"count":0})
        data["path"] = "/www/wwwroot/" + site
        data["type_id"] = self.get_type_id(_type)
        data["type"] = "PHP"
        data["version"] = self.get_php_version()[-1]["version"]
        data["port"] = "80"
        data["ps"] = ps
        data["ftp"] = ftp
        if ftp_password != None and ftp_username != None and ftp == "true":
            data["ftp_username"] = ftp_username
            data["ftp_password"] = ftp_password
        data["sql"] = sql
        if datauser != None and datapassword != None and sql == "true":
            data["datauser"] = datauser
            data["datapassword"] = datapassword
            data["codeing"] = sql_codeing
        endpoint = self.config["WebAddSite"]
        return self.post_data(endpoint, data=data)

    def web_delete_site(self, site, ftp="false", database="false", path="false"):
        """删除网站

        Args:
            site (string): 网站名
            ftp (str, optional): 是否删除FTP (true/false). Defaults to "false".
            database (str, optional): 是否删除数据库 (true/false). Defaults to "false".
            path (str, optional): 是否删除站点根目录 (true/false). Defaults to "false".
        """
        endpoint = self.config["WebDeleteSite"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["webname"] = site
        data["ftp"] = ftp
        data["database"] = database 
        data["path"] = path
        return self.post_data(endpoint, data=data)

    def web_site_stop(self, site):
        """停用网站

        Args:
            site (string): 网站名
        """
        endpoint = self.config["WebSiteStop"]
        data = {}
        data["id"] = str(self.get_site_id(site))
        data["name"] = site
        return self.post_data(endpoint, data=data)

    def web_site_start(self, site):
        """启用网站

        Args:
            site (string): 网站名
        """
        endpoint = self.config["WebSiteStart"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["name"] = site
        return self.post_data(endpoint, data=data)

    def web_set_end_date(self, site, end_date):
        """设置网站到期时间

        Args:
            site (string): 网站名
            edate (string): 到期时间 格式为xxxx-xx-xx 若需永久请输入0000-00-00
        """
        endpoint = self.config["WebSetEdate"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["edate"] = end_date
        return self.post_data(endpoint, data=data)

    def web_set_ps(self, site, ps):
        """修改网站备注

        Args:
            site (string): 网站名
            ps (string): 备注
        """
        endpoint = self.config["WebSetPs"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["ps"] = ps
        return self.post_data(endpoint, data=data)

    def web_backup_list(self, site, p="1", limit="5", tojs="get_site_backup"):
        """获取网站备份列表

        Args:
            site (string): 网站名
            p (str, optional): 当前分页. Defaults to "1".
            limit (str, optional): 每页取回的数据行数. Defaults to "5".
            tojs (str, optional): 分页 JS 回调,若不传则构造 URI 分页连接. Defaults to "get_site_backup".
        """
        endpoint = self.config["WebBackupList"]
        data = {}
        data["search"] = self.get_site_id(site)
        data["p"] = p
        data["limit"] = limit
        data["type"] = "0"
        data["tojs"] = tojs
        return self.post_data(endpoint, data=data)

    def web_to_backup(self, site):
        """创建网站备份

        Args:
            site (string): 网站名
        """
        endpoint = self.config["WebToBackup"]
        data = {}
        data["id"] = self.get_site_id(site)
        return self.post_data(endpoint, data=data)

    def web_del_backup(self, id):
        """删除网站备份

        Args:
            id (string): 备份列表 ID
        """
        endpoint = self.config["WebDelBackup"]
        data = {}
        data["id"] = id
        return self.post_data(endpoint, data=data)

    def web_domain_list(self, site):
        """获取网站域名列表

        Args:
            site (string): 网站名
        """
        endpoint = self.config["WebDomainList"]
        data = {}
        data["search"] = self.get_site_id(site)
        data["list"] = "true"
        return self.post_data(endpoint, data=data)

    def get_dir_binding(self, site):
        """获取网站域名绑定二级目录信息

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetDirBinding"]
        data = {}
        data["id"] = self.get_site_id(site)
        return self.post_data(endpoint, data=data)

    def add_dir_binding(self, site, domain, dirName):
        """添加网站子目录域名

        Args:
            site (string): 网站名
            domain (string): 域名
            dirName (string): 目录名
        """
        endpoint = self.config["AddDirBinding"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["domain"] = domain
        data["dirName"] = dirName
        return self.post_data(endpoint, data=data)

    def del_dir_binding(self, dirid):
        """删除网站绑定子目录

        Args:
            dirid (string): 子目录ID
        """
        endpoint = self.config["DelDirBinding"]
        data = {}
        data["id"] = dirid
        return self.post_data(endpoint, data=data)

    def get_dir_rewrite(self, dirid):
        """获取网站子目录绑定伪静态信息

        Args:
            dirid (string): 子目录ID
        """
        endpoint = self.config["GetDirRewrite"]
        data = {}
        data["id"] = dirid
        return self.post_data(endpoint, data=data)

    def web_add_domain(self, site, domain):
        """添加网站域名

        Args:
            site (string): 网站名
            domain (string): 新增的域名
        """
        endpoint = self.config["WebAddDomain"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["webname"] = site
        data["domain"] = domain
        return self.post_data(endpoint, data=data)

    def web_del_domain(self, site, domain, port):
        """删除网站域名

        Args:
            site (string): 网站名
            domain (string): 删除的域名
            port (string): 删除的域名的端口

        Returns:
            string: [description]
        """
        endpoint = self.config["WebDelDomain"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["webname"] = site
        data["domain"] = domain
        data["port"] = port
        return self.post_data(endpoint, data=data)

    def get_site_logs(self, site):
        """获取网站日志

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetSiteLogs"]
        data = {}
        data["siteName"] = site
        return self.post_data(endpoint, data=data)

    def get_security(self, site):
        """获取网站盗链状态及规则信息

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetSecurity"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["name"] = site
        return self.post_data(endpoint, data=data)

    def set_security(self, site, fix, domains, status):
        """获取网站盗链状态及规则信息

        Args:
            site (string): 网站名
            fix (string): URL后缀  如"jpg,jpeg,gif,png,js,css"
            domains (string): 许可域名  
            status (string): 启用防盗链状态: "true"/"false"
        """
        endpoint = self.config["SetSecurity"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["name"] = site
        data["fix"] = fix
        data["domains"] = domains
        data["status"] = status
        return self.post_data(endpoint, data=data)

    def get_ssl(self, site):
        """获取SSL状态及证书详情

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetSSL"]
        data = {}
        data["siteName"] = site
        return self.post_data(endpoint, data=data)

    def http_to_https(self, site):
        """开启强制HTTPS

        Args:
            site (string): 网站名
        """
        endpoint = self.config["HttpToHttps"]
        data = {}
        data["siteName"] = site
        return self.post_data(endpoint, data=data)

    def close_to_https(self, site):
        """关闭强制HTTPS

        Args:
            site (string): 网站名
        """
        endpoint = self.config["CloseToHttps"]
        data = {}
        data["siteName"] = site
        return self.post_data(endpoint, data=data)

    def set_ssl(self, site, key, csr, type="1"):
        """设置SSL证书

        Args:
            site (string): 域名
            key (string): 证书key
            csr (string): 证书PEM
            type (str, optional): [description]. Defaults to "1".
        """
        endpoint = self.config["SetSSL"]
        data = {}
        data["type"] = type
        data["siteName"] = site
        data["key"] = key
        data["csr"] = csr
        return self.post_data(endpoint, data=data)

    def close_ssl_conf(self, site, updateOf="1"):
        """关闭SSL

        Args:
            site (string): 域名
            updateOf (str, optional): 修改状态码 (暂不明确用途). Defaults to "1".
        """
        endpoint = self.config["CloseSSLConf"]
        data = {}
        data["siteName"] = site
        data["updateOf"] = updateOf
        return self.post_data(endpoint, data=data)

    def web_get_index(self, site):
        """获取网站默认文件

        Args:
            site (string): 网站名
        """
        endpoint = self.config["WebGetIndex"]
        data = {}
        data["id"] = self.get_site_id(site)
        return self.post_data(endpoint, data=data)

    def web_set_index(self, site, index):
        """设置网站默认文件

        Args:
            site (string): 网站名
            index (string): 默认文件内容，如 "api.php,index.php,index.html,index.htm,default.php,default.htm,default.html"
        """
        endpoint = self.config["WebSetIndex"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["Index"] = index
        return self.post_data(endpoint, data=data)

    def get_limit_net(self, site):
        """获取网站流量限制信息

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetLimitNet"]
        data = {}
        data["id"] = self.get_site_id(site)
        return self.post_data(endpoint, data=data)

    def set_limit_net(self, site, perserver, perip, limit_rate):
        """设置网站流量限制信息

        Args:
            site (string): 网站名
            perserver (string): 并发限制
            perip (string): 单IP限制
            limit_rate (string): 流量限制
        """
        endpoint = self.config["GetLimitNet"]
        data = {}
        data["id"] = self.get_site_id(site)
        data["perserver"] = perserver
        data["perip"] = perip
        data["limit_rate"] = limit_rate
        return self.post_data(endpoint, data=data)

    def close_limit_net(self, site):
        """关闭网站流量限制

        Args:
            site (string): 网站名
        """
        endpoint = self.config["CloseLimitNet"]
        data = {}
        data["id"] = self.get_site_id(site)
        return self.post_data(endpoint, data=data)

    def get_301_status(self, site):
        """获取网站301重定向信息

        Args:
            site (string): 网站名
        """
        endpoint = self.config["Get301Status"]
        data = {}
        data["siteName"] = site
        return self.post_data(endpoint, data=data)

    def set_301_status(self, site, toDomain, srcDomain, type):
        """设置网站301重定向信息

        Args:
            site (string): 网站名
            toDomain (string): 目标Url
            srcDomain (string): 来自Url
            type (string): 类型
        """
        endpoint = self.config["Set301Status"]
        data = {}
        data["siteName"] = site
        data['toDomain'] = toDomain
        data['srcDomain'] = srcDomain
        data['type'] = type
        return self.post_data(endpoint, data=data)

    def get_rewrite_list(self, site):
        """获取可选的预定义伪静态列表

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetRewriteList"]
        data = {}
        data["siteName"] = site
        return self.post_data(endpoint, data=data)

    def get_file_body(self, path, type):
        """获取预置伪静态规则内容（文件内容）

        Args:
            path (string): 规则名（站点名）
            type (string): 0->获取内置伪静态规则；1->获取当前站点伪静态规则
        """
        endpoint = self.config["GetFileBody"]
        data = {}
        if type:
            path_dir = "vhost/rewrite"
        else:
            path_dir = "rewrite/nginx"
        """
        获取当前站点伪静态规则
        /www/server/panel/vhost/rewrite/user_hvVBT_1.test.com.conf
        获取内置伪静态规则
        /www/server/panel/rewrite/nginx/EmpireCMS.conf
        保存伪静态规则到站点
        /www/server/panel/vhost/rewrite/user_hvVBT_1.test.com.conf
        /www/server/panel/rewrite/nginx/typecho.conf
        """
        data['path'] = '/www/server/panel/' + path_dir + '/' + path + '.conf'
        return self.post_data(endpoint, data=data)

    def save_file_body(self, path, _data, encoding="utf-8", type=0):
        """保存伪静态规则内容(保存文件内容)

        Args:
            path (string): 规则名（站点名）
            _data (string): 规则内容
            encoding (string): 规则编码强转utf-8
            type (string): 0->系统默认路径；1->自定义全路径
        """
        endpoint = self.config["SaveFileBody"]
        data = {}
        if type:
            path_dir = path
        else:
            path_dir = '/www/server/panel/vhost/rewrite/' + path + '.conf'
        data['path'] = path_dir
        data['data'] = _data
        data['encoding'] = encoding
        return self.post_data(endpoint, data=data)

    def get_proxy_list(self, site):
        """获取网站反代信息及状态

        Args:
            site (string): 网站名
        """
        endpoint = self.config["GetProxyList"]
        data = {}
        data["sitename"] = site
        return self.post_data(endpoint, data=data)

    def modify_proxy(self, cache, proxyname, cachetime, proxydir, proxysite, todomain, advanced, sitename, subfilter, type):
        """修改网站反代信息

        Args:
            cache (string): 是否缓存
            proxyname (string): 代理名称
            cachetime (string): 缓存时长 /小时
            proxydir (string): 代理目录
            proxysite (string): 反代URL
            todomain (string): 目标域名
            advanced (string): 高级功能：开启代理目录
            sitename (string): 网站名
            subfilter (string): 文本替换json格式[{"sub1":"百度","sub2":"白底"},{"sub1":"","sub2":""}]
            type (string): 开启或关闭 0关;1开
        """
        endpoint = self.config["ModifyProxy"]
        data = {}
        data['cache'] = cache
        data['proxyname'] = proxyname
        data['cachetime'] = cachetime
        data['proxydir'] = proxydir
        data['proxysite'] = proxysite
        data['todomain'] = todomain
        data['advanced'] = advanced
        data['sitename'] = sitename
        data['subfilter'] = subfilter
        data['type'] = type
        return self.post_data(endpoint, data=data)

    def create_proxy(self, cache, proxyname, cachetime, proxydir, proxysite, todomain, advanced, sitename, subfilter, type):
        """获添加网站反代信息

        Args:
            cache (string): 是否缓存
            proxyname (string): 代理名称
            cachetime (string): 缓存时长 /小时
            proxydir (string): 代理目录
            proxysite (string): 反代URL
            todomain (string): 目标域名
            advanced (string): 高级功能：开启代理目录
            sitename (string): 网站名
            subfilter (string): 文本替换json格式[{"sub1":"百度","sub2":"白底"},{"sub1":"","sub2":""}]
            type (string): 开启或关闭 0关;1开
        """
        endpoint = self.config["CreateProxy"]
        data = {}
        data['cache'] = cache
        data['proxyname'] = proxyname
        data['cachetime'] = cachetime
        data['proxydir'] = proxydir
        data['proxysite'] = proxysite
        data['todomain'] = todomain
        data['advanced'] = advanced
        data['sitename'] = sitename
        data['subfilter'] = subfilter
        data['type'] = type
        return self.post_data(endpoint, data=data)