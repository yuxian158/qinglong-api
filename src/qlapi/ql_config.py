import json

from .ql import ql_api


class qlconfig(ql_api):
    """
    青龙面板api配置文件模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_config = qlconfig(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_config.list()
    """
    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)

    def list(self):
        """获取配置文件列表

        :return: 源相应json
        """
        url = f"{self.url}/open/configs/files"
        return self.s.get(url=url).json()

    def value(self, file_name):
        """获取配置文件内容

        :param file_name: 文件名
        :return: 源相应json
        """
        url = f"{self.url}/open/configs/{file_name}"
        return self.s.get(url=url).json()

    def save(self, name, content):
        """保存配置文件

        :param name: 文件名
        :param content: 值
        :return: 源相应json
        """
        url = f"{self.url}/open/configs/save"
        data = {
            "name": name,
            "content": content
        }
        return self.s.post(url=url, data=json.dumps(data)).json()
