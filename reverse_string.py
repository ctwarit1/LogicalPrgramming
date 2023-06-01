"""
Reverse the string without affecting special characters and numbers.
Examples
rev_specstring("AFC#47GH$Ieu") ➞ "ueI#47HG$CFA"
rev_specstring("guyhiuj1234!@#$%rtyhghu") ➞ "uhghytr1234!@#$%juihyug"
rev_specstring("12!@" ) ➞ "12!@"
Notes
Try with for loops.
"""

def rev_specstring(str):
    str_list = list(str)
    alnum_list = []
    char_list = []
    new_list = []

    for i in str_list:
        if i.isalnum():
            alnum_list.insert(0, i)
            if not i.isalnum():
                index_char = new_list.index(i)
                char_list.insert(index_char, i)
                print(char_list)
    rev_str = ''.join(alnum_list)
    print(rev_str)


rev_specstring("AFC#47GH$Ieu")  # ➞ "ueI#47HG$CFA"
rev_specstring("guyhiuj1234!@#$%rtyhghu")  # ➞ "uhghytr1234!@#$%juihyug"
rev_specstring("12!@")  # ➞ "12!@"


# def rev_specstring(string):
#
#     string_list = list(string)
#     left = 0
#     right = len(string) - 1
#
#     while left < right:
#         if not string_list[left].isalnum():
#             left += 1
#
#         elif not string_list[right].isalnum():
#             right -= 1
#
#         else:
#             string_list[left], string_list[right] = string_list[right], string_list[left]
#             left += 1
#             right -= 1
#
#     rev_str = ''.join(string_list)
#     print(rev_str)
#
# rev_specstring("AFC#47GH$Ieu")
# rev_specstring("guyhiuj1234!@#$%rtyhghu")
# rev_specstring("12!@")