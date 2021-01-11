a=open('flight.txt','r')

flight=[]
tarihler=[]
konum=[]
saat=[]
süre=[]
varış=[]
for i in a:
  x=i.split(';')
  flight.append(x)

for i in flight:
  tarihler.append(i[0])
  konum.append(i[1])
  saat.append((i[2]))
  süre.append(i[3][:5])

for (x,y) in zip(saat,süre):
  varış.append(str(int(x[:2])+int(y[:2])+(int(x[3:])+int(y[3:]))//60)+':'+str((int(x[3:])+int(y[3:]))%60))


for i in range(len(varış)):
  if int(varış[i][:2])>23:
    tarihler[i]=str(int(tarihler[i][:2])+1)+tarihler[i][2:]
  if len(varış[i])==4:
    varış[i]+='0'
  varış[i]=str(int(varış[i][:2])%24)+varış[i][2:]
  if len(varış[i])==4:
    varış[i]='0'+varış[i]


     
print(varış)
print(tarihler)


































a.close()