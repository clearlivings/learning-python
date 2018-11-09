curr_age = 23

user_input = int(input('猜我有多大！'))
if user_input == curr_age:
	print('你真聪明，猜对了！')
elif user_input > curr_age:
	print('猜小点')
else:
	print('猜大点')