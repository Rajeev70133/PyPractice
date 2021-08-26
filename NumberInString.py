# n a given text you need to sum the numbers while excluding any digits that form part of a word.
# The text consists of numbers, spaces and letters from the English alphabet.
# Input: A string.
# Output: An int.
import re


def sum_numbers(text: str) -> int:
    return sum(int(i) for i in text.split() if i.isdigit())


if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('This picture is an oil on canvas '
                      'painting by Danish artist Anna '
                      'Petersen between 1845 and 1910 year'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
                       'painting by Danish artist Anna '
                       'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")

    # printing total value

    # your code here
    # lst = list(text)
    # for i in lst.split():
    #     if isdigit():
    #
    # return 0
    # return sum(int(word) for word in text.split() if word.isdigit())
    # witout_space = text.replace(" ", "")
    # #  return sum_numbers(text)
    # temp = re.findall(r'(\d+)', witout_space)
    # res = list(map(int, temp))
    # total = 0
    # for ele in range(0, len(res)):
    #     total = total + res[ele]
    #     return total
    # if not res:
    #     return 0
