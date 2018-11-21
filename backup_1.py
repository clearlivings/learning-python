import os
import time

# ����Ŀ���Ŀ���Ŀ¼
source = ['"C:\\byte-of-python-chinese-edition.pdf"',
          '"C:\\Users\\zhangkexu\Desktop\\byte-of-python-chinese-edition.pdf"']
# ������Ŀ¼
target_dir = 'E:\\python-learning\\backup'
# ������ ������ʱ����
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'
# ������Ŀ¼�򴴽�
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
# �ֽ�����Ŀ¼
today = target_dir + os.sep + time.strftime('%Y%m%d')
# ��ǰʱ������
now = time.strftime('%H%M%S')
# ������ע���Ը�������ⱸ�ݵ���ʲô
comment = input('Enter a comment --->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
# target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)
# ��������
zip_command = 'zip -r -v {0} {1}'.format(target, ' '.join(source))
print('Zip command is:')
print('Running')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')


