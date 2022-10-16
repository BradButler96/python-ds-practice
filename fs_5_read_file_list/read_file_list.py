def read_file_list(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """

    # hint: when you read lines of files, there will be a "newline"
    # (end-of-line character) at the end of each line, and you want to
    # strip that off before you print it. Do some research on that!

    f = open(filename, 'r')
    f_lines = f.readlines()
    new_lines = []
    if f_lines[0][0] != '-':
        for line in f_lines:
            new_line = '- ' + line
            new_lines.append(new_line)

        f = open(filename, 'w')
        for line in new_lines:
            f.write(line)
        f.close()
        f_read = open(filename, 'r')
        print(f_read.read())
    else:
        f = open(filename, 'r')
        print(f.read())