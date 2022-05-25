# 用户管理前后置方法
import pytest


@pytest.fixture(scope="function")
def user_fixture():
    print("\nfixture:用户管理前置")
    yield
    print("\nfixture:用户管理后置")
