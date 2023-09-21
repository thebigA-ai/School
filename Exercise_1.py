import re


# TASK 1
def base_to_dec_converter(number, base):  # function converts every given base to decimal. (used in task 2 too)
    try:
        dec_number = int(number, base)
        return dec_number
    except ValueError:
        print("invalid hex number")


def hex_to_dec(hex_number):  # converts hexadecimal to decimal
    print(base_to_dec_converter(hex_number, 16))


# TASK 2
def hex_sum(
        text):  # the function gets string as input and seperate the strings to the diffrente hexadecimal numbers and prints the sum
    sum = 0
    bad_letter = '[ghijklmnopqrstuvwxyz]'
    hex_list = re.split(bad_letter, text.lower())
    for i in hex_list:
        sum += base_to_dec_converter(i, 16)

    print(sum)


# TASK 3
def number_reader():  # function gets numbers from the user until something is not a number is enterd and returns the avrage and median of the numbers
    digit = "0"
    number_list = []
    a = True
    sum = 0
    avrage = 0
    while (a):
        digit = input("insert a number (insert anything else to stop): ")
        if (digit.isdigit()):
            number_list.append(int(digit))
        else:
            a = False
    for i in number_list:
        sum += i
    number_list.sort()
    length = len(number_list)
    if (length % 2 == 0):
        print(f'the median is: {(number_list[int(length / 2)] + number_list[int(length / 2) - 1]) / 2}')
    else:
        print(f'the median is: {number_list[int(length / 2)]}')
    print(f'the avrage is: {(sum) / len(number_list)}')


# TASK 1 implementation
'''
hex_number = input("insert a hexadecimal number: ")
hex_to_dec(hex_number)
'''

# TASK 2 implementation
'''
text = input("insert a text: ")
hex_sum(text)
'''

# TASK 3 implementation
'''
number_reader()
'''
