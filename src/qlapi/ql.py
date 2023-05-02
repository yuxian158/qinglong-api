import json

import requests

from requests import Response


class ql_api:
    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        """初始化

        :param url: 面板ip地址
        :param port: 面板端口
        :param client_id: client_id
        :param client_secret: client_secret
        """
        self.url = f"http://{url}:{port}"
        self.client_id = client_id
        self.client_secret = client_secret
        self.s = requests.session()
        self.__get_ql_token()

    def __get_ql_token(self):
        url = f"{self.url}/open/auth/token?client_id={self.client_id}&client_secret={self.client_secret}"
        res = self.s.get(url)
        print(self._get_req_results(res))
        res = res.json()
        token = res["data"]['token']
        self.s.headers.update({"authorization": "Bearer " + str(token)})
        self.s.headers.update({"Content-Type": "application/json;charset=UTF-8"})

    @staticmethod
    def _get_req_results(res: Response):
        if res.status_code == 200:
            return "青龙登录成功！"
        else:
            try:
                return res.json().get("message")
            except:
                return "未知错误"



