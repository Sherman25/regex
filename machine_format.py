#!/user/bin/python3

'''
  This extra parameter module opens and reading the txt file line by line 
  and searching for matching text. The output will be in machine format
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
            is_match = False
            for m in re.finditer(pattern, line):
                print("{}:{}:{}".format(filename, cnt, '%02d:%s' % (m.start(), m.group(0))), end=" ")
                is_match = True
            if is_match:
                is_match = False
                print()
            line = file.readline()
            cnt += 1

  
def machine_reader(pattern, filename):
    if type(filename) == type(set()):
        for file in filename:
            search_regex(pattern, file)
    else:
        search_regex(pattern, filename)

