#Author-Abhijit Nimbalkar & Sriman Kolachalam

#Function for converting Fahrenheit to Celsius
def FtoC(temp):
    temp=5/9*(temp-32)
    return temp

#Function for converting Fahrenheit to Kelvin
def FtoK(temp):
    temp= 5/9*(temp-32)+273
    return temp

#Function for converting Celsius to Fahrenheit
def CtoF(temp):
    temp=(9*temp/5)+32
    return temp

#Function for converting Celsius to Kelvin
def CtoK(temp):
    temp=temp+273
    return temp

#Function for converting Kelvin to Fahrenheit
def KtoF(temp):
    temp=9/5*(temp-273)+32
    return temp

#Function for converting Kelvin to Celsius
def KtoC(temp):
    temp=temp-273
    return temp

#Function for checking the valid input to be entered by User. It is same as function of input(arg)
def check_temp_input_for_F(display_string):
    while True:             #Infinite while loop until User enters the correct value
        try:                #to catch exception
            valid_temp=float(input(display_string))
            if valid_temp>212 or valid_temp<-100:   #checking the value is between 212 and -100
                print("Oops! Please enter the temperature below 212F and above -100F")
            else:
                return valid_temp       #if entered value is correct then returning it to main functions
        except:
            print("You have entered the invalid format of temperature. Please enter in the Correct Format!")

#Function to print the first list of temperatures asking User to select the option
def option_list_from():
    print("Out of following, which kind of temperature you would like to convert 'FROM'")
    print(" 1.Fahrenheit\n","2.Celsius\n","3.Kelvin\n","4.Exit")
    source=int(input("Please enter your option from 1 to 4: "))
    return source

#Function to print the first list of temperatures asking User to select the option
def option_list_to():
    print("Out of following, which kind of temperature you would like to convert 'TO'")
    print(" 1.Fahrenheit\n","2.Celsius\n","3.Kelvin\n","4.Exit")
    destination=int(input("Please enter your option from 1 to 4: "))
    return destination
