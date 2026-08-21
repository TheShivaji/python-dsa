def compare_strings(str1 , str2):
  if len(str1) != len(str2):
    return False

  for i in range(0 , len(str1) , 1):
    if str1[i] != str2[i]:
      return False

  return True


s = "hello"
t = "hellc"

print(compare_strings(s , t))
