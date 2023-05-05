import json

from .ql import ql_api


class qlsystem(ql_api):
    """
    青龙面板api系统模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_system = qlsystem(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_system.version()
    """
    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)

    def version(self) -> dict:
        """
        获取面板版本信息

        :return: 源相应json
        """
        url = f"{self.url}/open/system"
        return self.s.get(url).json()

    def get_log_remove(self) -> dict:
        """
        获取清除面板日志频率

        :return: 源相应json
        """
        url = f"{self.url}/open/system/log/remove"
        return self.s.get(url).json()

    def change_log_remove(self, frequency: int) -> dict:
        """
        修改清除面板日志频率

        :param log_remove: 日志清除频率,单位天
        :return: 源相应json
        """
        url = f"{self.url}/open/system/log/remove"
        data = {"frequency": frequency}
        return self.s.put(url, data=json.dumps(data)).json()

    def update_check(self) -> dict:
        """
        检查面板更新

        :return: 源相应json
        """
        url = f"{self.url}/open/system/update-check"
        return self.s.put(url).json()

    def update(self) -> dict:
        """
        更新面板

        :return: 源相应json
        """
        url = f"{self.url}/open/system/update"
        return self.s.put(url).json()