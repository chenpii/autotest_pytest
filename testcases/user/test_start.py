import re

import pytest

from common.request_util import RequestUtil
from common.yaml_util import write_yaml, read_testcase


class TestStart:
    # 访问首页接口
    @pytest.mark.parametrize("args_name", read_testcase("/user/start.yaml"))
    def test_start(self, args_name):
        url = args_name["request"]["url"]
        method = args_name["request"]["method"]
        res = RequestUtil.send_request(method=method, url=url)
        # 正则提取提取鉴权码：re.search("正则表达式",res.text)
        obj = re.search('name="csrf_token" value="(.*?)"', res.text)
        # 取匹配到的第1个值写入到yaml文件
        write_yaml({"csrf_token": obj.group(1)})
