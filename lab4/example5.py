n=int(input('enter number'))
factorial=1
if n>0:
  for i in range(1,n+1):
    factorial=factorial*i
  print(factorial)  
elif n==0:
  print(1)
else:
  print('factorial can not be calculated because of negative number')      