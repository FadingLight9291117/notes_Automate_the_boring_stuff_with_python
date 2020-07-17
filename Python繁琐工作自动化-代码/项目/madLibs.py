#! python3

'''
 实践项目 8.9.2 疯狂填词
'''

import os

if not os.path.exists('./files'):
    os.mkdirs('./files')

file = open('./files/madLibs.txt', 'w')
file.write('The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.')
file.close()

# read text from file
file = open('./files/madLibs.txt')
text = file.read()
file.close()

# 输入
adjective = input('Enter an adjective:\n')
noun = input('Enter a noun:\n')
adverb = input('Enter an adverb:\n')
verb = input('Enter a verb:\n')

# 替换文本
text = text.replace('ADJECTIVE', adjective)\
        .replace('NOUN', noun)\
        .replace('ADVERB', adverb)\
        .replace('VERB', verb)

print(text)
file = open('./files/madLibs.txt', 'w')
file.write(text)
file.close()