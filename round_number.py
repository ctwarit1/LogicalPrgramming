"""
Create a function that takes two integers, num and n, and
returns an integer which is divisible by n and is the closest
to num. If there are two numbers equidistant from num and
divisible by n, select the larger one.
Examples
round_number(33, 25) ➞ 25
round_number(46, 7) ➞ 49
round_number(133, 14) ➞ 140
Notes
n will always be a positive number.
"""


def round_number(num, n):
    quotient = num // n
    # print(quotient)

    num1 = quotient * n
    # print(num1)
    num2 = (quotient + 1) * n
    print(num2)
    if abs(num - num1) <= abs(num - num2):
        return num1
    else:
        return num2


print(round_number(33, 25))
print(round_number(46, 7))
print(round_number(133, 14))