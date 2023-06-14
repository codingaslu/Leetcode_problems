# write code here
def histogram(l):
  counts = {}

  for num in l:
    if num in counts:
      counts[num] += 1
    else:
      counts[num] = 1
  h = []
  for num in counts:
    h.append((num, counts[num]))

  h.sort()
  h.sort(key=lambda x: (x[1], x[0]))
  return h


# sufix code
L = eval(input())
print(histogram(L))
