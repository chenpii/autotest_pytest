# 获取token接口类

import requests

from TestConfig import TestConfig


class GetTokenApi():
    uri = "easytong_app/api/token"

    @classmethod
    def getResult(self, appid: str, appsecret: str):
        #  实例化configParser对象

        url = TestConfig.url + self.uri
        params = {"appid": appid,
                  "appsecret": appsecret}
        request = requests.get(url=url, params=params)
        result = request.json()
        return result
