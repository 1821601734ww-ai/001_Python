"""
raise 的作用：
- 主动抛出一个异常（错误），让程序进入异常处理流程。
"""

print("=== raise 入门小程序 ===")

age_text = input("请输入年龄：")
age = int(age_text)

if age < 0 or age > 120:
    # 年龄不合理时，主动抛出 ValueError
    raise ValueError("年龄必须在 0 到 120 之间。")

print("年龄输入合法：", age)
