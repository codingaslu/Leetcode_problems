def is_prime(n):
  if n <= 1:
    return False
  for i in range (2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

def primeproduct(m):
  if m < 0:
    return False

  for i in range (2,int(m**0.5)+1):
    if m%i==0:
      if is_prime(i) and is_prime(m//i):
        return True
        
  return False
  
  

#Suffix Code
n = int(input())
print(primeproduct(n))