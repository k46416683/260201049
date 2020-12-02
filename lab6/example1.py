mail='ceng113@example.com'
email=input('enter email adress')
seperated_email=email.split('@')
while True:
  if mail==email.lower() and '.' not in seperated_email[0] :
    print('equal')
    break
  else:
    print('not equal')
    pass  

    
  