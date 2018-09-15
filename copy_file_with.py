
# File: copy_file_with.py

with open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses.txt', 'rt',
          encoding = 'utf-8') as fin:
    with open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses_copy2.txt', 'wt',
              encoding = 'utf-8') as fout:
        for line in fin:
            fout.write(line)

# close of fin and fout is automatic!
