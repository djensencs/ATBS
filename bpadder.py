#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "line" list
    lines[i] = '*' + lines[i]  # add '*' to each line in the lines list   
text = '\n'.join(lines)        # add each lines list item to a text string
pyperclip.copy(text)
print(text)


