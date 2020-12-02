eq1=input('Enter the first equation:\n')
eq2=input('Enter the second equation:\n')

splited_eq1=eq1.split('=')
splited_eq2=eq2.split('=')

left_side_eq1,right_side_eq1=splited_eq1[1],splited_eq1[0]
left_side_eq2,right_side_eq2=splited_eq2[1],splited_eq2[0]

left_side_eq1=left_side_eq1.replace('+','!')
left_side_eq1=left_side_eq1.replace('-','+')
left_side_eq1=left_side_eq1.replace('!','-')

left_side_eq2=left_side_eq2.replace('+','!')
left_side_eq2=left_side_eq2.replace('-','+')
left_side_eq2=left_side_eq2.replace('!','-')

eq1=right_side_eq1+left_side_eq1
eq2=right_side_eq2+left_side_eq2
a,b,c,d,e,f=0,0,0,0,0,0
memory_coef=''
for i in range(len(eq1)-1,-1,-1):
  memory_coef+=eq1[i]

  if eq1[i]=='+':
    if 'x' in memory_coef:

      a+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    elif 'y' in memory_coef:

      b+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    else:    

      c+=int(memory_coef[::-1])
      memory_coef=''

  elif eq1[i]=='-':
    if 'x' in memory_coef:

      a+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    elif 'y' in memory_coef:

      b+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    else:

      c+=int(memory_coef[::-1])
      memory_coef=''

for i in range(len(eq2)-1,-1,-1):
  memory_coef+=eq2[i]

  if eq2[i]=='+':
    if 'x' in memory_coef:

      d+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    elif 'y' in memory_coef:

      e+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    else:    

      f+=int(memory_coef[::-1])
      memory_coef=''

  elif eq2[i]=='-':
    if 'x' in memory_coef:

      d+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    elif 'y' in memory_coef:

      e+=int(memory_coef[len(memory_coef)-1:0:-1])
      memory_coef=''

    else:

      f+=int(memory_coef[::-1])
      memory_coef=''
if b<0:
  updated_eq1=str(a)+'x'+str(b)+'y'+'='+str(-c)
else:  
  updated_eq1=str(a)+'x'+'+'+str(b)+'y'+'='+str(-c)

if e<0:
  updated_eq2=str(d)+'x'+str(e)+'y'+'='+str(-f)
else:
  updated_eq2=str(d)+'x'+'+'+str(e)+'y'+'='+str(-f)  
c=-c
f=-f
multipler=-b/e
result_x=(c-(b/e)*f)/(a-(b/e)*d)
result_y=(c-a*result_x)/b
print('Equations in the simplified form:')
print(updated_eq1)
print(updated_eq2)
print('Solution:')
print('x='+str(int(result_x)))
print('y='+str(int(result_y)))