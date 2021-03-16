#!/user/bin/python3

'''
  This is the main script that reading the system input, trimming and executing the module that parsing the input
'''

import sys


from args_parser import parse_input
def main():
    # read commandline arguments, first
    fullCmdArguments = sys.argv

    # - further arguments
    argumentList = fullCmdArguments[1:]

    # process the input
    parse_input(argumentList)

main()


