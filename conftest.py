# 全局前后置方法
import pytest

from common.yaml_util import clean_yaml


@pytest.fixture(scope="function")
def all_fixture():
    print("\nfixture:全局前置")
    yield
    print("\nfixture:全局后置")


# 在所有的接口请求之前执行。
@pytest.fixture(scope="session", autouse=True)
def clean_extract():
    clean_yaml()
