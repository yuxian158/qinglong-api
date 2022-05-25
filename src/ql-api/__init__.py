import json

import requests

from requests import Response


class ql_api:
    def __init__(self, url: str, post: int, client_id: str, client_secret: str):
        """初始化

        :param url: 面板ip地址
        :param post: 面板端口
        :param client_id: client_id
        :param client_secret: client_secret
        """
        self.url = f"http://{url}:{post}"
        self.client_id = client_id
        self.client_secret = client_secret
        self._s = requests.session()
        self._get_ql_token()

    def _get_ql_token(self):
        url = f"{self.url}/open/auth/token?client_id={self.client_id}&client_secret={self.client_secret}"
        res = self._s.get(url)
        token = json.loads(res.text)["data"]['token']
        self._s.headers.update({"authorization": "Bearer " + str(token)})
        self._s.headers.update({"Content-Type": "application/json;charset=UTF-8"})

    @staticmethod
    def _get_req_results(res: Response):
        if res.status_code == 200:
            return 200
        else:
            try:
                return res.json().get("message")
            except:
                return "未知错误"

    def add_env(self, new_env, value):
        url = f"{self.url}/open/envs"
        data = [{"value": value, "name": new_env}]
        data = json.dumps(data)
        res = self._s.post(url=url, data=data)
        return res

    def del_env(self, id):
        url = f"{self.url}/open/envs"
        data = json.dumps([id])
        res = self._s.delete(url=url, data=data)
        return res

    def get_env(self, env):
        url = f"{self.url}/open/envs?searchValue={env}"
        res = self._s.get(url=url).json().get("data")
        id_list = []
        value_list = []
        for i in res:
            id_list.append(i.get('id'))
            value_list.append(i.get('value'))
        return zip(id_list, value_list)

    def task_add(self, command: str, schedule: str, name: str, labels: str = '') -> dict:
        """添加定时任务,返回相应状态码以及响应结果或任务ID

        :param command: 命令
        :param schedule: 定时时间
        :param name: 定时任务名称
        :param labels: 备注,测试不通过，留空
        :return:
            成功返回示例 {'code': 200, 'data': 47}
            失败返回示例 {'code': 500, 'data': 'Validation error'}
        """
        url = f"{self.url}/open/crons"
        data = {
            "command": command,
            "schedule": schedule,
            "name": name,
            # "labels": labels
        }
        data = json.dumps(data)
        res = self._s.post(url=url, data=data)
        if res.status_code == 200:
            return {"code": 200,
                    "data": res.json().get('data').get('id')
                    }
        else:
            return {
                "code": res.status_code,
                "data": res.json().get("message")
            }

    def task_run(self, id: list) -> int:
        """根据id运行任务

        :param id: 任务ID列表
        :return:
        响应码
        """
        url = f"{self.url}/open/crons/run"
        data = json.dumps(id)
        return self._s.put(url=url, data=data).status_code

    def config_list(self):
        """获取配置文件列表

        :return: 源相应json
        """
        url = f"{self.url}/open/configs/files"
        return self._s.get(url=url).json()

    def config_value(self, file_name):
        """获取配置文件内容

        :param file_name: 文件名
        :return: 源相应json
        """
        url = f"{self.url}/open/configs/{file_name}"
        return self._s.get(url=url).json()

    def config_save(self, name, content):
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
        return self._s.post(url=url, data=json.dumps(data)).json()
