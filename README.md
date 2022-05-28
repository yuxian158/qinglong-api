# qinglongapi

青龙api的python SDK

具体文档

https://yuxian158.github.io/qinglong-api/

使用方法

安装

```
pip install qinglongapi
```

所有模块使用方法大同小异，以环境变量模块为例:

```
from qlapi import qlenv

ql_env = qlenv(
    url="12.22.43.23",   #青龙面板IP地址(不包含http://)
    port=5700,			#青龙面板端口
    client_id="admin",  # 青龙面板openapi登录用户名
    client_secret="abcdefg_", # 青龙面板openapi登录密码
)
ql_env.list()
```

青龙api文档

https://qinglong.ukenn.top/#/

很多还没有完善，欢迎pr
