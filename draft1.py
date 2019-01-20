import errno
import glob  # glob module finds all the path names matching a specified pattern

path = '/Users/naila/Desktop/WP_tables/tables_redi2_1/*.json'
files = glob.glob(path)
for name in files:
    try:
        with open(name) as f:  # opens the files and read them
            corpus = f.read()

            row = len(corpus)
            print(row)

            column = len(corpus[0])
            print(column)

    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise


















