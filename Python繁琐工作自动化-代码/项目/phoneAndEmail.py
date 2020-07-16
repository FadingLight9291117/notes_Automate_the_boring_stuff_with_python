#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

###########################################
#   7.15 项目：电话号码和Email地址提取程序  #
###########################################

import pyperclip
import re

# create phone regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                      # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

# create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # usename
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name
    (\.[a-zA-Z]{2,4})       # dot-something
)''', re.VERBOSE)

# find matches in clipboard text.
text = pyperclip.paste()
matches = []
for group in phoneRegex.findall(text):
    phone = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phone += ' x' + group[8]
    matches.append(phone)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
else:
    print("No phone numbers or email address found.")
