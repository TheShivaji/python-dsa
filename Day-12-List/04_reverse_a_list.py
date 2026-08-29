def reverse_list(lst):
    reverse_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reverse_lst.append(lst[i])

    return reverse_lst


lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
