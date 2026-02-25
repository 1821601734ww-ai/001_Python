"""
elif 的作用：
- 在 if 条件不满足时，继续判断下一个条件。
"""

print("=== elif 入门小程序 ===")

score = int(input("请输入分数（0~100）："))

if score >= 90:
    print("等级：A")
elif score >= 60:
    print("等级：B")
else:
    print("等级：C")
