import json

from .ql import ql_api


class qlconfig(ql_api):
    """
    青龙面板配置文件
    """
    def __init__(self, url: str, post: int, client_id: str, client_secret: str):
        super().__init__(url, post, client_id, client_secret)

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
