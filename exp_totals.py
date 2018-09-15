#Author-Abhijit Nimbalkar & Sriman Kolachalam

#intializing all variables
total=0
total_feb=0
total_mar=0
total_travel=0
total_meal=0
total_supply=0
total_util=0
with open('/Users/Deadpool/Desktop/Assignment 2/Files/expenses.txt') as fin:        #Opening the file expenses.txt for reading
    for line in fin:
        line_to_print=line.split(':')   #splitting each string by ':'
        if not line_to_print[0]=='Amount':  #Calculating total expenses
            total+=float(line_to_print[0])
        if line_to_print[2]!='Date':    
            date=line_to_print[2]   #calculating the expenses occured in the month of February
            if date[4:6]=='02':
                total_feb+=float(line_to_print[0])
            if date[4:6]=='03':
                total_mar+=float(line_to_print[0])  #calculating the expenses occured in the month of March
        if line_to_print[1]!='Category':
            if line_to_print[1]=='travel':      #calculating the expenses for category 'travel'
                total_travel+=float(line_to_print[0])
            if line_to_print[1]=='meal':        #calculating the expenses for category 'travel'
                total_meal+=float(line_to_print[0])
            if line_to_print[1]=='supply':      #calculating the expenses for category 'travel'
                total_supply+=float(line_to_print[0])
            if line_to_print[1]=='util':        #calculating the expenses for category 'travel'
                total_util+=float(line_to_print[0])

            #printing required output as mentioned in the problem statement
    print("Total of all expenses:  ${:<4.2f}\nTotal of Feb expenses:  ${:<4.2f}\nTotal of Mar expenses:  ${:<4.2f}\nTotal travel expenses:\
  ${:<4.2f}\nTotal meal expenses:    $0{:>3.2f}\nTotal supply expenses:  ${:<4.2f}\nTotal util expenses:    ${:>4.2f}"\
          .format(total,total_feb,total_mar,total_travel,total_meal,total_supply,total_util))


            
        
    
            
        
