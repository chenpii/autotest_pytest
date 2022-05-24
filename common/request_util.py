# 处理请求的包
import json

import requests


# 封装就意味着，这个方法要适应所有的请求
class RequestUtil:
    # 全局变量,类变量
    sess = requests.session()

    @classmethod
    def send_request(self, method, url, datas=None, **kwargs):
        method = str(method).lower()
        res = None
        if method == "get":
            res = RequestUtil.sess.request(method=method, url=url, params=datas, **kwargs)
        elif method == "post":
            if datas and isinstance(datas, dict):
                datas = json.dumps(datas)
            res = RequestUtil.sess.request(method=method, url=url, data=datas, **kwargs)
        else:
            pass

        return res
