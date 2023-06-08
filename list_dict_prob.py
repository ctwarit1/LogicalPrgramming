"""
2. Write a program that reads a list of integers and finds the
kth smallest element, where k is a positive integer.
"""
a = [3, 4, 55, 1, 9]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(smallest)

"""
4. Implement a program that reads a large text file and finds 
the top 10 most frequent words, excluding common stop words.
"""


# def read_file(file):
#     with open(file, 'r') as f:
#         text = f.read()
#     return text

def common_stop_words():
    return {"an", "the", "for", "and", "that", "in"}


def repeating_words(file):
    words = {}
    stop_word = common_stop_words()
    with open(file, 'r') as f:
        for i in f:
            i = i.lower()
            word = i.split()


repeating_words('large_text.txt')

"""
5. Write a function that takes two lists of integers and returns a 
new list that contains the intersection of the two lists, without 
using any built-in intersection functions.
"""


def intersection(lst1, lst2):
    intersect = []
    lst1_set = set(lst1)
    for i in lst2:
        if i in lst1_set and i not in intersect:
            intersect.append(i)
    print(intersect)


intersection([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])

#                           --------------------- dictionary ---------------------
"""
1. Create a dictionary that maps products to
their prices. Write a program that finds the most expensive
and the least expensive product.
"""


def expensive_product(dict):
    max_price = float('-inf')
    max_product = None
    for product, price in dict.items():
        if price > max_price:
            max_product = product
            max_price = price
    print(max_product)


def least_expensive_product(dict):
    min_price = float('inf')
    min_product = None
    for product, price in dict.items():
        if price < min_price:
            min_product = product
            min_price = price
    print(min_product)


expensive_product({"tv": 2000, "laptop": 5000, "fridge": 7000, "mobile": 333})
least_expensive_product({"tv": 2000, "laptop": 5000, "fridge": 7000, "mobile": 333})

"""
2. Implement a function that takes a dictionary as input and 
returns a new dictionary where the keys are sorted based on
their corresponding values.
"""


def unsorted_dict(dict):
    keys = []
    for i in dict:
        value = False
        for j in range(len(keys)):
            if dict[i] < dict[keys[j]]:
                keys.insert(j, i)
                value = True
                break
        if not value:
            keys.append(i)

    sorted_dict = {}
    for i in keys:
        sorted_dict[i] = dict[i]
    print(sorted_dict)


unsorted_dict({"three": 3, "one": 1, "four": 4, "two": 2})

"""
3. Write a program that reads a list of dictionaries, where 
each dictionary represents a person with attributes like name,age.
and profession. Find the oldest person in the list.
"""


def oldest_person(dict):
    max_age = 0
    max_age_name = None
    for i in dict:
        # if i.get("age") == max(age_list):
        #     print(i.get("name"))
        if i["age"] > max_age:
            max_age = i["age"]
            max_age_name = i
    print(max_age_name)


oldest_person(
    [{"name": "twarit", "age": 24, "profession": "student"}, {"name": "kunal", "age": 30, "profession": "student"},
     {"name": "rahul", "age": 28, "profession": "student"}])

"""
4. Create a dictionary that maps words to their frequencies in a given text.
 Write a program that finds the most common word and its frequency.
 """


# def frequency_word(para):
#     frequency = {}
#
#     words = para.split()
#     for i in words:
#         if i in frequency:
#             frequency[i] += 1
#         else:
#             frequency[i] = 1
#
#     common_word = None
#     max_frequency = 0
#     for i, j in frequency.items():
#         if j > max_frequency:
#             max_frequency = j
#             common_word = i
#     print(common_word)
#     print(frequency)
#
#
# para = "Hello my name is twarit. I am from kota, studied in kota"
# frequency_word(para)
