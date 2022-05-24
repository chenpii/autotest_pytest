# 测试加签
import hashlib


def get_sign(data: dict, key: str):
    keys = sorted(data.keys())
    string = ""
    for k in keys:
        value = ""
        if data.get(k):
            value = str(data.get(k))
        string += k + "=" + value + "&"
    string += "key=" + key
    sign = get_md5(string)
    return sign


def get_md5(sinBody):
    # 1- 实例化加密对象
    md5 = hashlib.md5()
    # 2- 进⾏加密操作
    md5.update(sinBody.encode('gbk'))
    # 3- 返回加密后的结果
    return md5.hexdigest()


if __name__ == '__main__':
    # epId：1
    # fixType：1
    # areaNums：
    # str:areaNums=&epId=1&fixType=1&
    # key:8627E1958EE45E374E88C2118CF920E9
    # dst:areaNums=&epId=1&fixType=1&key=8627E1958EE45E374E88C2118CF920E9
    # sign:2f121a9ac8dfe18d6feefb5659c92613

    data = {
        "epId": 1,
        "fixType": 1,
        "areaNums": None
    }
    key = "8627E1958EE45E374E88C2118CF920E9"
    sign = get_sign(data, key)
    print(sign)
