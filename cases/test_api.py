import json
import re

import requests


class TestRequest:
    # 全局变量,类变量
    access_token = ""
    csrf_token = ""
    php_cookie = ""
    sess = requests.session()

    # get请求：获取统一鉴权码token接口
    def test_get_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        data = {
            "grant_type": "client_credential",
            "appid": "wx7ff6c1d5ba45d17e",
            "secret": "4b5fe134130b7c292d6a6c22f38b56d0"
        }
        res = requests.request(method="get", url=url, params=data)
        print(res.json())
        TestRequest.access_token = res.json()['access_token']

    # post请求:编辑标签接口
    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + TestRequest.access_token
        data = {"tag": {"id": 101, "name": "广东人"}}
        str_date = json.dumps(data)
        res = requests.request(method="post", url=url, data=str_date)
        print(res.json())

    # 文件上传
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + TestRequest.access_token
        data = {
            "media": open(r"E:\developer\idea\workspace\autotest_pytest\image.png", "rb")
        }
        res = requests.request(method="post", url=url, files=data)
        print(res.json())

    # 访问首页接口
    def test_start(self):
        url = "http://47.107.116.139/phpwind/"
        # res = requests.request(method="get", url=url)
        # 通过sess请求，就不用cookies
        res = TestRequest.sess.request(method="get", url=url)
        # print(res.text)
        # 正则提取提取鉴权码
        # re.search("正则表达式",res.text)
        obj = re.search('name="csrf_token" value="(.*?)"', res.text)
        # 取匹配到的第1个值
        print(obj.group(1))
        TestRequest.csrf_token = obj.group(1)

        # # 提取cookies
        # TestRequest.php_cookie = res.cookies

    def test_login(self):
        url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
        data = {
            "username": "chenh",
            "password": "chen0816php",
            "csrf_token": TestRequest.csrf_token,  # 鉴权码，从首页获取
            "backurl": "http://47.107.116.139/phpwind/",
            "invite": ""
        }
        headers = {
            "Accept": "application/json,text/javascript,/; q=0.01",
            "X-Requested-With": "XMLHttpRequest"
        }
        # res = requests.request(method="post", url=url, data=data, headers=headers, cookies=TestRequest.php_cookie)
        # 使用session请求
        res = TestRequest.sess.request(method="post", url=url, data=data, headers=headers)
        print(res.json())


if __name__ == '__main__':
    TestRequest.test_get_token()
    TestRequest.test_edit_flag()
    TestRequest.test_file_upload()
    TestRequest.test_start()
    TestRequest.test_login()
