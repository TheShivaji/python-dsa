def remove_spaces(s):

  str_no_space = ""

  space = " "

  for i in s:
      if i != space:

        str_no_space+=i

  return str_no_space




s = "Hello World"

print(remove_spaces(s))
