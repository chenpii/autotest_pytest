import re

from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml


class TestLogin:




    # 登录接口
    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "chenh",
            "password": "chen0816php",
            "csrf_token": read_yaml("csrf_token"),  # 鉴权码，从首页获取
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json,text/javascript,/; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        res = RequestUtil.send_request(method="post", url=url, datas=data, headers=headers)
        print(res.json())
