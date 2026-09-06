# rows = 4
# columns = 6

# for i in range(rows):
#     row = ""
#     for j in range(columns):
#         if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
#             row += "*"
#         else:
#             row += " "

#     print(row)

# # Revision Q2 — Increasing Triangle

# n = 5

# for i in range(n):
#     row = ""
#     for j in range(n):
#         if j <= i:
#             row += "*"
#     print(row)


# # Revision Q3 — Pyramid

# n = 5

# for i in range(1, n + 1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)

#     print(spaces, stars)


# # Revision Q4 — Inverted Pyramid

# n = 5
# for i in range(n, 0, -1):
#     spaces = " " * (n - i)
#     stars = "*" * (2 * i - 1)

#     print(spaces, stars)


# # Revision Q5 — Floyd's Triangle

# n = 5

# number = 1
# for i in range(1, n + 1):
#     row = ""
#     for j in range(1, n + 1):
#         if j <= i:
#             row += str(number) + " "
#             number = number + 1
#     print(row)

# # Warm-up Q1 — Hollow Rectangle

# rows = 5
# columns = 7

# for i in range(rows):
#     row = ""
#     for j in range(columns):
#         if i == 0 or j == 0 or i == rows - 1 or j == columns - 1:
#             row += "*"
#         else:
#             row += " "
#     print(row)


# n = 5

# for i in range(1, n + 1):
#     row=""
#     spaces = " " * (n - i)
#     for j in range(1, 2 * i):
#             row += str(j)

#     print(spaces , row)

# numbers = [2, 3, 2, 5, 3, 2]
# freq = {}
# for num in numbers:
#     if num in freq:
#         freq[num] = freq[num] + 1
#     else:
#         freq[num] = 1

# print(freq)


# def merge_dictionaries(dict1, dict2, dict3):
#     merge_dict = dict1.copy()

#     for key, val in dict2.items():
#         merge_dict[key] = val
#     for key, val in dict3.items():
#         merge_dict[key] = val

#     return merge_dict


# dict1 = {"name": "Shivaji"}
# dict2 = {"age": 21}
# dict3 = {"city": "Jalgaon"}

# print(merge_dictionaries(dict1, dict2, dict3)


# def palindromic_tuple(tup):
#     reverse_tup = ()
#     for i in range(len(tup) - 1, -1, -1):
#         reverse_tup += (tup[i],)

#     if tup == reverse_tup:
#         return True

#     return False


# tup = ("a", "b", "c", "b", "a")
# print(palindromic_tuple(tup))

# =========================
# Q1 — Second Largest
# =========================

nums = [12, 5, 8, 20, 15, 20]

largest = float("-inf")
second_largest = float("-inf")

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)


# =========================
# Q2 — Remove Duplicates
# =========================

nums = [3, 5, 3, 2, 5, 8, 2]

result = []

for num in nums:
    if num not in result:
        result.append(num)

print(result)


# =========================
# Q3 — Character Frequency
# =========================

text = "banana"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)


# =========================
# Q4 — Count Vowels
# =========================

text = "programming"

vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(count)


# =========================
# Q5 — Even + Greater Than 10
# =========================


def even_also_greater_than_ten(nums):
    result = []

    for num in nums:
        if num % 2 == 0 and num > 10:
            result.append(num)

    return result


nums = [4, 12, 7, 20, 9, 16, 3]

print(even_also_greater_than_ten(nums))


# =========================
# Q6 — Binary Search
# =========================


def binary_search(nums, target):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return False


nums = [2, 5, 8, 12, 16, 23, 38, 45]

print(binary_search(nums, 16))


# =========================
# Q7 — Positive / Negative / Zero
# =========================

nums = [3, -2, 0, 7, -5, 0, 4]

positive_count = 0
negative_count = 0
zero_count = 0

for num in nums:
    if num == 0:
        zero_count += 1
    elif num < 0:
        negative_count += 1
    else:
        positive_count += 1

print("Positive =", positive_count)
print("Negative =", negative_count)
print("Zero =", zero_count)


# =========================
# Q8 — Reverse In-Place
# =========================

nums = [1, 2, 3, 4, 5]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1

print(nums)


# =========================
# Q9 — Number Frequency
# =========================

nums = [2, 3, 2, 5, 3, 2, 4]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)


# =========================
# Q10 — String Palindrome
# =========================


def palindrome(text):
    reversed_text = ""

    for i in range(len(text) - 1, -1, -1):
        reversed_text += text[i]

    if text == reversed_text:
        return True

    return False


text = "madam"

print(palindrome(text))


# =========================
# Q11 — Linear Search
# =========================


def linear_search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i

    return -1


nums = [10, 25, 7, 18, 30]

print(linear_search(nums, 18))


# =========================
# Q12 — Smallest Element + Index
# =========================


def smallest(nums):
    smallest_index = 0

    for i in range(1, len(nums)):
        if nums[i] < nums[smallest_index]:
            smallest_index = i

    return smallest_index, nums[smallest_index]


nums = [8, 3, 12, 5, 1, 9]

print(smallest(nums))
