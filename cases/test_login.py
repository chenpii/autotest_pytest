import pytest


def test_fi01():
    print("测试函数01")
    assert 1 == 2


class TestLogin:
    age = 18

    # 标记执行顺序
    @pytest.mark.run(order=1)
    def test_01(self):
        print("测试方法01")

    # 标记成冒烟用例
    @pytest.mark.smoke
    def test_02(self):
        print("测试方法02")

    # 标记成模块用例
    @pytest.mark.usermanage
    def test_03(self):
        print("测试方法03")

    # 标记成无条件跳过
    @pytest.mark.skip(reason="还没调试好")
    def test_04(self):
        print("测试方法04")

    # 标记成有条件跳过
    @pytest.mark.skipif(age >= 18, reason="已成年，不执行")
    def test_05(self):
        print("测试方法05")
