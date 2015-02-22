import re

f = open('temp/test.txt')

line = f.readline()

if (re.match('.*version 1.*', line)):
    exit(0)
else:
    exit(1)

