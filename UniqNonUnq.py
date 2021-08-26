# You are given a non-empty list of integers (X). For this task, you should return a list consisting of only the non-unique elements in this list. To do so you will need to remove all unique elements (elements which are contained in a given list only once). When solving this task, do not change the order of the list. Example: [1, 2, 3, 1, 3] 1 and 3 non-unique elements and result will be [1, 3, 1, 3].
# non-unique-elements
# Input: A list of integers.
# Output: An iterable of integers.
# How it is used: This mission will help you to understand how to manipulate arrays, something that is the basis for solving more complex tasks. The concept can be easily generalized for real world tasks. For example: if you need to clarify statistics by removing low frequency elements (noise).
# You can find out more about Python arrays in one of our articles featuring lists, tuples, array.array and numpy.array .
# Precondition:
# 0 < len(data) < 1000

# Your optional code here
# You can import some modules or create additional functions
target = [1, 2, 3, 4, 4, 4, 3, 5, 6, 8, 4, 3, 3]
duplicates = filter(lambda rec: target.count(rec) > 1, target)
print(duplicates)
# duplicates = dict(set((x, target.count(x)) for x in filter(lambda rec: target.count(rec) > 1, target)))
# print(duplicates)
# from
# list(duplicates([1,1,2,1,2,3,4,2]))
# [1, 1, 2, 2]

#
# def checkio(data: set):
#     dupes = []
#
#     for x in data:
#         k = i
#         for j in
#         if x not in seen:
#             seen[x] = 1
#         else:
#             if seen[x] == 1:
#                 dupes.append(x)
#             seen[x] += 1
#     lst = list(data)
#     _size = len(lst)
#     rep = []
#     for i in range(_size):
#         k = i = 1
#         for j in range(k, _size):
#             if lst[i] == lst[j] and lst[i] not in rep:
#                 rep.append(lst[i])
#     return (rep)
#

# print(checkio([10, 20, 20, 10, 2, 1]))

# def Repeat(x):
#     _size = len(x)
#     repeated = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated
# Your code here
# It's main function. Don't remove this function
# It's used for auto-testing and must return a result for check.

# replace this for solution
# myset = set(data)
# return myset

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list

#
# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")
#


# Python program to print duplicates from a list


# # Driver Code
# list1 = [10, 20, 30, 20, 20, 30, 40,
#          50, -20, 60, 60, -20, -20]
# print(Repeat(list1))

# This code is contributed
# by Sandeep_anand
# mylist = ['nowplaying', 'PBS', 'PBS', 'nowplaying', 'job', 'debate', 'thenandnow']
# myset = set(mylist)
# print(myset)
