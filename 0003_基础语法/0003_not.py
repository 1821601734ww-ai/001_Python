print("=== not 逻辑判断小程序 ===")

answer = input("你已经登录了吗？(y/n)：").strip().lower()
is_login = answer == "y"

if not is_login:
    print("你还没有登录，请先登录。")
else:
    print("欢迎回来，登录成功。")
