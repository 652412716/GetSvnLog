# coding=utf-8
import time

nums = [0, 1, 2, 2, 3, 4, 2]
val = 2
out_string = ""


def romanToInt(s):
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IX": 8, "IV": 3, "XL": 30, "XC": 80,
                 "CD": 300, "CM": 800}
    # return sum(roman_dic.get(s[max(i - 1, 0):i + 1], roman_dic[n]) for i, n in enumerate(s))
    for i, n in enumerate(s):
        print("i=", i)
        print("n=", n)
        print("max=", max(i - 1, 0))
        print s[max(i - 1, 0):i + 1]
        print roman_dic[n]
        print(roman_dic.get(s[max(i - 1, 0):i + 1], roman_dic[n]))
        print "-------------------"


# romanToInt("IVI")


def climb_stairs_1(i, n):
    if i > n:
        return 0
    elif i == n:
        return 1
    return climb_stairs_1(i+1, n) + climb_stairs_1(i+2, n)


def climb_stairs_2(i, n, memo):
    memo.append(0)
    if i > n:
        return 0
    if i == n:
        return 1

    if memo[i] > 0:
        return memo[i]

    memo[i] = climb_stairs_2(i+1, n, memo) + climb_stairs_2(i+2, n, memo)
    return memo[i]


def climb_stairs_3(n):
    if n == 1:
        return n
    count_list = [0 for x in range(0, n+1)]
    i = 3
    count_list[1] = 1
    count_list[2] = 2
    while i <= n:
        count_list[i] = count_list[i-1] + count_list[i-2]
        i += 1

    return count_list[n]


def climb_stairs_4(n):  # 斐波那契数
    if n == 1:
        return 1

    first = 1
    second = 2
    i = 3
    while i <= n:
        third = first + second
        first = second
        second = third

    return third


test_memo = []


print "2", climb_stairs_2(0, 40, test_memo)

print "3", climb_stairs_3(40)

print "4", climb_stairs_4(40)

# print climb_stairs_1(0, 40)

