import re

from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml


class TestUser:

    # 访问首页接口
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        res = RequestUtil.send_request(method="get", url=url)
        # 正则提取提取鉴权码：re.search("正则表达式",res.text)
        obj = re.search('name="csrf_token" value="(.*?)"', res.text)
        # 取匹配到的第1个值写入到yaml文件
        write_yaml({"csrf_token": obj.group(1)})


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
