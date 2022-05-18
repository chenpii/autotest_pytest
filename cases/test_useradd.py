import pytest


@pytest.fixture()
def my_fixture():
    print("这是前后置的方法，可以实现部分以及全部用例的前后置")


class TestUser:

    def test_06(self):
        print("\n测试方法06")

    def test_07(self):
        print("\n测试方法07")

    def test_08(self):
        print("\n测试方法08")
