"""
is 的作用：
- 判断两个变量是否指向同一个对象（身份比较）。
"""

print("=== is 入门小程序 ===")

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)  # True，同一个对象
print("a is c:", a is c)  # False，不是同一个对象
print("a == c:", a == c)  # True，内容相同
