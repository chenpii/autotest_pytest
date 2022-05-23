# import re
#
#
#
# class TestUser:
#     # # 访问首页接口
#     # def test_start(self):
#     #     url = "http://47.107.116.139/phpwind/"
#     #     # res = requests.request(method="get", url=url)
#     #     # 通过sess请求，就不用cookies
#     #     res = TestRequest.sess.request(method="get", url=url)
#     #     # print(res.text)
#     #     # 正则提取提取鉴权码
#     #     # re.search("正则表达式",res.text)
#     #     obj = re.search('name="csrf_token" value="(.*?)"', res.text)
#     #     # 取匹配到的第1个值
#     #     print(obj.group(1))
#     #     TestRequest.csrf_token = obj.group(1)
#     #
#     #     # # 提取cookies
#     #     # TestRequest.php_cookie = res.cookies
#     #
#     # # 登录接口
#     # def test_login(self):
#     #     url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
#     #     data = {
#     #         "username": "chenh",
#     #         "password": "chen0816php",
#     #         "csrf_token": TestRequest.csrf_token,  # 鉴权码，从首页获取
#     #         "backurl": "http://47.107.116.139/phpwind/",
#     #         "invite": ""
#     #     }
#     #     headers = {
#     #         "Accept": "application/json,text/javascript,/; q=0.01",
#     #         "X-Requested-With": "XMLHttpRequest"
#     #     }
#     #     # res = requests.request(method="post", url=url, data=data, headers=headers, cookies=TestRequest.php_cookie)
#     #     # 使用session请求
#     #     res = TestRequest.sess.request(method="post", url=url, data=data, headers=headers)
#     #     print(res.json())
