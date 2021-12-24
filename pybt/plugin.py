from .client import Client

class Plugin(Client):
    """插件管理
    """
    def deployment(self, search=False):
        """获取宝塔一键部署列表

        Args:
            search (bool, optional): 搜索关键词. Defaults to False.
        """
        endpoint = self.config["deployment"]
        if search:
            url = endpoint + "&search=" + search
            print(url)
        return self.post_data(endpoint)

    def setup_package(self, dname, site_name, php_version):
        """宝塔一键部署执行

        Args:
            dname (string): 部署程序名
            site_name (string): 部署到网站名
            php_version (string): PHP版本
        """
        endpoint = self.config["SetupPackage"]
        data = {}
        data['dname'] = dname
        data['site_name'] = site_name
        data['php_version'] = php_version
        return self.post_data(endpoint, data=data)