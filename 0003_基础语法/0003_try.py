"""
try 的作用：
- 先尝试执行可能出错的代码。
"""

print("=== try 入门小程序 ===")

try:
    num = int(input("请输入一个数字："))
    print("你输入的是：", num)
except ValueError:
    print("输入错误：请输入数字。")
