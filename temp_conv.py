#Author-Abhijit Nimbalkar & Sriman Kolachalam

import Functions    #All functions are stored in the Functions.py file. To use all required functions importing the Functions.py file
find_function_to_call=['F','C','K'] #This list used to call the required function from list of conversion functions. 
number_of_options=['Fahrenheit','Celsius','Kelvin'] #This list used for printing the temperature which User has requested

while True:
    try:
        source=Functions.option_list_from() #Displying list of option by calling function from Functions.py
        if not source<=4 and source>=1:     #Checking the entered value is valid
            print("Please enter the correct option from 1 to 4!")
        elif source==4:
            break
        else:
            destination=Functions.option_list_to()  #Displaying list of option by calling function from Functions.py
            if not destination<=4 and destination>=1:   #Checking the entered value is valid
                print("Please enter the correct option from 1 to 4!")
            elif destination==4:
                break
            else:
                temp_value=Functions.check_temp_input_for_F("Please enter the temperature in "+number_of_options[source-1]+": ")#Accepting the input value from User and checking it if is valid input. Here I have called the function from Functions.py
                output_function=find_function_to_call[source-1]+'to'+find_function_to_call[destination-1]   #Creating the function as per the inputs received from User and the list defined initially in program i.e. find_function_to_call[]
                output_temp=getattr(Functions,output_function)(temp_value)  #Calling the function with the help of getattr(). It is use to call the function prepared from string
                print("The converted temperature from "+number_of_options[source-1]+ " to "+ number_of_options[destination-1]+" is: "+ str(output_temp)+"\n\n") #printing the required output
    except:
        print("Your Input is INVALID. Function will start from beginning. Please Re-enter value correctly.\n\n")
