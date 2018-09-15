# Python-Assignment-2
In this assignment, I have covered Files, Lists, Loops with operators.

----------Download the three example programs from the notes: user_age.py, copy_file_open_close.py, and copy_file_with.py.  Also, download the example data file for this homework, expenses.txt.  Put all four of these files in new directory by themselves, preferably not too many levels down from the top of your directory tree.  (For example, my copies of these files are in the directory \Users\jostlund\IPP_HW2.)

a.	In IDLE (or the Python development environment of your choice), open the user_age.py program file, and run the program (in IDLE, do this by pressing F5).  Look at the code and run it a few times so you are confident what the program is doing.

b.	Write a new program, ftoc.py, that asks the user to enter a Fahrenheit temperature and that displays the corresponding Celsius temperature in a user-friendly way.  Make sure that if the user enters a non-numeric string, or a Fahrenheit temperature above 212 degrees or below -100 degrees, that you ask the user to enter a correctly formatted and more reasonable value.  In your program, define a function named FtoC that takes a Fahrenheit temperature as an argument and computes and returns the corresponding Celsius temperature.  (I did not say, during Lecture, where function definitions should go in your program.  Most often, a function that you want to use in your program is defined above the start of the main part of your program.)

c.	Write a new program, temp_conv.py, that asks the user which kind of temperature they would like to convert from (Fahrenheit, Celsius, or Kelvin), which kind of temperature they would like to convert to (Fahrenheit, Celsius, or Kelvin), and what the temperature value is that they would like to convert.  If the input temperature value is reasonable, perform the requested conversion and display a user-friendly message describing the input temperature, the conversion performed, and the converted temperature.  You may wish to add some more conversion function definitions in this program.
 

2.	Processing a Data File

a.	Edit the copy_file_open_close.py program, and change the file pathname for the input file to your expenses.txt file.  (For example, my input file pathname will be '/Users/jostlund/IPP_HW2/expenses.txt'.  Notice that even though I am running MS-Windows 10, I can use / rather than \ as my directory separator.)

Then, change the output file name to expenses_copy1.txt, and change the output file pathname to what is appropriate for you.  (My output file pathname will be '/Users/jostlund/IPP_HW2/expenses_copy1.txt'.)

Save your modified program file (Ctrl-S in IDLE) and then run it (F5 in IDLE), and confirm that the expenses_copy1.txt file was created, and contains a copy of the contents of expenses.txt.

b.	Now, edit the copy_file_with.py program, and make analogous changes to the input file and output file pathnames, with expenses_copy2.txt as the name of the output file for this program.

Save your modified program file (Ctrl-S in IDLE) and then run it (F5 in IDLE), and confirm that the expenses_copy2.txt file was created, and contains a copy of the contents of expenses.txt.

c.	The expenses.txt file is a record of business expenses for an individual consultant, over a short period of time, February and March of 2017.  Each line in the file (after the header line) fives the dollar amount, category, date, and description of an expenses.  The descriptions sometimes contain commas, like:

paper, toner, pens, paperclips, tape
	
	so the four fields in each line are separated with colon (:) characters rather than
	commas (as in a .csv file).

	Write a program, tab_sep.py, that reads the expenses.txt file as input, and
	displays each line from expenses.txt as output, but with each colon replaced with
	a horizontal tab character, '\t'. 

Please note that, unlike the input() function, each line that you read from the
Input file using for line in fin: does not have its newline stripped.  You will have
to do that yourself.  Hint: How can you get a slice of a str that includes all but
the last character?
 
d.	Your output in part (c) might not look quite right, because ‘Category’ in the header line is 8 characters wide, the same width as a tab stop.  Also, the dates (like ‘20170222’) are exactly 8 characters wide.  So tab stops might not be the right approach here.  Write a program, exp_pretty.py, that displays the contents of the expenses.txt file in four nicely formatted columns.  The largest expense amount is 2147.49, so make the Amount column 10 characters wide, and right justify the numbers (but not the column name).  Leave two spaces before the Category column.  Make the Category column 10 characters wide, left-justified.  Make the Date column 10 characters wide, and leave the Description column of arbitrary width.  So the program’s output should look like:

Amount      Category  Date      Description
      5.25  supply    20170222  box of staples
     79.81  mean      20170222  lunch with ABC ...
     43.00  travel    20170222  cab back to office


e.	Write a program, exp_totals.py, that computes and displays the total expense amounts for: (1) the entire expenses.txt file, (2) the records from February, (3) the records from March, (4) the records for travel, (5) the records for meals, (6) the records for supplies, and (7) the records for utilities.  The output should look like:

Total of all expenses:  $xxxx.xx
Total of Feb expenses:  $xxxx.xx
Total of Mar expenses:  $xxxx.xx
Total travel expenses:  $xxxx.xx
Total meal expenses:    $xxxx.xx
Total supply expenses:  $xxxx.xx
Total util expenses:    $xxxx.xx

