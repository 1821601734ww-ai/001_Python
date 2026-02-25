"""
print 常见用法示例

重点说明 end 参数：
- end 表示“这次 print 结束后，末尾放什么字符”
- 默认是换行符 \n，所以 print 通常会自动换行
- 若写 end=""，表示不换行，下一次输出会接在后面
"""

name = "小明"
age = 18
score = 95.5

print("=== print 入门小程序 ===")

# 1) 最基础输出
print("你好，Python！")

# 2) 输出多个值（默认用空格隔开）
print("姓名：", name, "年龄：", age)

# 3) sep 参数：设置多个值之间的分隔符
print("2026", "02", "25", sep="-")

# 4) end 参数：设置本次 print 的结尾（默认是换行）
# 默认相当于 end="\n"
print("这句话不换行，", end="")
print("会接在后面。")

# 再看一个 end 的例子：让 1~5 显示在同一行
print("数字演示：", end="")
for i in range(1, 6):
    print(i, end=" ")
print()  # 单独 print() 用来换行

# 5) f-string 格式化输出（推荐）
print(f"{name} 的成绩是 {score} 分。")
