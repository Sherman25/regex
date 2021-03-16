#!/user/bin/python3

'''
  This extra parameter module opens and reading the txt file line by line 
  and searching for matching text. The line which contains the matching 
  text will be printed with '^' underline the matched text.
'''

try:
    import re2 as re
except ImportError:
    import re
else:
    re.set_fallback_notification(re.FALLBACK_WARNING)


def search_regex(pattern, filename):
    name_len = len(filename)
    with open(filename) as file:
        line = file.readline()
        cnt = 1
        while line:
            is_match = False
            indent = 26 + name_len + len(str(cnt))
            new_line = [' '] * (len(line) + indent) # 
            for m in re.finditer(pattern, line):
                for index in range(indent + m.start(), indent + m.end()):
                   new_line[index] = '^'
                is_match = True
            if is_match:
                is_match = False
                print("The file {} line number {} is {}".format(filename, cnt, line[:-1], end=" "))
                print("".join(new_line))
            line = file.readline()
            cnt += 1

   
def underline_reader(pattern, filename):
    if type(filename) == type(set()):
        for file in filename:
            search_regex(pattern, file)
    else:
        search_regex(pattern, filename)
    


