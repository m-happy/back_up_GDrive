import os
import time
source = ['../learning']
target_dir = '../../cpp'
# os.mkdir(target_dir)
comment = input("Enter a commnet added to file : ")
if len(comment) == 0:
	target = target_dir + os.sep + time.strftime('%Y_%m_%d_%H_%M_%S') + '.zip'
else:
	target = target_dir + os.sep + time.strftime('%Y%m%d') + comment.replace(' ', '_') + time.strftime('%H_%M_%S') + '.zip'
#create a directory if directory doesn't exists
if not os.path.exists(target_dir):
	os.mkdir(target_dir)  #make directory
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
#Run the backup
print('zip command is : ')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
	print('successful backup to : ', target)
else:
	print('Backup failed')
