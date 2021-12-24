from .client import Client
class DBM(Client):
    """数据库管理
    """
    def web_db_list(self, page='1', limit='15', type='-1', order='id desc', tojs='', search=''):
        """获取SQL信息列表

        Args:
            page (string): 当前分页
            limit (string): 取出的数据行数
            type (string): 分类标识 -1: 分部分类 0: 默认分类
            order (string): 排序规则 使用 id 降序：id desc 使用名称升序：name desc
            tojs (string): 分页 JS 回调,若不传则构造 URI 分页连接
            search (string): 搜索内容
        """
        endpoint = self.config["WebSqlList"]
        data = {}
        data['p'] = page
        data['limit'] = limit
        data['type'] = type
        data['order'] = order
        data['tojs'] = tojs
        data['search'] = search
        return self.post_data(endpoint, data=data)

    def get_db_id(self, sql_username):
        """根据数据库名获取SQLID

        Args:
            sql_username (string): SQL用户名
        """
        data = {}
        for i in data['data']:
            if i['name'] == sql_username:
                return i['id']
        return -1

    def res_database_pass(self, ftp_username, new_password):
        """修改数据库账号密码

        Args:
            ftp_username (string): 数据库名
            new_password (string): 新密码
        """
        endpoint = self.config["ResDatabasePass"]
        data = {}
        data["id"] = self.get_sql_id(ftp_username)
        data["name"] = ftp_username
        data["password"] = new_password
        return self.post_data(endpoint, data=data)

    def db_to_backup(self, database_name):
        """创建sql备份

        Args:
            database_name (string): 数据库名
        """
        endpoint = self.config["SQLToBackup"]
        data = {}
        data["id"] = self.get_sql_id(database_name)
        return self.post_data(endpoint, data=data)

    def db_del_backup(self, id):
        """删除sql备份

        Args:
            id (string): 备份ID
        """
        endpoint = self.config["SQLDelBackup"]
        data = {}
        data["id"] = id
        return self.post_data(endpoint, data=data)
