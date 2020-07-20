#!python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

'''
项目9.4 将带有美国风格日期的文件名改为欧洲风格日期
'''

import os, shutil, re
import random

# create a regex that matches files with the American date format.
dataPattern  = re.compile(r'''^(.*?)    # all text before the date
    ((0|1)?\d)-                         # one or two digits for the month
    ((0|1|2|3|)?\d)-                    # one or two digits for the day
    ((19|20)\d\d)                       # four digits for the year
    (.*?)$                              # all text after the date 
''', re.VERBOSE)                        # ignore all the space of regex

# remove files before created.
removeRex = re.compile(r'^(file)')
for filename in os.listdir('./项目/files'):
    mo = removeRex.search(filename)
    if mo != None:
        os.remove(os.path.join('.', '项目', 'files',filename))
# create some files with American date
for i in range(3):
    open('./项目/files/file{}-{}-{}file.txt'.format('0' + str(random.randint(1, 9)), \
         random.randint(1, 29), random.randint(1900, 2100)), 'w') \
        .close()

# loop over the files in the working directory.
for filename in os.listdir('./项目/files'):
    mo = dataPattern.search(filename)
    # skip file without a date
    if mo == None:
        continue
    else:
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        datePart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)
        # form the European-style filename.
        euroFileName = beforePart + datePart + '-' + monthPart + '-' + yearPart + afterPart
        # Get the full, absolute file paths.
        absWorkDir = os.path.abspath(os.path.join('.', '项目', 'files'))
        amerFileName = os.path.join(absWorkDir, filename)
        euroFileName = os.path.join(absWorkDir, euroFileName)

        # rename all files
        print('Renaming {} to {}'.format(amerFileName, euroFileName))
        shutil.move(amerFileName, euroFileName)
