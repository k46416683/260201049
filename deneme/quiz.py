password='abc123'
counter=0
while counter!=3:
  users_input=input('Enter the password')
  if users_input==password:
    print('You have successfully logged in')
    break
  else:
    print('Sorry, the password is wrong')
    counter+=1

if counter==3:
  print('You have been denied access')