#!/usr/bin/python3
 """
        A function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file
    Returns:
        Nothing
    """
def read_file(filename=""):
    with open('workfile', encoding="utf-8") as f:
        print(f, end="")
