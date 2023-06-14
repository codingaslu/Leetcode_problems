# write code here
def sumsquare(l):

  result = [
    sum(i**2 for i in l if i % 2 != 0),
    sum(i**2 for i in l if i % 2 == 0)
  ]

  # even = [i**2 for i in l if i % 2 == 0]
  # odd = [i**2 for i in l if i % 2 != 0]
  # result = [sum(odd), sum(even)]

  return result


# Suffix code
L = eval(input())
print(sumsquare(L))
