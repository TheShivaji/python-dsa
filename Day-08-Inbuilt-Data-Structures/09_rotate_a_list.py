def rotate_list(lst, k):

    view_list = []

    for i in range(len(lst) - k, len(lst)):
        view_list.append(lst[i])

    for i in range(abs(0) , len(lst) - k):
      view_list.append(lst[i])

    print(view_list)



lst = [1, 2, 3, 4, 5]
k = 2

rotate_list(lst, k)
