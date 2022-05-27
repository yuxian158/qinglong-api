import json

from .ql import ql_api


class qllog(ql_api):
    """
    青龙面板日志接口
    """
    def __init__(self, url: str, post: int, client_id: str, client_secret: str):
        super().__init__(url, post, client_id, client_secret)

    def list(self):
        """获取日志文件列表

        :return: 源相应json
        """
        url = f"{self.url}/open/logs"
        return self.s.get(url=url).json()