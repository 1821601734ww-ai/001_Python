"""
except 的作用：
- 捕获并处理 try 中发生的异常，避免程序直接崩溃。
"""

print("=== except 入门小程序 ===")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("捕获到异常：除数不能为 0。")

print("程序继续执行。")
