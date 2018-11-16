def change(x, y):
    """Prints the maximum of two numbers.打印两个数值中的最大数。

    The	two	values must be integers.这两个数都应该是整数"""
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is max')
    else:
        print(y, 'is max')


help(change)
change(2, 6)
print(change.__doc__)
