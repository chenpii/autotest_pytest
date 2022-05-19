# 全局前后置方法
import pytest


@pytest.fixture(scope="function")
def all_fixture():
    print("\nfixture:全局前置")
    yield
    print("\nfixture:全局后置")
