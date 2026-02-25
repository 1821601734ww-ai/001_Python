"""
for 的作用：
- 按顺序遍历一个序列（如 range、列表、字符串）。
"""

print("=== for 入门小程序 ===")
print("打印 1 到 10，并计算总和。")

total = 0

for num in range(1, 11):  # 1 到 10
    print("当前数字：", num)
    total += num

print("1 到 10 的总和是：", total)
