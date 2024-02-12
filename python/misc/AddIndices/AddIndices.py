with open('output.txt', 'w') as outFile:
    # clear previous run
    outFile.write('\n')
with open('input.txt', 'r') as decFile:
    for line in decFile:
        if '(' in line:
            newline = line.split('(')[0] + '(int i, int j, int k, ' + line.split('(')[1] + '\n'
            with open('output.txt', 'a') as outFile:
                outFile.write(newline)

