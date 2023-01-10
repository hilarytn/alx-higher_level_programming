#!/usr/bin/python3
def read_file(filename=""):
    """
        A function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file
    Returns:
        Nothing
    """
    with open('workfile', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
