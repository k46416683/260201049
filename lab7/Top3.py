x={}
for i in range(5):
  name=(input('enter your name'))
  salary=int(input('enter your salary'))
  x[name]=salary
sorted_list=sorted(x.values())
print(sorted_list[-2:])