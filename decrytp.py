k=[3,]
decyrpted_list=[]
a=0
for i in range(10,11):
  for b in k:
    a=b-i
    a=a%26
    decyrpted_list.append(a)   
  print(decyrpted_list)  
  decyrpted_list=[]