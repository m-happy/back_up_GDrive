import os
import time
#input for the source file to be backed
__source = input("Enter the path to directory to be backed up : ")
__source = '../' + __source
source = [__source]
#target for the source file where source file should be backed
target_dir = input("Enter the directory in which the files to backed up : ")
target_dir = '../' + target_dir

#add a comment to differentiate the folder
comment = input("Enter a commnet added to file : ")
if len(comment) == 0:
	target = target_dir + os.sep + time.strftime('%Y_%m_%d_%H_%M_%S') + '.zip'
else:
	target = target_dir + os.sep + time.strftime('%Y%m%d') + comment.replace(' ', '_') + time.strftime('%H_%M_%S') + '.zip'
#create a directory if directory doesn't exists
if not os.path.exists(target_dir):
	os.mkdir(target_dir)  #make directory
#zip command
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
#Run the backup

print('Running')
if os.system(zip_command) == 0:
	print('successful backup to : ', target)
else:
	print('Backup failed')
