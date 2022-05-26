import pytest

from common.request_util import RequestUtil
from common.yaml_util import read_yaml, read_testcase


class TestLogin:

    # 登录接口
    @pytest.mark.parametrize("args_name", read_testcase("/user/login.yaml"))
    def test_login(self, args_name):
        url = args_name["request"]["url"]
        method = args_name["request"]["method"]
        data = args_name["request"]["data"]
        data.update({"csrf_token": read_yaml("csrf_token")})
        headers = args_name["request"]["headers"]
        res = RequestUtil.send_request(method=method, url=url, datas=data, headers=headers)
        print(res.json())
