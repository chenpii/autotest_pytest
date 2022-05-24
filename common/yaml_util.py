# 操作yaml的工具包

# 读取
import os

import yaml


def read_yaml(key):
    with open(os.getcwd() + "/extract.yaml", mode="r", encoding="utf-8") as f:
        # FullLoader 全局加载
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 写入
def write_yaml(data):
    # 以追加的模式打开，编码格式为utf-8
    with open(os.getcwd() + "/extract.yaml", mode="a", encoding="utf-8") as f:
        yaml.dump(data, stream=f, allow_unicode=True)


# 清空
def clean_yaml():
    # 以追加的模式打开，编码格式为utf-8
    with open(os.getcwd() + "/extract.yaml", mode="w", encoding="utf-8") as f:
        f.truncate()
