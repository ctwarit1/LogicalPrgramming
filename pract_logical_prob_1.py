"""
Create a function that takes a number x and a character
y ("m" for male, "f" for female), and returns the name of
 an ancestor (m/f) or descendant (m/f).
If the number is negative, return the related ancestor.
If positive, return the related descendant.
You are generation 0. In the case of 0 (male or female), return "me!".
"""


def generation(x, y):
    match x:
        case -3:
            if y == "m":
                print("great grandfather")
            else:
                print("great grandmother")

        case -2:
            if y == "m":
                print("grandfather")
            else:
                print("grandmother")

        case -1:
            if y == "m":
                print("father")
            else:
                print("mother")

        case 0:
            if y == "m":
                print("son")
            else:
                print("daughter")

        case 1:
            if y == "m":
                print("son")
            else:
                print("daughter")

        case 2:
            if y == "m":
                print("grandson")
            else:
                print("granddaughter")
        case 3:
            if y == "m":
                print("great grandson")
            else:
                print("great granddaughter")


if __name__ == "__main__":
    print("-------------")
    generation(2, "f")
    generation(-3, "m")
    generation(1, "f")
    print("-------------")


class CircleWithObject:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        area = self.pi * self.radius ** 2
        print(f"The area of circle is {area}")

    def circle_perimeter(self):
        perimeter = 2 * self.pi * self.radius
        print(f"The perimeter of circle is {perimeter}")


obj = CircleWithObject(3)
obj.circle_area()
obj.circle_perimeter()
print("-------------")

"""
Create a function that takes two numbers as arguments (num, length)
 and returns an array of multiples of num until the array length reaches length.
Examples
arrayOfMultiples(7, 5) ➞ [7, 14, 21, 28, 35]
arrayOfMultiples(12, 10) ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
arrayOfMultiples(17, 6) ➞ [17, 34, 51, 68, 85, 102]
"""


def array_of_multiples(num, length):
    count = 1
    nums = []
    for i in range(length):
        mult = count * num
        count += 1
        nums.append(mult)
    print(nums)


array_of_multiples(7, 5)
array_of_multiples(12, 10)
array_of_multiples(17, 6)
print("-------------")

"""
Create a function that determines whether a number is
Oddish or Evenish. A number is Oddish if the sum of all
of its digits is odd, and a number is Evenish if the sum
of all of its digits is even. If a number is Oddish, return "Oddish".
 Otherwise, return "Evenish".
For example, oddishOrEvenish(121) should return "Evenish",
since 1 + 2 + 1 = 4. oddishOrEvenish(41) should return "Oddish", since 4 + 1 = 5.
Examples
oddishOrEvenish(43) ➞ "Oddish"
// 4 + 3 = 7
// 7 % 2 = 1
oddishOrEvenish(373) ➞ "Oddish"
// 3 + 7 + 3 = 13
// 13 % 2 = 1
oddishOrEvenish(4433) ➞ "Evenish"
// 4 + 4 + 3 + 3 = 14
// 14 % 2 = 0
"""


def oddish_or_evenish(num):
    num_in_str = str(num)
    if len(num_in_str) == 2:
        num_in_list = num_in_str.split(" ")
        for i in num_in_list:
            store = int(i[0]) + int(i[1])
    elif len(num_in_str) == 3:
        num_in_list = num_in_str.split(" ")
        for i in num_in_list:
            store = int(i[0]) + int(i[1]) + int(i[2])
    elif len(num_in_str) == 4:
        num_in_list = num_in_str.split(" ")
        for i in num_in_list:
            store = int(i[0]) + int(i[1]) + int(i[2]) + int(i[3])
    if store % 2 == 0:
        print("Evenish")
    else:
        print("Oddish")


oddish_or_evenish(43)
oddish_or_evenish(373)
oddish_or_evenish(4433)

print("-------------")
