from .client import Client


class System(Client):
    """
    定义功能（功能详见data.py）
    系统状态相关接口
    """
    def get_system_total(self):
        """获取系统基础统计
        """
        endpoint = self.config["GetSystemTotal"]
        return self.post_data(endpoint)

    def get_disk_info(self):
        """获取磁盘分区信息
        """
        endpoint = self.config["GetDiskInfo"]
        return self.post_data(endpoint)

    def get_net_work(self):
        """获取实时状态信息(CPU、内存、网络、负载)
        """
        endpoint = self.config["GetNetWork"]
        return self.post_data(endpoint)

    def get_task_count(self):
        """检查是否有安装任务
        """
        endpoint = self.config["GetTaskCount"]
        return self.post_data(endpoint)

    def update_panel(self):
        """检查面板更新
        """
        endpoint = self.config["UpdatePanel"]
        return self.post_data(endpoint)