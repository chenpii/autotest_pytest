import pytest


def test_fix():
    print("测试函数")
    assert 1 == 2


class TestLogin:

    @pytest.mark.smoke
    def test_01(self):
        print("登录测试方法01")
    @pytest.mark.usermanage
    def test_02(self):
        print("登录测试方法02")

    def test_03(self):
        print("登录测试方法03")

    def test_04(self):
        print("登录测试方法04")
