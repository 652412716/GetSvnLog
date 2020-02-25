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
    return climb_stairs_1(i + 1, n) + climb_stairs_1(i + 2, n)


def climb_stairs_2(i, n, memo):
    memo.append(0)
    if i > n:
        return 0
    if i == n:
        return 1

    if memo[i] > 0:
        return memo[i]

    memo[i] = climb_stairs_2(i + 1, n, memo) + climb_stairs_2(i + 2, n, memo)
    return memo[i]


def climb_stairs_3(n):
    if n == 1:
        return n
    count_list = [0 for x in range(0, n + 1)]
    i = 3
    count_list[1] = 1
    count_list[2] = 2
    while i <= n:
        count_list[i] = count_list[i - 1] + count_list[i - 2]
        i += 1

    return count_list[n]


def climb_stairs_4(n):  # 斐波那契数
    if n == 1:
        return 1

    if n == 2:
        return 2

    first = 1
    second = 2
    i = 3
    while i <= n:
        third = first + second
        first = second
        second = third
        i += 1

    return third


def climb_stairs_5():
    print "5"


# test_memo = []
#
# q = [[1, 1], [1, 0]]
#
#
# print "2", climb_stairs_2(0, 40, test_memo)
#
# print "3", climb_stairs_3(40)
#
# print "4", climb_stairs_4(40)

# print climb_stairs_1(0, 40)

def count_max_profit_1(prices):
    max_profit = 0
    idx = 0
    for price in prices:
        for n in range(idx + 1, len(prices)):
            match_price = prices[n]
            profit = match_price - price
            if profit > max_profit:
                max_profit = profit
        idx += 1
    return max_profit


def count_max_profit_2(prices):
    if not prices:
        return 0
    if len(prices) < 2:
        return 0
    max_profit = 0
    min_price = prices[0]
    for price in prices:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
    return max_profit


# prices_list = [7, 1, 5, 3, 6, 4]
# print count_max_profit_1(prices_list)
#
# print count_max_profit_2(prices_list)


def isHappy_1(num):
    str_num = str(num)
    next_num = 0
    num = num
    if num == 1:
        return True
    while next_num != 1:

        next_num = 0
        for i in str_num:
            next_num = next_num + int(i) ** 2

        if num == next_num:
            return False
        num = next_num
        str_num = str(next_num)

    if next_num == 1:
        return True

    if next_num == 1:
        return True


# print isHappy_1(2)


def letter_combination(letters):
    dict_1 = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    letter_list = ["", "", "", ""]
    letters_len = len(letters)
    for letter in letters:
        print dict_1[letter]


def count_list(letter_list, letters):
    print "ccc"
    idx = 0
    for letter in letters:
        letter_list[idx] = letter_list[idx]


# letter_combination("23")


def queue_test(k):
    test_list = [None for i in range(k)]
    print test_list.count(None)
    print test_list


def num_reverse(x):
    min_mun = (-2) ** 31
    max_mun = 2 ** 31 - 1
    print x
    print max_mun
    print x > max_mun
    if x < min_mun | x > max_mun:
        return 0

    is_negative = False
    numbers = x
    if x > 0:
        str_nums = str(numbers)
    else:
        is_negative = True
        str_nums = str(abs(numbers))

    reverse_str = str_nums[::-1]
    reverse_num = int(reverse_str)

    if is_negative:
        reverse_num = 0 - reverse_num

    if reverse_num < min_mun or reverse_num > min_mun:
        return 0

    return reverse_num


def orangesRotting(grid):
    bad_oranges = []
    good_oranges = []
    for i in range(len(grid)):
        line = grid[i]
        for j in range(len(line)):
            sub = line[j]
            if sub == 2:
                bad_oranges.append([i, j])
            elif sub == 1:
                good_oranges.append([i, j])

    return infectOranges(bad_oranges, good_oranges, 0)


def infectOranges(bad_oranges, good_oranges, count_time):
    new_bad_oranges = []
    maybe_bad = []
    can_infect = False
    for bad_orange in bad_oranges:
        x = bad_orange[0]
        y = bad_orange[1]
        maybe_bad.append([x + 1, y])
        maybe_bad.append([x - 1, y])
        maybe_bad.append([x, y + 1])
        maybe_bad.append([x, y - 1])

    for bad in maybe_bad:
        if bad in good_oranges:
            can_infect = True
            new_bad_oranges.append(bad)
            good_oranges.remove(bad)

    if can_infect:
        count_time += 1
        return infectOranges(new_bad_oranges, good_oranges, count_time)
    else:
        if len(good_oranges) > 0:
            return -1
        else:
            return count_time


print orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])