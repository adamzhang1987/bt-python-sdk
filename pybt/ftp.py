from .client import Client


class Ftp(Client):
    """Ftp管理
    """
    def web_ftp_list(self, page='1', limit='15', type='-1', order='id desc', tojs='', search=''):
        """获取网站FTP列表

        Args:
            page (str, optional): 当前分页. Defaults to '1'.
            limit (str, optional): 取出的数据行数. Defaults to '15'.
            type (str, optional): 分类标识 -1: 分部分类 0: 默认分类. Defaults to '-1'.
            order (str, optional): 排序规则 使用 id 降序：id desc 使用名称升序：name desc. Defaults to 'id desc'.
            tojs (str, optional): 分页 JS 回调,若不传则构造 URI 分页连接. Defaults to ''.
            search (str, optional): 搜索内容. Defaults to ''.
        """
        endpoint = self.config["WebFtpList"]
        data = {}
        data['p'] = page
        data['limit'] = limit
        data['type'] = type
        data['order'] = order
        data['tojs'] = tojs
        data['search'] = search
        return self.post_data(endpoint, data=data)

    def get_ftp_id(self, ftp_username):
        """根据Ftp_Username获取FTPID
        
        Args:
            ftp_username (string): 用户名
        """
        data = self.web_ftp_list()
        for i in data['data']:
            if i['name'] == ftp_username:
                return i['id']
        return -1

    def set_user_password(self, ftp_username, new_password):
        """修改FTP账号密码
         
        Args:
            ftp_username (string): 用户名
            new_password (string): 密码
        """
        endpoint = self.config["SetUserPassword"]
        data = {}
        data["id"] = self.__get_ftp_id(ftp_username)
        data["ftp_username"] = ftp_username
        data["new_password"] = new_password
        return self.post_data(endpoint, data=data)

    def set_status(self, ftp_username, status):
        """启用/禁用FTP
        ftp_username 
        status       

        Args:
            ftp_username (string): 用户名
            status (string): 状态 0->关闭;1->开启
        """
        endpoint = self.config["SetStatus"]
        data = {}
        data["id"] = self.get_ftp_id(ftp_username)
        data["username"] = ftp_username
        data["status"] = status
        return self.post_data(endpoint, data=data)
