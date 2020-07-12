#! python3
# pw.py - An insecure password locker program.

############################
#    6.3 项目 口令保管箱    #
###########################

PASSWORDS = {'email': 'F123@213132',
             'blog': '123fdaf',
             'luggage': '123456'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name.

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for \'' + account + '\' copied to clipboard.')
else:
    print('There is no account named \'' + account + '\'')