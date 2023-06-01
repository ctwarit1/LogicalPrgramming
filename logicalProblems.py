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
    dict_2 = {name: value}
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
n = 5
count = 1
while count < n + 1:
    list_1 = [i * count for i in range(1, n + 1)]
    print(list(list_1), end=" ")
    count += 1

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

# def total_overs(ball):
#     if ball % 6 == 0:
#         over_ball = ball / 6
#         print(round(over_ball))
#     else:
#         over_ball = f
#
#
# total_overs(2400)
# total_overs(164)
# total_overs(945)
# total_overs(5)

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
In the Code tab is a function which is meant to return how many
uppercase letters there are in a list of various words. Fix the
 list comprehension so that the code functions normally!
Examples
count_uppercase(["SOLO", "hello", "Tea", "wHat"]) ➞ 6
count_uppercase(["little", "lower", "down"]) ➞ 0
count_uppercase(["EDAbit", "Educate", "Coding"]) ➞ 5
"""


def count_uppercase(upper_list):
    convert_string = " "
    count_letter = 0
    store_string = convert_string.join(upper_list)
    for i in store_string:
        if i.isupper():
            count_letter += 1
    print(count_letter)


count_uppercase(["SOLO", "hello", "Tea", "wHat"])
count_uppercase(["little", "lower", "down"])
count_uppercase(["EDAbit", "Educate", "Coding"])

"""
Given two lists smlst and biglst, we say smlst is an ordered
sublist of biglst if all the elements of smlst can be found
in biglst, and in the same order.
Examples:
[4, 3, 2] is an ordered sublist of [5, 4, 3, 2, 1].
[5, 3, 1] is an ordered sublist of [5, 4, 3, 2, 1].
[5, 3, 1] is not and ordered sublist of [1, 2, 3, 4, 5] since
elements are not in the same - [1, 2, 3] is an ordered sublist of [3, 2, 1, 2, 3].
Write a function that, given lists smlst and biglst, decides
if smlst is an ordered sublist of biglst.
Examples
is_ord_sub([4, 3, 2], [5, 4, 3, 2, 1]) ➞ True
is_ord_sub([5, 3, 1], [5, 4, 3, 2, 1]) ➞ True
is_ord_sub([5, 3, 1], [1, 2, 3, 4, 5]) ➞ False
is_ord_sub([1, 2, 3], [3, 2, 1, 2, 3]) ➞ True
Notes
Be careful of examples like the fourth example, where the elements
 of smlst appear multiple times in biglst.
