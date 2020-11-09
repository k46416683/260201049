a=int(input('write number'))
b=int(input('write number'))
c=1
if b>0:
  for i in range(b):
    c=c*a
  print(c)
else:
  for i in range(b):
    c=c/a
  print(c)      