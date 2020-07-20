#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

'''
项目9.5 将一个文件夹备份到一个zip文件
'''

import os
import zipfile


def backupToZip(folder):
    # 将folder中的内容备份到ZIP文件
    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exists.
    # 检查文件名是否已存在
    number = 1
    while True:
        zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(os.path.join(os.path.dirname(folder), zipFileName)):
            break
        number += 1

    # create the zip file
    print('Create {}...'.format(zipFileName))
    backupZip = zipfile.ZipFile(os.path.join('项目', 'files', zipFileName), 'w')

    # 压缩整个文件夹必须递归地一个一个压缩文件，否则只压缩文件夹得到的是空文件
    # walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in {}...'.format(foldername))
        # Add the current folder to the Zip file
        backupZip.write(foldername)
        
        # Add all files in this folder to the ZIP file.
        for filename in filenames:
            backupZip.write(os.path.join(foldername, filename))
            

    backupZip.close()
    print('Done.')


backupToZip('项目/files')