"""

# num_list = [4, 3, 2]
# check_list = [5, 4, 3, 2, 1]
# num = 0
# count = 1
# for i in range(len(num_list)):
#     for j in range(len(check_list)):
#         if num_list[i] == check_list[j]:
#             num = j
#             count += 1
#             if count == 3:
#                 print("True")
"""
Given a list of 10 numbers, return whether or not the list is
shuffled sufficiently enough. In this case, if 3 or more numbers
appear consecutively (ascending or descending), return False.
Examples
is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# 1, 2, 3 appear consecutively
is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# 9, 8, 7, 6 appear consecutively
is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# No consecutive numbers appear
is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# No consecutive numbers appear
Notes
Only steps of 1 in either direction count as consecutive (i.e. a sequence
 of odd and even numbers would count as being properly shuffled (see example #4)).
You will get numbers from 1-10.
"""

is_list_shuffle = [1, 2, 3, 5, 8, 6, 9, 10, 7, 4]
is_list_shuffle = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
list_new = []
for i in range(10):
    list_new.append(i)
# print(list_new)
rev_list = list_new.sort(reverse=True)
# print(list_new)
if list_new in is_list_shuffle or rev_list in is_list_shuffle:
    print("False")
else:
    print("True")

"""
Create a function that takes an integer n and returns
the factorial of factorials. See below examples for
a better understanding:
Examples
fact_of_fact(4) ➞ 288
# 4! * 3! * 2! * 1! = 288
fact_of_fact(5) ➞ 34560
fact_of_fact(6) ➞ 24883200
"""


def fact(n):
    if n != 0:
        return n * fact(n - 1)

    else:
        return 1


fact(4)

num = 4
factorial = 1

if num < 0 or num == 0:
    print("Enter a valid number")
else:
    # while num > 0:
    for i in range(1, num + 1):
        factorial = factorial * i
        factorial = factorial * factorial
        num -= 1
        print(factorial)

"""
Write a function that adds two numbers. The catch,
 however, is that the numbers will be strings.
Examples
add_str_nums("4", "5") ➞ "9"
add_str_nums("abcdefg", "3") ➞ "-1"
add_str_nums("1", "") ➞ "1"
add_str_nums("1874682736267235927359283579235789257", "32652983572985729")
 ➞ "1874682736267235927391936562808774986"
Notes
If there are any non-numerical characters, return "-1".
An empty parameter should be treated as "0".
Your function doesn't have to add negative numbers.
Zeros at the beginning of the string should be trimmed.
"""
num1 = "4"
num2 = "5"


def add_str_nums(num1, num2):
    if not num1.isdigit() or not num2.isdigit():
        print("-1")
    else:
        if num1 == "":
            num1 = 0
        if num2 == "":
            num2 = 0
        sum = int(num1) + int(num2)
        print(sum)


add_str_nums("4", "5")
add_str_nums("abcdefg", "3")
add_str_nums("1", "")
add_str_nums("1874682736267235927359283579235789257", "32652983572985729")

"""
Create a function that counts the number of digits
in a number. Conversion of the number to a string
is not allowed.
Examples
digits_count(4666) ➞ 4
digits_count(544) ➞ 3
digits_count(121317) ➞ 6
digits_count(0) ➞ 1
digits_count(12345) ➞ 5
digits_count(1289396387328) ➞ 13
Notes
All inputs are integers but some are in exponential
 form, deal with it accordingly.
"""
import math


def digits_count(n):
    if n == 0:
        print("0")
    else:
        print(round(math.log10(n)) + 1)


digits_count(4666)
digits_count(544)
digits_count(121317)
digits_count(0)
digits_count(12345)
digits_count(1289396387328)

"""
The keys of the new dictionary will be the elements in
the list, so we will iterate over the elements in list. If
the element is also in the dictionary, the value will be
the values of that key in the dictionary. Otherwise,
the value will be the length of the key.
{i:dct[i] if i in dct else len(i) for i in lst}
{'artificial': 10, 'data': 5, 'intelligence': 12, 'science': 3}
"""

"""
Given a sentence with numbers representing a word's
 location embedded within each word,
return the sorted sentence.
Examples
rearrange("is2 Thi1s T4est 3a") ➞ "This is a Test"
rearrange("4of Fo1r pe6ople g3ood th5e the2") ➞ "For the good of the people"
rearrange(" ") ➞ " "
Notes
Only the integers 1-9 will be used.
"""
rearrange = "is2 Thi1s T4est 3a"
li = list(rearrange.split(" "))
print(li)
# for i in range(len(li)):
#     if "1" in li[0] or "2" in li[0] or "3" in li[0] or "4" in li[0]:


"""
The function is given two strings t - template, s - to be sorted.
Sort the characters in s such that if the character is present in
t then it is sorted according to the order in t and other characters
are sorted alphabetically after the ones found in t.
Examples
custom_sort("edc", "abcdefzyx") ➞ "edcabfxyz"
custom_sort("fby", "abcdefzyx") ➞ "fbyacdexz"
custom_sort("", "abcdefzyx") ➞ "abcdefxyz"
custom_sort("", "") ➞ ""
Notes
The characters in t and s are all lower-case.
"""
# def custom_sort(s):
#     list_t = list(t.split(" "))
#     print(list_t)
#     list_s = list(s.split(" "))
#     print(list_s)
#     list_t.extend(list_s)
#     print(list_t)
#     for i in list_t:
#         for j in list_s:
#             if i in j:
#                 print(type(j))
#                 for i in range(len_new_list):
#                 for j in range(len_new_list-1):
#                     if new_list[j] > new_list[j+1]:
#                         temp = new_list[j]
#                         new_list[j] = new_list[j+1]
#                         new_list[j + 1] = temp
#             for i in range(len(new_list)):
#                 print(new_list[i])
#
#
# custom_sort("abcdefzyx")  #➞ "edcabfxyz"
# custom_sort("fby", "abcdefzyx")  #➞ "fbyacdexz"
# custom_sort("", "abcdefzyx")     #➞ "abcdefxyz"
# custom_sort("", "")              #➞ ""


"""
How to Calculate Points and Goal Difference
team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
Goal Difference = scored - conceded = 88 - 20 = 68
Examples
champions([
  {
    "name": "Manchester United",
    "wins": 30,
    "loss": 3,
    "draws": 5,
    "scored": 88,
    "conceded": 20,
  },
  {
    "name": "Arsenal",
    "wins": 24,
    "loss": 6,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  },
  {
    "name": "Chelsea",
    "wins": 22,
    "loss": 8,
    "draws": 8,
    "scored": 98,
    "conceded": 29,
  }
]) ➞ "Manchester United"
Notes
Input is a list of teams.
"""


def champions(name):
    dict_new = [{
        "name": "Chelsea",
        "wins": 22,
        "loss": 8,
        "draws": 8,
        "scored": 98,
        "conceded": 29
    },
        {
            "name": "Arsenal",
            "wins": 24,
            "loss": 6,
            "draws": 8,
            "scored": 98,
            "conceded": 29},
        {
            "name": "Manchester United",
            "wins": 30,
            "loss": 3,
            "draws": 5,
            "scored": 88,
            "conceded": 20
        }]
    for i in dict_new:
        if i.get("name") == name:
            print("Total Points = ", 3 * i.get("wins") + 1 * i.get("draws"))
            print("Goal Difference = ", i.get("scored") - i.get("conceded"))


champions("Chelsea")
champions("Arsenal")
champions("Manchester United")

"""
A word is alphabetically sorted if all of the letters in it
are in consecutive alphabetical order. Some examples of alphabetically
sorted words: abhors (a is before b, b is before h, h is before o, etc.), ghost, accent, hoop.
Create a function that takes in a sentence as input and returns
 True if there is at least one alphabetically sorted word inside
 that has a minimum length of 3.
Examples
is_alphabetically_sorted("Paula has a French accent.") ➞ True
# "accent" is alphabetically sorted.
is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
# "biopsy" is alphabetically sorted.
is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
# Although "by" is alphabetically sorted, it is only 2 letters long.
Notes
Do not count words with 2 or fewer characters.
Ignore punctuation (periods, commas, etc).
"""

"""
Given an integer array, find k'th smallest element in
the array where k is a positive integer less than or
equal to the length of array.
Input : [7, 4, 6, 3, 9, 1], k = 3
Output: 4
Explanation: The 3rd smallest array element is 4
Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
Output: 4
Explanation: The 5th smallest array element is 4
"""


def getting_num(unsort_list, k):
    len_list = len(unsort_list)
    for i in range(len_list):
        for j in range(len_list - 1):
            if unsort_list[j] > unsort_list[j + 1]:
                temp = unsort_list[j]
                unsort_list[j] = unsort_list[j + 1]
                unsort_list[j + 1] = temp
    for i in range(len(unsort_list)):
        print(unsort_list[i])
    print("""""""""""""""""""")
    for num in range(10):
        if num == k:
            print(unsort_list[num - 1])


getting_num([7, 4, 6, 3, 9, 1], 3)
getting_num([1, 5, 2, 2, 2, 5, 5, 4], 5)

"""
Run–length encoding (RLE) is a simple form of lossless data
 compression that runs on sequences with the same value
 occurring many consecutive times. It encodes the sequence
 to store only a single value and its count.
Input: 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
Output: '12W1B12W3B24W1B14W'
Explanation: String can be interpreted as a sequence of twelve W’s, one B, twelve W’s, three B’s, and so on..
"""

str = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
list_str = list(str)
length_str = len(list_str)
print(length_str)  # 67
print(str.count("W"))  # 62
print(str.count("B"))  # 5
count_w = str[0:10].count("W")
print(count_w)
count_b_w = str[10:20].count("W" and "B")
print(count_b_w)
count_w = str[20:30].count("W")
print(count_w)

count = 0
n = 0
list_str = list(str)
length_str = len(list_str)
for i in list_str:
    if "w" == i:
        count = count + 1
        print(count)
print(list_str)
length_str = len(str)
count = 0
start = 0
print(length_str)
while start < length_str:
    if "w" in str:
        count += 1

        print(count)

"""
Create a function that takes a string as an argument and returns the Morse code equivalent.
Examples
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
This dictionary can be used for coding:
char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
'6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}
Notes
Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
Input value can be lower or upper case.
Input string can have digits.
Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
One space " " is expected after each character, except the last one.
"""

"""
Create a function that takes in two words as input
and returns a list of three elements, in the following order:
Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element should have unique letters, and have
each letter be alphabetically sorted.
Examples
letters("sharp", "soap") ➞ ["aps", "hr", "o"]
letters("board", "bored") ➞ ["bdor", "a", "e"]
letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should
# only exist a single "f" in your first element.
letters("match", "ham") ➞ ["ahm", "ct", ""]
# "ham" does not contain any letters that are not found already
# in "match".
Notes
Both words will be in lower case.
You do not have to worry about punctuation, all words only have letters from [a-z].
If an element contains no letters, return an empty string (see last example)
"""
one = "sharp"
two = "soap"
list_dup = []
list_same = []
for i in one:
    for j in two:
        if i in two:
            print(i)
        elif i not in two:
            print(i)
        else:
            print("hello")
if one in two:
    concat = one + two
print(concat)
print(set(concat))

list_one = list(one)
list_two = list(two)
list_same = []
list_dup = []
list_res = []

for i in list_one:
    if i in list_two:
        list_same.append(i)
        list_two.remove(i)
    else:
        list_dup.append(i)

list_res.append(list_same)
list_res.append(list_dup)
list_res.append(list_two)
list_res = str(list_res)

print(list_res)

"""
input = [0, 1, 0, 3, 12]
output = [1, 3, 12, 0, 0]
"""


def sort_list(list_1):
    for i in range(len(list_1)):
        for j in range(len(list_1) - 1):
            if list_1[j] > list_1[j + 1]:
                temp = list_1[j]
                list_1[j] = list_1[j + 1]
                list_1[j + 1] = temp
    new_list = []
    for i in list_1:
        if i != 0:
            new_list.append(i)
    for i in list_1:
        if i == 0:
            new_list.append(i)
    print(new_list)


sort_list([0, 6, 8, 4, 0, 3, 0])
sort_list([0, 1, 0, 3, 12])

"""
Create the instance attributes fullname and email in the
Employee class. Given a person's first and last names:
Form the fullname by simply joining the first and last name
together, separated by a space.
Form the email by joining the first and last name together
with a . in between, and follow it with @company.com at the
end. Make sure the entire email is in lowercase.
Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"
emp_2.email ➞ "mary.sue@company.com"
emp_3.firstname ➞ "Antony"
"""


class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print(self.first_name, self.last_name)


"""


Write a method that accepts two integer parameters rows and cols.
 The output is a 2d array of numbers displayed in column-major
 order, meaning the numbers shown increase sequentially down each
  column and wrap to the top of the next column to the right once
  the bottom of the current column is reached.
Examples
printGrid(3, 6) ➞ [
  [1, 4, 7, 10, 13, 16],
  [2, 5, 8, 11, 14, 17],
  [3, 6, 9, 12, 15, 18]
]
printGrid(5, 3) ➞ [
  [1, 6, 11],
  [2, 7, 12],
  [3, 8, 13],
  [4, 9, 14],
  [5, 10, 15]
]
printGrid(4, 1) ➞ [
  [1],
  [2],
  [3],
  [4]
]
"""


def print_grid(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]
    value = 1
    for j in range(cols):
        for i in range(rows):
            matrix[i][j] = value
            value += 1

    print(matrix)


print_grid(3, 6)
print_grid(5, 3)
print_grid(4, 1)

"""
output ----> cup_swapping(["AB", "CA"]) ➞ "C"
             cup_swapping(["AC", "CA", "CA", "AC"]) ➞ "B"
             cup_swapping(["BA", "AC", "CA", "BC"]) ➞ "A"
starting with ball in B
"""


def cup_swapping(list_new):
    start_pos = "B"
    for i in list_new:

        if start_pos in i:
            if start_pos == i[0]:
                start_pos = i[1]
            else:
                start_pos = i[0]
    print(start_pos)
    # return start_pos


cup_swapping(["AB", "CB"])
cup_swapping(["AC", "CA", "CA", "AC"])
cup_swapping(["BA", "AC", "CA", "BC"])



"""
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number
by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Input: n = 19
Output: true
Explanation:
1^2 + 9
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Input: n = 2
Output: false
"""
n = "19"
li = n.split(" ")

for i in li:
    nums = int(i[0]) ** 2 + int(i[1]) ** 2
    while nums >= 1:
        n = nums
        print(n)
        continue

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
