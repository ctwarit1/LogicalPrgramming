"""
It takes 21 seconds to wash your hands and help prevent
the spread of COVID-19.
Create a function that takes the number of times a person
washes their hands per day N and the number of months they
follow this routine nM and calculates the duration in minutes
 and seconds that person spends washing their hands.
Examples
wash_hands(8, 7) ➞ "588 minutes and 0 seconds"
wash_hands(0, 0) ➞ "0 minutes and 0 seconds"
wash_hands(7, 9) ➞ "661 minutes and 30 seconds"
Notes
Consider a month has 30 days.
"""


def covid_19(wash_hands, months):
    if wash_hands != 0 or months != 0:
        result = wash_hands * 21 * 30 * months
        time_min = result // 60
        time_sec = round(result % 60 / 60 * 60)
        print(f"{time_min} minutes and {time_sec} seconds")
    else:
        print(f"0 minutes and 0 seconds")


covid_19(8, 7)
covid_19(0, 0)
covid_19(7, 9)

"""
Given an unsorted integer array, find a pair with the given sum in it.
• Each input can have multiple solutions. The output should match with
either one of them.
Input : nums[] = [8, 7, 2, 5, 3, 1], target = 10
Output: (8, 2) or (7, 3)
• The solution can return pair in any order. If no pair with the given
sum exists, the solution should return an empty tuple.
Input : nums[] = [5, 2, 6, 8, 1, 9], target = 12
Output: ()
"""

def num_target(nums, target):
    for i in nums:
        for j in nums:
            if i + j == target:
                if i != j:
                    return i, j
    return ()


print(num_target([8, 7, 2, 5, 3, 1], 10))
print(num_target([5, 2, 6, 8, 1, 9], 12))


"""
Given three arguments ⁠— an object obj of the stolen items,
 the pet's name and a value ⁠— return an object with that
 name and value in it (as key-value pairs).
Examples
addName({}, "Brutus", 300) ➞ { Brutus: 300 }
addName({ piano: 500 }, "Brutus", 400) ➞ { piano: 500, Brutus: 400 }
addName({ piano: 500, stereo: 300 }, "Caligula", 440) ➞ { piano: 500, stereo: 300, Caligula: 440 }
"""
def addName(dict_1, name, value):

    dict_2 ={name:value}
    dict_1.update(dict_2)
    print(dict_1)


addName({}, "Brutus", 300)
addName({"piano": 500}, "Brutus", 400)
addName({"piano": 500, "stereo": 300}, "Caligula", 440)



""" Create a function that takes a list of numbers
 lst, a string s and return a list of numbers as per the following rules:

"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.
Examples
asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]

asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]

asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4] """


def arrange_list(list_order, arrange):
    if "Asc" in arrange:
        list_order.sort()
        print(list_order)
    elif "Des" in arrange:
        list_order.sort(reverse=True)
        print(list_order)
    else:
        print(list_order)


arrange_list([4, 3, 2, 1], "Asc")
arrange_list([7, 8, 11, 66], "Des")
arrange_list([1, 2, 3, 4], "")

"""
Your task, is to create N x N multiplication table,
of size n provided in parameter.

For example, when n is 5, the multiplication table is:

1, 2, 3, 4, 5
2, 4, 6, 8, 10
3, 6, 9, 12, 15
4, 8, 12, 16, 20
5, 10, 15, 20, 25
This example will result in:

[[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]]
Examples
multiplication_table(1) ➞ [[1]]

multiplication_table(3) ➞ [[1, 2, 3], [2, 4, 6], [3, 6, 9]
"""
n=5
count = 1
while count < n+1:
    list_1 = [i * count for i in range(1, n + 1)]
    print(list(list_1), end=" ")
    count += 1

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
    match x:
        case -2:
            if y == "m":
                print("grandfather")
            else:
                print("grandmother")
    match x:
        case -1:
            if y == "m":
                print("father")
            else:
                print("mother")
    match x:
        case 0:
            if y == "m":
                print("son")
            else:
                print("daughter")
    match x:
        case 1:
            if y == "m":
                print("son")
            else:
                print("daughter")
    match x:
        case 2:
            if y == "m":
                print("grandson")
            else:
                print("granddaughter")
    match x:
        case 3:
            if y == "m":
                print("great grandson")
            else:
                print("great granddaughter")

generation(2, "f")
generation(-3, "m")
generation(1, "f")

"""
Create a function that takes an array of numbers and 
return "Boom!" if the digit 7 appears in the array. 
Otherwise, return "there is no 7 in the array".
"""


# def seven_boom(hello):
# seven_boom = [1, 2, 3, 4, 5, 6, 7]
seven_boom = [8, 6, 33, 100]
if 7 in seven_boom:
    print("Boom!")
else:
    print("there is no 7 in the array")


# seven_boom([1, 2, 3, 4, 5, 6])
# seven_boom([8, 6, 33, 100])
# seven_boom([2, 55, 60, 97, 86])

"""
Create a function that takes a list of numbers or strings and 
returns a list with the items from the original list stored 
into sublists. Items of the same value should be in the same sublist.
Examples
advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]
advanced_sort(["b", "a", "b", "a", "c"]) ➞ [["b", "b"], ["a", "a"], ["c"]]
Notes
The sublists should be returned in the order of each element's first 
appearance in the given list.
"""
list_1 = [2, 1, 2, 1]
list_2 = []
count = 0
for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[i] == list_1[j]:
            count += 1
            list_2.append(list_1[i])
            print(list_2)










