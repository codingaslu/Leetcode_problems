def expanding(l):
  length = len(l)

  if length < 2:
    return False

  difference = abs(l[1] - l[0])

  for i in range(1, length - 1):
    current_diff = abs(l[i + 1] - l[i])

    if current_diff <= difference:
      return False

    difference = current_diff

  return True


# Test the function
L = eval(input())
print(expanding(L))
