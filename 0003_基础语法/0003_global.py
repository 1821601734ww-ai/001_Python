"""
global 的作用：
- 在函数内部声明“我要使用并修改全局变量”。
- 不写 global 时，在函数里给同名变量赋值会变成“局部变量”。
"""

print("=== global 入门小程序 ===")

# 全局变量（函数外定义）
count = 0


def add_one():
    global count  # 声明：这里的 count 是全局变量
    count = count + 1
    print("函数内 count =", count)


print("调用函数前，count =", count)
add_one()
add_one()
print("调用函数后，count =", count)
