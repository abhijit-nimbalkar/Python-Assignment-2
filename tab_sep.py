#Author-Abhijit Nimbalkar & Sriman Kolachalam

with open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses.txt') as fin:    #Opening the file expenses.txt
    for line in fin:    #Reading each line from the file
        line_stripped_newline=line[0:len(line)-1]   #Stripping the newline character
        line_to_print=line_stripped_newline.split(':')  #Seperating the string with str.split() function as ':' delimeter
        print(line_to_print[0],line_to_print[1],line_to_print[2],line_to_print[3],sep='\t') #printing the required output
