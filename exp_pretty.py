#Author-Abhijit Nimbalkar & Sriman Kolachalam

with open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses.txt') as fin:    #Opening the expenses.txt file
    for line in fin:
        line_stripped_newline=line[0:len(line)-1]               #Stripping newline character from the each line read from the file
        line_to_print=line_stripped_newline.split(':')          #Splitting the strings by ':'
        print("{:>10}{}{:<10}{:10}{}".format(line_to_print[0],"  ",line_to_print[1],line_to_print[2],line_to_print[3],sep='\t'))#printing the string as per desired output
