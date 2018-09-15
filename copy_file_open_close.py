
# File: copy_file_open_close.py

fin = open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses.txt',  # pathname
           'rt',                 # read text
           encoding = 'utf-8')   # Unicode,
                                 # with ASCII
fout = open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses_copy1.txt',
            'wt',                # write text
            encoding = 'utf-8')
for line in fin:  # line is a str
    fout.write(line)

fin.close()    # so you can open again later
fout.close()   # do not forget!

