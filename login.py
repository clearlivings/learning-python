import getpass

name = input('请输入用户名:')
pas = getpass.getpass('请输入密码:')
if name == 'aa' and pas == '222':
    print('登录成功')
else:
    print('用户名或密码不正确')
