x = 25


def landing():
    global x
    print(x)
    x = 65
    print('changed local x to', x)


landing()
print('x', x)

