import json

from .ql import ql_api


class qlenv(ql_api):
    """
    青龙面板api环境变量模块

    url: 青龙面板IP地址(不包含http://)

    port: 青龙面板端口

    client_id: 青龙面板openapi登录用户名

    client_secret: 青龙面板openapi登录密码

    Usage::
        >>> ql_env = qlenv(
            url="12.22.43.23",
            port=5700,
            client_id="admin",
            client_secret="abcdefg_",
        )
        ql_env.list()
    """
    def __init__(self, url: str, port: int, client_id: str, client_secret: str):
        super().__init__(url, port, client_id, client_secret)

    def add(self, new_env, value):
        """
        添加环境变量

        :param new_env: 新环境变量名
        :param value: 新环境变量值
        :return:  响应结果json
        """
        url = f"{self.url}/open/envs"
        data = [{"value": value, "name": new_env}]
        data = json.dumps(data)
        res = self.s.post(url=url, data=data)
        return res.json()

    def delete(self, id):
        """
        删除环境变量

        :param id: 环境变量ID
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs"
        data = json.dumps([id])
        res = self.s.delete(url=url, data=data).json()
        return res

    def search(self, env):
        """
        获取环境变量

        :param env: 环境变量名
        :return: zip(环境变量ID,环境变量值) 使用for(id,value) in get_env(env)
        """
        url = f"{self.url}/open/envs?searchValue={env}"
        res = self.s.get(url=url).json().get("data")
        id_list = []
        value_list = []
        for i in res:
            id_list.append(i.get('id'))
            value_list.append(i.get('value'))
        return zip(id_list, value_list)

    def update(self, value, name, id, remarks=""):
        """
        更新环境变量

        :param value: 新值
        :param name: 新名称
        :param id: 环境变量id
        :param remarks: 新备注
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs"
        data = {"value": value, "name": name, "remarks": remarks, "id": id}
        data = json.dumps(data)
        print(data)
        res = self.s.put(url=url, data=data).json()
        return res

    def list(self):
        """
        获取所有环境变量

        :param id: 环境变量ID
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs/"
        res = self.s.get(url=url).json()
        return res

    def get_by_id(self, id):
        """
        根据环境变量ID获取环境变量

        :param id: 环境变量ID
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs/{id}"
        res = self.s.get(url=url).json()
        return res

    def enable(self, id_list):
        """
        启用环境变量

        :param id_list: 环境变量ID列表
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs/enable"
        data = json.dumps(id_list)
        res = self.s.put(url=url, data=data).json()
        return res

    def disable(self, id_list):
        """
        禁用环境变量

        :param id_list: 环境变量ID列表
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs/disable"
        data = json.dumps(id_list)
        res = self.s.put(url=url, data=data).json()
        return res

    def rename(self, id, name):
        """
        修改环境变量名

        :param id: id
        :param name: name
        :return: 响应结果json
        """
        url = f"{self.url}/open/envs/name"
        data = json.dumps({"ids": id, "name": name})
        res = self.s.put(url=url, data=data).json()
        return res
