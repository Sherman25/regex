#!/user/bin/python3

'''
  This module is parsing the list of input arguments. 
  According to format, sequence and correctness of the arguments, the module
  will either send an Error message or call proper module to process the text.
'''

from regex import regex_reader
from underline_text import underline_reader
from color_text import color_reader
from machine_format import machine_reader


def parse_input(argumentList):
    ''' The function parsing the input arguments '''
    if len(argumentList) < 3:
        print("Incorrect input - Not enough arguments")
    elif len(argumentList[1]) is 0:
        print("The pattern is too short")
    else:
        if not argumentList[0] in ("-r", "--regex"):
            print("Incorrect input")
        elif argumentList[2] in ("-f", "--files"):
            if len(argumentList) > 3 and not is_extra_parameter(argumentList[3]):
                list_of_files, flag = get_all_files(argumentList, 3)
                if len(argumentList) > (flag + 3):
                    var = is_extra_parameter(argumentList[flag + 3])
                    if var:
                        run_with_extra(argumentList[1], list_of_files, var)
                    else:
                        print("The extra parameter is invalid")
                else:
                    regex_reader(argumentList[1], list_of_files)    
            else:
                 # The list of files was not provided 
                 print("No files to read")  
        else:
            if len(argumentList) > 3:
                # Parameter was entered after the only "txt" file we expecting
                # to receive. We will check the correctness of this parameter. 
                var = is_extra_parameter(argumentList[3])
                if var:
                    # The parameter is an extra parameter. We will parse and print
                    # the text in format according to parameter
                    run_with_extra(argumentList[1], argumentList[2], var)
            else:
                regex_reader(argumentList[1], argumentList[2]) 

 
def run_with_extra(pattern, file, param):
    # This function will be called if there is an EXTRA parameter
    # According to parameter the proper function will be called
    if param == "underline": 
        underline_reader(pattern, file)
    elif param == "color": 
        color_reader(pattern, file)
    else:
        machine_reader(pattern, file)

        
def is_extra_parameter(arg):
    # Checking the correctness of the extra parameter
    if arg in ("-u","--underline"):
        return "underline"
    elif arg in ("-c", "--color"):
        return "color"
    elif arg in ("-m","--machine"):
        return "machine"
    else: 
        #print("The extra parameter is invalid")
        return False


def get_file(arguments, i):
    # Returns the correct txt file or False if file is not txt
    if len(arguments) > i and not is_extra_parameter(arguments[i]):
        return arguments[i]
    else:        
        return False


def get_all_files(arguments, i):
    # The function will be used with -f|--files parameter
    # Returns the set of txt files.
    files_set = set()
    file = get_file(arguments, i)
    cnt = 0 # This variable will help to know where to proceed reading the input
    while file:
        files_set.add(file)
        i += 1
        cnt += 1
        file = get_file(arguments, i)
    return files_set, cnt
