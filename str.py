ss = '''
css world async svn 
is man is shy
test guess ddd
'''
print(ss)
# 格式化方法 format()
name = 'jack'
age = 45
print('{} was {} years old where is from Hangzhou'.format(name, age))
print('{} is man'.format(name))
print(name + 'is' + str(age) + 'years old')
# 0.333
print('{0:.3f}'.format(1.0/3), end='')
# ___hello___
print('{0:_^11}'.format('hello'), end='')
print('{name} wrote {book}'.format(name='rick', book='a byte of python'))
# 转义序列
print('what\'s your name?')
print("what\'s \"your name?")
print('this is python demo\nthis is good book')
print('this is my pc. \t '
      'this is the second sentence')
print(r"Newlines	are	indicated	by	\n")
print('\\1', r'\1')
# 运算符
print(3**4)
print(1/3)
# while
number = 21
running = True
while running:
    guess = int(input('please input integer:'))
    if guess == number:
        print('congratulations you guessed it.')
        running = False
    elif guess < number:
        print('guess bigger.')
    else:
        print('guess smaller.')
else:
    print('this while loop is over.')
print('Done')
# for 循环
for i in range(1, 5):
    print(i)
else:
    print('the for loop is over')


