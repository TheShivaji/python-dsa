def is_subset(lst1, lst2):
    for element in lst1:
        found = False

        for item in lst2:
            if element == item:
                found = True
                break

        if not found:
            return False

    return True


lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]

print(is_subset(lst1, lst2))
