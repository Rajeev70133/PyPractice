# You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.
#
# For an empty array, the result will always be 0 (zero).
#
# Input: A list of integers.
#
# Output: The number as an integer.
#
# Precondition: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

def checkio(array: list) -> int:
    if len(array) == 0:
        return 0
    result = 0
    for i in range(len(array)):
        if not i % 2:
            result += array[i]
    return result * array[-1]
    # result = 0
    # for i in range(0, len(array), 2):
    #     result += array[i]
    #
    # return result
        # a = 0
    # if array[0]==0:
    #     for i in range(1, len(array), 2):
    #         a=i+1
    # else:
    #     for i in range(0, len(array), 2):
    #         a=i+1
    # a=a*array[-1]
    # return a
    #
    # """
    #     sums even-indexes elements and multiply at the last
    # """


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio([0, 1, 2, 3, 4, 5]))

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# print(u'Hello World !')
# print(u'Hello\u0020World !')

# a, b = 0, 1
# while b < 20:
#     print(b)
#     a, b = b, a + b

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# print(letters)
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# letters[2:5] = []
# print(letters)
# # letters[:]= []
# # print(letters)
# print(len(letters))
# a =['a', 'b', 'c', 'd']
# n= [1, 2, 3]
# x=[a, n]
# print(x)
# print(x[0])
# print(x[1][2])
# squares = [1, 4, 9, 16, 25]
# print(squares[-1])
# print(squares[-3:])
# print(squares[:])
# a= squares + [36, 49, 64, 81, 100]
# print(a)
# b = 4 ** 4
# print(b)
# def Ittera2n():
#     a = dict(one=1, two=2, three=3)
#     b = {'one': 1, 'two': 2, 'three': 3}
#     c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
#     d = dict([('two', 2), ('one', 1), ('three', 3)])
#     e = dict({'three': 3, 'one': 1, 'two': 2})
#     f = dict({'one': 1, 'three': 3}, two=2)
#     return d.keys()
#
#
# print(Ittera2n())

# print(Ittera2n())

# >>> b = {'one': 1, 'two': 2, 'three': 3}
# >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
# >>> e = dict({'three': 3, 'one': 1, 'two': 2})
# >>> f = dict({'one': 1, 'three': 3}, two=2)
