n=int(input('enter number'))
factorial=1
if n>=0:
  for i in range(1,n+1):
    factorial=factorial*i
  print(factorial)  
else:
  print('factorial can not be calculated because of negative number')      