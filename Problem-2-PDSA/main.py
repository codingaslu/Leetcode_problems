# write here
def del_char(s, c):
  if len(c) != 1:
    return s
  # result = ""
  # for i in s:
  #   if i == c:
  #     continue
  #   result = result + i
  # return result
  result ="".join([char for char in s if char!=c ])
  return result

# suffix code
s = input()
c = input()
print(del_char(s, c))
