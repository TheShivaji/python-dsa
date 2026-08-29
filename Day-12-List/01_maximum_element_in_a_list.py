def maximum_element(list):
    num = list[0]
    for i in list:
        if i > num:
            num = i
    return num


# lst = [3, 5, 2, 9, 6]
lst = [-1, -2, -3, -4]
print(maximum_element(lst))
