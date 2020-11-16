a=int(input('please write number'))
odd=0
for i in range(a):
  b=int(input('please write your number'))
  if b%2==1:
    odd+=1
print(odd)    
print((odd/a)*100,'%')    