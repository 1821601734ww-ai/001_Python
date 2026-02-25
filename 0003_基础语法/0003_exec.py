"""
exec() 是什么？
- exec() 可以把“字符串形式的 Python 代码”当成真正代码执行。
- 常见写法：exec(代码字符串, 全局命名空间, 局部命名空间)
- 本示例使用一个字典 scope 接收 exec 内部产生的变量，方便在外部读取。
"""

print("=== exec() 入门小程序 ===")
print("说明：exec 会执行字符串代码，下面演示如何读取执行结果。")

# 1) 要执行的 Python 代码（字符串）
# 这段多行字符串里的内容会被 exec 当作代码执行
code_text = """
a = 10
b = 20
result = a + b
print("在 exec 内部计算：", result)
"""

# 2) 准备一个“命名空间字典”接收 exec 里创建的变量
# exec 运行后，a / b / result 会被放到 scope 里
scope = {}

# 3) 执行字符串代码
# 第1个参数：代码字符串
# 第2个参数：全局命名空间（这里给空字典）
# 第3个参数：局部命名空间（这里用 scope 来接收变量）
exec(code_text, {}, scope)

# 4) 在 exec 外部读取 exec 里产生的变量
print("在 exec 外部读取 result：", scope["result"])