"""
Given a sentence as txt, return True if any two adjacent
 words have this property: One word ends with a vowel, while
  the word immediately after begins with a vowel (a e i o u).

Examples
vowel_links("a very large appliance") ➞ True

vowel_links("go to edabit") ➞ True

vowel_links("an open fire") ➞ False

vowel_links("a sudden applause") ➞ False
Notes
You can expect sentences in only lowercase, with no punctuation.
"""
# word = ["hello", "world"]
# string = "go to edabit"
# list_str = [string]
# print(list_str, end=" ")
# list(word)
# print(word[0])
# print(word[0][-1])
# if "a" == word[0][-1] or "e" == word[0][-1] or "i" == word[0][-1] or "o" == word[0][-1] or "u" == word[0][-1]:
#     print(word[0])
# else:
#     print("no vowel")
# for i in word:
#     if " " in word:
#         print("yes")
#     else:
#         print("NO")


"""
Create a function that reorders the digits of each numerical element
 in a list based on ascending (asc) or descending (desc) order.

Examples
reorder_digits([515, 341, 98, 44, 211], "asc") ➞ [155, 134, 89, 44, 112]

reorder_digits([515, 341, 98, 44, 211], "desc") ➞ [551, 431, 98, 44, 211]

reorder_digits([63251, 78221], "asc") ➞ [12356, 12278]
reorder_digits([63251, 78221], "desc") ➞ [65321, 87221]

reorder_digits([1, 2, 3, 4], "asc")  ➞ [1, 2, 3, 4]
reorder_digits([1, 2, 3, 4], "desc") ➞ [1, 2, 3, 4]
Notes
Single-digit numbers should be ordered the same regardless of direction.
Numbers in the list should be kept the same order.
"""

# reorder_digits = [515, 341, 98, 44, 211]
# print(len(reorder_digits))
# res = reorder_digits[0]//10
# res_1 =res//10
# print(res_1)

# for reorder_digits in range(len(reorder_digits)):
#     print(reorder_digits[0])

""" Create a function that takes a number num and returns its length.

Examples
number_length(10) ➞ 2

number_length(5000) ➞ 4

number_length(0) ➞ 1 """


def num_length(num):
    count = 0
    sum = str(num)
    for sum in range(len(sum)):
        count += 1
    print(count)


num_length(10)
num_length(5000)
num_length(1)

"""                Create a function that takes a number as 
an argument and returns "Fizz", "Buzz" or "FizzBuzz".
If the number is a multiple of 3 the output should be "Fizz".
If the number given is a multiple of 5, the output should be "Buzz".
If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
The output should always be a string even if it is not a multiple of 3 or 5.
Examples
fizz_buzz(3) ➞ "Fizz"
fizz_buzz(5) ➞ "Buzz"
fizz_buzz(15) ➞ "FizzBuzz"
fizz_buzz(4) ➞ "4"         """


def fizz_buzz():
    for i in range(1, 20):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizz_buzz()

""" Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.
Example
sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0]) """


def odd_even(sum_odd_and_even):
    sum_even = 0
    sum_odd = 0
    for i in sum_odd_and_even:
        if i % 2 != 0:
            sum_odd += i
        if i % 2 == 0:
            sum_even += i
    print([sum_even, sum_odd])


odd_even([1, 2, 3, 4, 5, 6])
odd_even([-1, -2, -3, -4, -5, -6])

""" Write a function that takes an integer
 minutes and converts it to seconds.
Examples
convert(5) ➞ 300
convert(3) ➞ 180
convert(2) ➞ 120 """


def min_sec(min):
    min_in_sec = min * 60
    print(min_in_sec)


min_sec(5)
min_sec(3)

""" 
In cricket, an over consists of six deliveries a 
bowler bowls from one end. Create a function that
 takes the number of balls bowled by a bowler and 
 calculates the number of overs and balls bowled 
 by him/her. Return the value as a float, in the 
 format overs.balls.

Examples
total_overs(2400) ➞ 400

total_overs(164) ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

total_overs(945) ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.

total_overs(5) ➞ 0.5"""

def total_overs(ball):
    if ball % 6 == 0:
        over_ball = ball / 6
        print(round(over_ball))
    else:
        over_ball =f


total_overs(2400)
total_overs(164)
total_overs(945)
total_overs(5)

"""
Create a function that takes two number 
strings and returns their sum as a string.

Examples
add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"
"""


def add_num(num1, num2):
    if "" in num1 or "" in num2:
        print("Invalid Operation")
    else:
        sum = int(num1) + int(num2)
        print(str(sum))


add_num("111", "111")
add_num("10", "80")
add_num("", "20")





"""
Given a linked list class, implement a method called reverse() that 
reverses the linked list.
Examples
Input: 10 -> 20 -> 30 -> 40 -> None
Output: 40 -> 30 -> 20 -> 10 -> None
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display_LL(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end=" ")
                n = n.ref

    def add_elem_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


# obj = LinkedList()
#
# obj.add_elem_end(10)
# obj.add_elem_end(20)
# obj.add_elem_end(30)
# obj.add_elem_end(40)
#
# obj.display_LL()
