def cal_rounds(n, capacity):
    rounds = n // capacity

    if n % capacity != 0:
        rounds += 1

    return rounds


print(cal_rounds(10, 3))
print(cal_rounds(7, 4))
print(cal_rounds(12, 3))


def calculate_vans(packages, capacity):
     vans_req = packages // capacity
     if packages % capacity != 0:
        vans_req+=1

     return vans_req

print(calculate_vans(20 , 5))

