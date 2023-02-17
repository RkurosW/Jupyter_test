from datetime import datetime, time

def get_first_drink_price(dt, coupon=False):
    if coupon:
        return 100
    else:
        t = dt.time()
        if t >=time(16, 0) and t <= time(17, 59):
            return 290
    return 490

happy_hour = datetime(2023, 2, 15, 17, 0, 0)
normal_hour = datetime(2023, 2, 15, 19, 0, 0)
print(get_first_drink_price(happy_hour, coupon=True))
print(get_first_drink_price(happy_hour))
print(get_first_drink_price(normal_hour, coupon=True))
print(get_first_drink_price(normal_hour))