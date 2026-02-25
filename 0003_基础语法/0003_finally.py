"""
finally 是什么？
- finally 代码块不管程序是否报错，最后都会执行。
- 常用于“收尾动作”，比如：关闭文件、关闭连接、释放资源。
"""

print("=== finally 入门小程序 ===")

try:
    num_text = input("请输入一个数字（试试输入 0）：")
    num = int(num_text)
    result = 10 / num
    print("计算结果是：", result)
except ZeroDivisionError:
    print("发生错误：除数不能为 0。")
except ValueError:
    print("发生错误：你输入的不是数字。")
finally:
    print("finally：这句话一定会执行。")
