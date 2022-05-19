# 商品管理前后置方法
import pytest


@pytest.fixture(scope="function")
def product_fixture():
    print("\nfixture:商品管理前置")
    yield
    print("\nfixture:商品管理后置")
