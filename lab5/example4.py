password='abc123'

while True:
  entered_password=input('enter password')
  if password==entered_password:
    print('welcome')
    break
  elif entered_password=='help':
    print(password[0])
  else:
    print('wrong password')  


  