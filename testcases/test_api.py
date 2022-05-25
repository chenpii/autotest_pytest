import os

import pytest

from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_yaml, read_testcase


class TestRequest:

    # get请求：获取统一鉴权码token接口
    @pytest.mark.smoke
    @pytest.mark.parametrize("args_name", read_testcase("get_token.yaml"))
    def test_get_token(self, args_name):
        url = args_name["request"]["url"]
        data = args_name["request"]["data"]
        method = args_name["request"]["method"]
        res = RequestUtil.send_request(method=method, url=url, datas=data)
        print(res.json())
        # 将access_token写入到yaml中
        if "access_token" in res.text:
            write_yaml({"access_token": res.json()['access_token']})

    # post请求:编辑标签接口
    @pytest.mark.parametrize("args_name", read_testcase("edit_flag.yaml"))
    def test_edit_flag(self, args_name):
        url = args_name["request"]["url"] + read_yaml("access_token")
        # data = {"tag": {"id": 134, "name": "广东人"}}
        data = args_name["request"]["data"]
        method = args_name["request"]["method"]
        res = RequestUtil.send_request(method=method, url=url, datas=data)
        print(res.json())

    # 文件上传接口
    @pytest.mark.parametrize("args_name", read_testcase("file_upload.yaml"))
    def test_file_upload(self, args_name):
        url = args_name["request"]["url"] + read_yaml("access_token")
        data = {
            "media": open(os.getcwd() + args_name["request"]["data"]["media"], "rb")
        }
        method = args_name["request"]["method"]
        res = RequestUtil.send_request(method=method, url=url, files=data)
        print(res.json())


if __name__ == '__main__':
    TestRequest.test_get_token()
    TestRequest.test_edit_flag()
    TestRequest.test_file_upload()
