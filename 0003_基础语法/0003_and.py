print("=== 办理业务资格判断 ===")

age_text = input("请输入你的年龄：")
has_id_text = input("你有身份证吗？(y/n)：")

age = int(age_text)
has_id = has_id_text.lower() == "y"

if age >= 18 and has_id:
    print("可以办理业务。")
else:
    print("暂时不能办理业务。")
