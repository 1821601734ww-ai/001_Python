"""
from 的常见用法：
- from 模块名 import 名称
- 作用：从模块中只导入你需要的内容

random 模块是什么？
- random 是 Python 标准库中的“随机数模块”。
- 它可以用来生成随机整数、随机小数、随机选择元素、打乱顺序等。
- 本例使用的是 randint(a, b)：返回 a 到 b（包含两端）的随机整数。
"""

# 从 random 模块里导入 randint 函数
from random import randint

print("=== from import 入门小程序 ===")
print("随机生成 1 到 10 的数字。")

num = randint(1, 10)
print("本次随机数是：", num)
