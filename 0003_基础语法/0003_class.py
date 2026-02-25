"""
class 入门示例：
- class 用来描述一类事物（例如“学生”）。
- 对象是 class 创建出来的具体实例。

本文件重点说明：
1) self：代表“当前对象自己”
2) __init__：创建对象时自动执行的初始化方法
3) f"...{变量}..."：格式化字符串（f-string），可把变量值直接放进字符串
"""


class Student:
    # __init__ 是构造方法：创建对象时自动执行
    # self 代表“当前这个对象自己”
    def __init__(self, name, age):
        # self.name / self.age 是“对象自己的属性”
        # 不同对象的属性值可以不同
        self.name = name
        self.age = age

    # 对象方法：每个学生对象都可以调用
    def introduce(self):
        # f"..." 是格式化字符串（f-string）
        # {self.name} 和 {self.age} 会被替换成真实值
        print(f"大家好，我叫{self.name}，今年{self.age}岁。")


print("=== class 入门小程序 ===")

# 创建两个学生对象
# 这里会自动调用 __init__(self, name, age)
s1 = Student("小明", 18)
s2 = Student("小红", 17)

# 调用对象方法
s1.introduce()
s2.introduce()
