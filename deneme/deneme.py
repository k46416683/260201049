infile=open('sayılar.txt','r')
summ=str
count=0
line=infile.readline()
while line!='':
  summ=(line)
  count+=1
  print(line)
  line=infile.readline()
  
print(summ)  