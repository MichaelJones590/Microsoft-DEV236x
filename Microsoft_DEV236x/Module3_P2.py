#3.6 Optional Practice
# Input a number 
# - if number IS a digit string then cast to int
# - print number "greater than 100 is" True/False
# - if number is NOT a digit string then message the user that "only int is accepted"
number = input('Please input a number (integer): ')
if number.isdigit() == False:
    print('Please enter an integer.  Only integers are accepted.')
elif int(number) > 100: 
    print(number, 'greater than 100 is true')
else:
    print(number, 'greater than 100 is false')