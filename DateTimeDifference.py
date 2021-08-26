from datetime import date, timedelta


def days_diff(a, b):
    date1 = date(*a)
    date2 = date(*b)
    # your code here
    return abs(date1-date2).days


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")

# from datetime import date
#
#
# def numOfDays(date1, date2):
#     return (date2 - date1).days
#
#
# # Driver program
# date1 = date(2018, 12, 13)
# date2 = date(2019, 2, 25)
# print(numOfDays(date1, date2))

# delta = timedelta(days=50, hours=8, weeks=2)
# print(delta)

#
# f = date(2014, 12, 31)
# s = date(2011, 1, 1)
# print(abs(f - s).days)
# # diff = f - s
# # print(timedelta().days)
# # # diff == datetime.timedelta(diff)
# # print(abs(diff))
# # # print(diff)