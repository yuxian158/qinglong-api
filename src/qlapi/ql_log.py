import json

from .ql import ql_api


class qllog(ql_api):
    """
    青龙面板api日志模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_log = qllog(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_log.list()
    """
    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)

    def list(self):
        """获取日志文件列表

        :return: 源相应json
        """
        url = f"{self.url}/open/logs"
        return self.s.get(url=url).json()