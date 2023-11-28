#!/usr/bin/python3

"""

The module as a function that indent text

"""

def text_indentation(text):
    '''This function prints the text with 2 new lines after each of ".", "?", or ":"

    Args:
        text: It string to be printed

    Raises:
        TypeError: If the text is not the string

    '''


    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
