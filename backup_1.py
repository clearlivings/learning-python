import os
import time

# 备份目标和目标的目录
source = ['"C:\\byte-of-python-chinese-edition.pdf"',
          '"C:\\Users\\zhangkexu\Desktop\\byte-of-python-chinese-edition.pdf"']
# 备份主目录
target_dir = 'E:\\python-learning\\backup'
# 重命名 年月日时分秒
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'
# 不存在目录则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# 分今天子目录
today = target_dir + os.sep + time.strftime('%Y%m%d')
# 当前时间命名
now = time.strftime('%H%M%S')
# 命名加注释以更容易理解备份的是什么
comment = input('Enter a comment --->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
# target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)
# 备份命令
zip_command = 'zip -r -v {0} {1}'.format(target, ' '.join(source))
print('Zip command is:')
print('Running')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


