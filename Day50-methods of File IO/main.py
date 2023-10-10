#Readlines
'''f = open('Day50-methods of File IO/myfile.txt', 'r')
while True:
    line = f.readline() #reading from file until there are lines and returns them as a list of strings.
    if not line:
        break
    print(line)
    # readlines are used in ML
    '''

#writeline
f = open('Day50-methods of File IO/myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
