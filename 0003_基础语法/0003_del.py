"""
del 的作用：
- 删除变量或列表中的元素。
"""

print("=== del 入门小程序 ===")

fruits = ["苹果", "香蕉", "橙子"]
print("删除前：", fruits)

del fruits[1]  # 删除索引 1 的元素（香蕉）
print("删除后：", fruits)
