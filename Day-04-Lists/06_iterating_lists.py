# ============================================================
#          Day-04 | 06 - Iterating Lists
# ============================================================


# Q1 ⭐ — Print Every Element
# languages = ["Python", "JavaScript", "Java", "C++", "Go"]
# for loop se har language print karo.
# Expected:
#   Python
#   JavaScript
#   Java
#   C++
#   Go

languages = ["Python", "JavaScript", "Java", "C++", "Go"]

for language in languages:
    print(language)



# -------------------------------------------------------

# Q2 ⭐ — Print Numbers
# numbers = [10, 20, 30, 40, 50]
# Loop se har number print karo.

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(f"number is : {number}")


# -------------------------------------------------------

# Q3 ⭐⭐ — Even Numbers
# numbers = [10, 15, 22, 31, 40, 55, 60]
# Sirf even numbers print karo.
# Expected: 10, 22, 40, 60

numbers = [10, 15, 22, 31, 40, 55, 60]

for num in numbers:
    if(num % 2 == 0):
        print(num)



# -------------------------------------------------------

# Q4 ⭐⭐ — Odd Numbers
# numbers = [10, 15, 22, 31, 40, 55, 60]
# Sirf odd numbers print karo.
# Expected: 15, 31, 55

numbers = [10, 15, 22, 31, 40, 55, 60]

for num in numbers:
    if(num % 2 != 0):
        print(num)



# -------------------------------------------------------

# Q5 ⭐⭐ — Sum of List
# numbers = [10, 20, 30, 40, 50]
# Loop use karke total calculate karo.
# Expected: 150
# ⚠️ sum() function use nahi karna.

numbers = [10, 20, 30, 40, 50]
result = 0;
for num in numbers:
    result+=num

print(result)



# -------------------------------------------------------

# Q6 ⭐⭐ — Find Largest
# numbers = [10, 45, 23, 89, 12, 67]
# Loop se largest number find karo.
# Expected: 89
# ⚠️ max() use nahi karna

max_num = 0;

numbers = [10, 45, 23, 89, 12, 67]

for max in numbers:
    if(max > max_num):
        max_num = max

print(max_num)



# -------------------------------------------------------

# Q7 ⭐⭐⭐ — Count Even Numbers
# numbers = [10, 15, 22, 31, 40, 55, 60]
# Kitne even numbers hain, count karo.
# Expected: 4

numbers = [10, 15, 22, 31, 40, 55, 60]
count = 0;
for num in numbers:
    if(num % 2 == 0):
        count+=1

print(count)
    



# -------------------------------------------------------

# Q8 ⭐⭐⭐ — Count Positive Numbers
# numbers = [-10, 20, -5, 30, 0, 15, -2]
# Sirf positive numbers count karo.
# Expected: 3

numbers = [-10, 20, -5, 30, 0, 15, -2]

positive_num = 0

for num in numbers:
    if(num > 0):
        positive_num+=1

print(positive_num)



# -------------------------------------------------------

# Q9 ⭐⭐⭐ — Create New List (Squares)
# numbers = [1, 2, 3, 4, 5]
# Loop use karke ek new list banao jisme har number ka square ho.
# Expected: [1, 4, 9, 16, 25]
# ⚠️ Abhi list comprehension use nahi karna. Normal for loop.

numbers = [1, 2, 3, 4, 5]
square = []
for num in numbers:
    square.append(num ** 2)

print(square)




# -------------------------------------------------------

# Q10 🧠 — Separate Even & Odd
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Do new lists banao:
#   Even: [2, 4, 6, 8, 10]
#   Odd:  [1, 3, 5, 7, 9]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even = []
odd = []

for num in numbers:
    if(num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)


print(even)
print(odd)


