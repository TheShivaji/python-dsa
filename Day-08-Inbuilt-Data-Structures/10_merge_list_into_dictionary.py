keys = ["name", "age", "city"]
values = ["Shivaji", 21, "Jalgaon"]

i = 0
j = 0
data = {}
while i < len(keys) and j < len(values):
    data[keys[i]] = values[j]

    i+=1
    j+=1


print(data)
