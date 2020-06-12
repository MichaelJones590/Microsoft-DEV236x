#3.6 Optional Practice
# Create check_guess()
def rainbow_color(color_letter):
    if color_letter == 'r':
        color = 'Your favorite color is Red'
    elif color_letter == 'o':
        color = 'Your favorite color is Orange'
    elif color_letter == 'y':
        color = 'Your favorite color is Yellow'
    elif color_letter == 'g':
        color = 'Your favorite color is Green'
    elif color_letter == 'b':
        color = 'Your favorite color is Blue'
    elif color_letter == 'i':
        color = 'Your favorite color is Indigo'
    elif color_letter == 'v':
        color = 'Your favorite color is Violet'
    else:
        color = 'No color match'
    return color
def age_20(age):
    if age >= 50:
        age_by_20 = age-20
        age_comment = 'Twenty years ago you were ' + str(age_by_20)
    else: 
        age_by_20 = age+20
        age_comment = 'In twenty years you will be ' + str(age_by_20)
    return age_comment   
def rainbow_or_age(rainage):
    if rainage.isdigit():
        age_int = int(rainage)
        rainage_str = age_20(age_int)
    elif rainage.isalpha():
        rainage_lower = rainage.lower()
        rainage_str = rainbow_color(rainage_lower)
    else:
        rainage_str = 'FALSE'
    return rainage_str

input_str = input('Enter the letter of your favorite color (R,O,Y,G,B,I,V) or your age:')
color_age = rainbow_or_age(input_str)
print(color_age)