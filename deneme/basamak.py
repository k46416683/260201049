Sx=int(input('gir'))
while x>0:
  print(len(str(x)),'digit',x//(10**(len(str(x))-1)))
  x=x%10**(len(str(x))-1)
