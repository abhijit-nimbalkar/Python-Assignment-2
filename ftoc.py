#Author-Abhijit Nimbalkar & Sriman Kolachalam

import Functions                                #importing Functions.py file having multiple functions
temp_in_F=Functions.check_temp_input_for_F("Enter the Temperature in Fahrenheit: ") #Calling function check_temp_input_for_F() for accepting the valid input from User
temp_in_C=Functions.FtoC(temp_in_F)             #Calling function to convert temperature from Fahrenheit to Celsius
print("{0}{1:0.2f}".format("Temperature in Celsius is: ", temp_in_C))   #printing the output in right format


