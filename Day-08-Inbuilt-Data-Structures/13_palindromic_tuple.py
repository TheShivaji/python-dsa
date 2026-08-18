def is_palindromic_tuple(tup):
    print(len(tup))
    reversed_tup = ()
    for num in range(len(tup) - 1, -1, -1):
        reversed_tup += (tup[num],)

    if reversed_tup == tup:
        return True


    return False


is_palindromic_tuple((1, 2, 3, 2, 1))


print(is_palindromic_tuple((1, 2, 3, 4, 5)))
