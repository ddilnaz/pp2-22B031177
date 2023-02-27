import re
#input
string=str(input())
#Find the words in string starting with uppercase letter. 
words = re.findall('[A-Z][a-z]*', string)
#concatenate the word with space
print(' '.join((words)))