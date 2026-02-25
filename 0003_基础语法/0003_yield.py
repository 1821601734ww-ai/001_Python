"""
yield 的作用：
- 把函数变成“生成器”，一次返回一个值，节省内存。
"""

print("=== yield 入门小程序 ===")


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1


for num in count_up_to(5):
    print("生成器返回：", num)
