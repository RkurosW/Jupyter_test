def get_discount(items):
    percentage = 0.00
    if len(items) >= 7:
        percentage += 0.07
    
    if 'shirt' in items:
        if 'necktie' in items:
            percentage += 0.05
    
    return percentage

items = ['necktie', 'shirt', 'jacket', 'handkerchief', 'pants', 'shoes', 'belt', 'sox']

print(get_discount(items)) # 0.12
print(get_discount(items[1:])) # 0.07
print(get_discount(items[:2])) # 0.05
print(get_discount(items[-3:])) # 0.00