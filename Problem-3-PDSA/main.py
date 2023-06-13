
# Write code here
def shuffle(l1,l2):
  result=[]
  length = max(len(l1),len(l2))

  for i in range(length):
    if i < len(l1):
      result.append(l1[i])
    if i < len (l2):
      result.append(l2[i])
  return result    

# suffix Code
L1 = eval(input())
L2 = eval(input())
print(shuffle(L1,L2))