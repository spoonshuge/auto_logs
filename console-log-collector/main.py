import re
import argparse

LOG = 'C:/Users/HPz420/Desktop/git/auto_logs/WebLogFile.log'

parser = argparse.ArgumentParser(description='your friendly neighborhood log collector')
parser.add_argument(
    '-m',
    '--match-string',
    help='string to match log lines on',
    required=False,
    default='Error',
)

args = parser.parse_args()


def is_line_dated(line_to_check):
    if re.match('^[0-9]{4}/[0-9]{2}/[0-9]{2}\s.+', line_to_check):
        return True
    return False


with open(LOG, 'r') as f:
    lines = f.readlines()
    print(len(lines))
    line_after = False
    for line in lines:
        if args.match_string in line:
            print(line)
            line_after = True
            continue
        if line_after == True:
            if is_line_dated(line) == True:
                line_after = False
                continue
            print(line)
