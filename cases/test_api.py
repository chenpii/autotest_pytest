import json
import os

import requests

from common.yaml_util import write_yaml, read_yaml


class TestRequest:

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
        # 将access_token写入到yaml中
        write_yaml({"access_token": res.json()['access_token']})
        # TestRequest.access_token = res.json()['access_token']

    # post请求:编辑标签接口
    def test_edit_flag(self):
        url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token=" + read_yaml("access_token")
        data = {"tag": {"id": 134, "name": "广东人"}}
        str_date = json.dumps(data)
        res = requests.request(method="post", url=url, data=str_date)
        print(res.json())

    # 文件上传
    def test_file_upload(self):
        url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=" + read_yaml("access_token")
        data = {
            "media": open(os.getcwd()+"/image.png", "rb")
        }
        res = requests.request(method="post", url=url, files=data)
        print(res.json())


if __name__ == '__main__':
    TestRequest.test_get_token()
    TestRequest.test_edit_flag()
    TestRequest.test_file_upload()
