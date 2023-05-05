import json

from .ql import ql_api


class qldependence(ql_api):
    """
    青龙面板api依赖管理模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_dependence = qldependence(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_dependence.get()
    """
    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)
        self.dependence_url = f"{self.url}/open/dependence"

    def get(self):
        """
        获取已安装依赖列表

        :return: 源响应json
        """
        return self.s.get(self.dependence_url).json()


