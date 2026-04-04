def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        txt = f.readlines()
        lines = len(txt)
        chars = sum(len(line) for line in txt)
        words = sum(len(line.split()) for line in txt)
        return f'{lines} {words} {chars} {file_}'


if __name__ == '__main__':
    import sys
    print(wc(sys.argv[1]))