# Find the nearest value to the given one.
#
# You have a list of values as set form and need to find the nearest one
#
# For example,we have the following set of numbers:
# 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9.
# If we sort this set in the ascending order, THEN the:
# left: of number 9 will be number 7, AND
# right: will be number 10. BUT
# THEN 10 is closer than 7, which means that the correct answer is 10.
#
# A few clarifications:
#
# If 2 numbers are at the same distance, you need to choose the smallest one;
# The set of numbers is always non-empty, i.e. the size is >=1;
# The given value can be in this set, which means that it’s the answer;
# The set can contain both positive and negative numbers, but they are always integers;
# The set isn’t sorted and consists of unique numbers.
# Input: Two arguments. A list of values in the set form. The sought value is an int.
# Output: Int.
#
# def nearest_value(values):
# return = lkjhgvc
#
# if __name__ == '__main__':
#     print("Example:")
#     print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
#     assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
#     assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
#     assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
#     assert nearest_value({-1, 2, 3}, 0) == -1
#     print("Coding complete? Click 'Check' to earn cool rewards!")
#
# # using abs() + list comprehension
# diff _of_number_and_values_of_nearest_values =  [abs(ele) for ele in values]
from typing import List, Any
#
import a


def nearest_value(values: set, numb: int) -> int:
    a = {}
    #     values = values() ....typo err
    # values = : List[Any] = list(values)
    # # anyvardiff= [abs()]
    values = list(values)
    values.sort()
    # diff is absolute number of numb for the val list

    diff = [abs(forloop_itterator - numb) for forloop_itterator in values]

    return values[diff.index(min(diff))]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 8))
    # 100 is numb

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
#
# def nearest_value(values: set, numb: int) -> int:
#     #     values = values() ....typo err
#     # values = : List[Any] = list(values)
#     # # anyvardiff= [abs()]
#     values = list(values)
#     values.sort()
#     # diff is absolute number of numb for the val list
#
#     diff = [abs(forloop_itterator - numb) for forloop_itterator in values]
#
#     return values[diff.index(min(diff))]
#
#
# if __name__ == '__main__':
#     print("Example:")
#     near_value_in = {4, 7, 10, 11, 12, 17}
#     near_value_of = {9}
#     print(nearest_value(near_value_in, near_value_of))
#     # 100 is number
#
#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
#     assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
#     assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
#     assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
#     assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
#     assert nearest_value({-1, 2, 3}, 0) == -1
#     print("Coding complete? Click 'Check' to earn cool rewards!")
