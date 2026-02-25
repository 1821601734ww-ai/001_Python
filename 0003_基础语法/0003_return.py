"""
return 的作用：
- 把函数里的结果“返回”给函数外部使用。
"""

print("=== return 入门小程序 ===")


def add(a, b):
    return a + b


result = add(3, 5)
print("3 + 5 =", result)
