#!/user/bin/python3

'''
  This module opens and reading the txt file line by line and searching for matching text.
  The line which contains the matched text will be printed
'''

try:
    import re2 as re
except ImportError:
    import re
else:
    re.set_fallback_notification(re.FALLBACK_WARNING)


def search_regex(pattern, filename):
    with open(filename) as file:
        line = file.readline()
        cnt = 1
        while line:
            if re.search(pattern, line):
                print("The file {} line number {} is {}".format(filename, cnt, line, end=" "))
            line = file.readline()
            cnt += 1

def regex_reader(pattern, filename):
    if type(filename) == type(set()):
        for file in filename:
            search_regex(pattern, file)
    else:
        search_regex(pattern, filename)

