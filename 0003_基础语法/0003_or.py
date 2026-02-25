"""
or 的作用：
- 两个条件中只要有一个为 True，整体就是 True。
"""

print("=== or 逻辑判断小程序 ===")

is_vip_text = input("你是会员吗？(y/n)：").strip().lower()
coupon_text = input("你有优惠券吗？(y/n)：").strip().lower()

is_vip = is_vip_text == "y"
has_coupon = coupon_text == "y"

if is_vip or has_coupon:
    print("可以享受优惠。")
else:
    print("暂时不能享受优惠。")
