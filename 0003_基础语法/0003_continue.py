"""
continue 的作用：
- 跳过本次循环后面的代码，直接进入下一次循环。
"""

print("=== continue 入门小程序 ===")
print("打印 1 到 10 中的奇数（跳过偶数）。")

for num in range(1, 11):
    if num % 2 == 0:
        # 如果是偶数，跳过本次循环
        continue

    print("奇数：", num)

print("程序结束。")
