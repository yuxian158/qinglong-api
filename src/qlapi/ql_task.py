import json

from .ql import ql_api


class qltask(ql_api):
    """
    青龙面板api定时任务模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_task = qltask(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_task.list()
    """

    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)

    def add(self, command: str, schedule: str, name: str, labels: str = '') -> dict:
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
        res = self.s.post(url=url, data=data)
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
        :return: 响应码
        """
        url = f"{self.url}/open/crons/run"
        data = json.dumps(id)
        return self.s.put(url=url, data=data).status_code

    def edit(self, command: str, schedule: str, name: str, id: int) -> dict:
        """修改定时任务,返回相应状态码以及响应结果或任务信息

        :param command: 命令
        :param schedule: 定时时间
        :param name: 定时任务名称
        :param id: 任务ID
        :return:
            成功返回示例 {'code': 200, 'data': {'id': 42, 'name': 'newrefin', 'command': 'task tgrefin.py', 'schedule': '* * * 1 5'}}

            失败返回示例 {'code': 500, 'data': 'Validation error'}
        """
        url = f"{self.url}/open/crons"
        data = {
            "command": command,
            "schedule": schedule,
            "name": name,
            "id": id
        }
        data = json.dumps(data)
        res = self.s.put(url=url, data=data)
        if res.status_code == 200:
            return {"code": 200,
                    "data":
                        {
                            "id": res.json().get('data').get('id'),
                            "name": res.json().get('data').get('name'),
                            "command": res.json().get('data').get('command'),
                            "schedule": res.json().get('data').get('schedule')
                        }
                    }
        else:
            return {
                "code": res.status_code,
                "data": res.json().get("message")
            }

    def delete(self, id: str) -> dict:
        """删除定时任务,返回相应状态码以及响应结果或任务ID

        :param id: 任务ID
        :return:
            成功返回示例 {'code': 200}

            失败返回示例 {'code': 400, 'data': 'Validation failed'}
        """
        url = f"{self.url}/open/crons"
        data = json.dumps([id])
        res = self.s.delete(url=url, data=data)
        if res.status_code == 200:
            return {"code": 200}
        else:
            return {
                "code": res.status_code,
                "data": res.json().get("message")
            }
