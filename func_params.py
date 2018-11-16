def print_max(a, b):
    if a > b:
        print(a, ' is maximum')
    elif a < b:
        print(b, 'is maximum')
    else:
        print(a, 'is equal to', b)

# 字面量形式传参


print_max(5, 6)

x = 9
y = 10
# 参数形式传递变量
print_max(x, y)

