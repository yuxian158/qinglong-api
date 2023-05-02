import json

from .ql import ql_api


class qlscript(ql_api):
    """
    青龙面板api脚本管理模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_script = qlscript(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_script.get_all()
    """

    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)
        self.script_url = f"{self.url}/open/scripts/"

    def get_all(self):
        """
        获取所有脚本列表

        :return: 源响应json
        """
        url = self.script_url + 'files'
        return self.s.get(url).json()

    def get_script(self, name: str):
        """
        获取脚本详情

        :param name: 脚本名称
        :return: 源响应json
        """
        url = self.script_url + name
        return self.s.get(url).json()

    def add(self, filename: str, path: str, content: str, originFilename: str) -> dict:
        """
        添加脚本

        :param filename: 脚本名称
        :param path: 脚本路径
        :param content: 脚本内容
        :param originFilename: 脚本原始名称
        :return: 源响应json
        """
        url = self.script_url
        data = {
            "filename": filename,
            "path": path,
            "content": content,
            "originFilename": originFilename
        }
        return self.s.post(url, json=json.dumps(data)).json()

    def update(self, filename: str, path: str, content: str) -> dict:
        """
        更新脚本

        :param filename: 脚本名称
        :param path: 脚本路径
        :param content: 脚本内容
        :return: 源响应json
        """
        url = self.script_url
        data = {
            "filename": filename,
            "path": path,
            "content": content
        }
        return self.s.put(url, data=json.dumps(data)).json()

    def delete(self, path:str,filename: str) -> dict:
        """
        删除脚本

        :param path: 脚本路径
        :param filename: 脚本名称
        :return: 源响应json
        """
        url = self.script_url
        data = {
            "path": path,
            "filename": filename
        }
        return self.s.delete(url,data=json.dumps(data)).json()

    def download(self, filename: str) -> dict:
        """
        下载脚本

        :param filename: 脚本名称
        :return: 源响应json
        """
        url = self.script_url + "download"
        data = {
            "filename": filename
        }
        return self.s.post(url,data=json.dumps(data)).json()

    def run(self, path:str,filename: str) -> dict:
        """
        运行脚本

        :param path: 脚本路径
        :param filename: 脚本名称
        :return: 源响应json
        """
        url = self.script_url + "run"
        data = {
            "filename": filename,
            "path": path
        }
        print(data,url)
        return self.s.put(url,data=json.dumps(data)).json()

    def stop(self, path:str,filename: str) -> dict:
        """
        停止脚本

        :param path: 脚本路径
        :param filename: 脚本名称
        :return: 源响应json
        """
        url = self.script_url + "stop"
        data = {
            "filename": filename,
            "path": path
        }
        return self.s.put(url,data=json.dumps(data)).json()
