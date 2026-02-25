"""
break 的作用：
- 立刻结束当前循环，不再执行后续循环内容。
"""

print("=== break 入门小程序 ===")
print("请输入内容，输入 q 退出程序。")

while True:
    text = input("请输入：").strip()

    if text == "q":
        print("收到 q，使用 break 退出循环。")
        break

    print("你输入的是：", text)

print("程序结束。")
