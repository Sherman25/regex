# regex
 A Python3 script which searches for a pattern using a regular expression in lines of text, 
  and prints the lines which contain matching text. 
  Output format: "file_name line_number line"

How to run:
  Compile the main.py file by running: python3 main.py and provide arguments and parameters.
  
  The script accepts the following parameters:
    -r, --regex     - the regular expression to search for.
    -f, --files     - a list of files to search in. If this parameter is omitted, 
                      the script expects text input from STDIN.

  These extra parameters are mutually exclusive:
    -u, --underline - "^" is printed underneath the matched text.
    -c, --color     - the matched text is highlighted in RED color.
    -m, --machine   - print the output in the format: 
                      "file_name:line_number:start_position:matched_text".

  Note: It is recommended to run and provide arguments in the CORRECT form.
  Examples of the correct input:
    -r|--regex "some pattern" "filename.txt" -u|--color|-m
    -r|--regex "some pattern" -f|--files "file1.txt" "file2.txt" ... "fileN.txt" --underline|-c|--machine
