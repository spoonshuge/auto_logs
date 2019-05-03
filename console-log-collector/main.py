import re

LOG = 'C:/Users/HPz420/Desktop/git/auto_logs/WebLogFile.log'

def is_line_dated(line_to_check):
    if re.match('^[0-9]{4}/[0-9]{2}/[0-9]{2}\s.+', line_to_check):
        return True
    return False

# print(is_line_dated('2019/04/22 04:37:58.107	UEM-CONSOLE	4'))

with open(LOG, 'r') as f:
    lines = f.readlines()
    print(len(lines))
    lineafter = False
    for line in lines:
        if 'Error' in line:
            print(line)
            lineafter = True
            continue
        if lineafter == True:
            if is_line_dated(line) == True:
                lineafter = False
                continue
            print(line)
        #     if is_line_dated(line) == False:
        #         print(line)
        #     lineafter = False


