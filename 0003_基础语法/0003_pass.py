"""
pass 的作用：
- 什么都不做，只是占一个位置。
- 常用于先搭代码结构，后面再补实现。
"""

print("=== pass 入门小程序 ===")

score = int(input("请输入分数（0~100）："))

if score < 0 or score > 100:
    print("分数不合法。")
elif score >= 60:
    print("成绩及格。")
else:
    # 这里先不处理不及格逻辑，先占位
    pass

print("程序执行结束。")
