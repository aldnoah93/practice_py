'''
Armstrong Numbers

Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if. 

abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 

ref: https://www.geeksforgeeks.org/program-for-armstrong-numbers/
'''

import math

# Gets the digits count of a given number
def get_digit_count(number: int) -> int:
    return int(math.log10(number)) + 1
    
# calculates the sum of a number digits power to the number's length
def armstrong_sum(number: int) -> int:
    n = get_digit_count(number)
    sum = 0
    while number != 0:
        sum += (number % 10) ** n
        number //= 10
    return sum
 
def show_result(number: int):
    is_armstrong = number == armstrong_sum(number)
    if is_armstrong:
        print("%d is an armstrong number"%(number))
    else:
        print("%d is not an armstrong number"%(number))

number = 153
show_result(number)

number = 663
show_result(number)

number = 1634
show_result(number)