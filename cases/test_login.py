import pytest


def test_fi01():
    print("测试函数01")
    assert 1 == 2


class TestLogin:
    age = 18

    def setup_class(self):
        print("\n在每个类执行前的初始化工作：比如：创建日志对象、创建数据库连接、创建接口请求对象")

    def setup(self):
        print("\n执行测试用例之前初始化：打开浏览器，加载网页")

    # 标记执行顺序
    @pytest.mark.run(order=1)
    def test_01(self):
        print("\n测试方法01")

    # 标记成冒烟用例
    @pytest.mark.smoke
    def test_02(self):
        print("\n测试方法02")

    # 标记成模块用例
    @pytest.mark.login
    def test_03(self):
        print("\n测试方法03")

    # 标记成无条件跳过
    @pytest.mark.skip(reason="还没调试好")
    def test_04(self):
        print("\n测试方法04")

    # 标记成有条件跳过
    @pytest.mark.skipif(age >= 18, reason="已成年，不执行")
    def test_05(self):
        print("\n测试方法05")

    def teardown(self):
        print("\n执行测试用例后的扫尾工作：关闭浏览器")

    def teardown_class(self):
        print("\n在每个类执行后的扫尾工作：比如：销毁日志对象、断开数据库连接、销毁接口请求对象")
