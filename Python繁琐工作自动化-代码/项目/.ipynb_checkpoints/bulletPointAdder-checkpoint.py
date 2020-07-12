#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

#####################################
#  6.4 项目 在Wiki标记中添加无序列表  #
#####################################

import pyperclip

text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
lines = list(map(lambda line: '*' + line, lines))

# Join the lines
text = '\n'.join(lines)

pyperclip.copy(text)