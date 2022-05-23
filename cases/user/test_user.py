import re

import requests

from common.yaml_util import write_yaml, read_yaml


class TestUser:
    # 全局变量,类变量
    sess = requests.session()

    # 访问首页接口
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        # res = requests.request(method="get", url=url)
        # 通过sess请求，就不用cookies
        res = TestUser.sess.request(method="get", url=url)
        # 正则提取提取鉴权码：re.search("正则表达式",res.text)
        obj = re.search('name="csrf_token" value="(.*?)"', res.text)
        print(obj.group(1))  # 取匹配到的第1个值

        # 写入到yaml文件
        write_yaml({"csrf_token": obj.group(1)})

        # # 提取cookies
        # TestRequest.php_cookie = res.cookies

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
        # res = requests.request(method="post", url=url, data=data, headers=headers, cookies=TestRequest.php_cookie)
        # 使用session请求
        res = TestUser.sess.request(method="post", url=url, data=data, headers=headers)
        print(res.json())
