"""
with 的作用：
- 自动管理资源（如文件），用完会自动关闭。
"""

print("=== with 入门小程序 ===")

with open("demo.txt", "w", encoding="utf-8") as f:
    f.write("这是 with 写入的一行文本。")

with open("demo.txt", "r", encoding="utf-8") as f:
    content = f.read()

print("读取到的内容：", content)
