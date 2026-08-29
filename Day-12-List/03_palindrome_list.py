def palindrome(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1

    return True


lst = [7, 8, 9, 8, 7]
print(palindrome(lst))
