def file_read():
  file=open('users.txt','r')
  users={}
  users_pass=''
  users_friends=''
  users_values=[]
  for i in file:
    user=i.split(';')[0]
    users_pass=i.split(';')[1]
    users_friends=i.split(';')[2][:-1]
    users_values.append(users_pass)
    users_values.append(users_friends)
    users[user]=users_values
    users_values=[]
  return users

logined_user=False

users=file_read()

def login_user(users):
  username=input("Please enter username:\n")
  password=input('Please enter password:\n')
  if username in users.keys():

    if password==users[username][0]:
      print("Logged in\n")
      return username
    else:
      print('Wrong password or username\n')
      return False
  else:
    print('Wrong password or username\n')
    return False


def check_name(users):
  username=input("Please enter username:\n").strip()
  if username not in users.keys():

    if 4<=len(username)<=8:
      username=username.lower()

      return username
    else:

      return False
  else:
    return False    


def check_pass():
    password=input('Please enter password:\n')
    alpha_ct=0
    digit_ct=0
    for i in password:
      if i.isdigit():
        digit_ct+=1
      elif i.isalpha():
        alpha_ct+=1
    if alpha_ct and digit_ct >0:
      return password
    else:  
      return False


def register_user(users):
  checked_name=check_name(users)
  checked_pass=check_pass()
  if check_name!=False:

    if checked_name and checked_pass !=False:
      users[checked_name]=[checked_pass,'']

    else:
      print('Password not valid\n')
  else:
    print('Username not valid\n')


def add_friend(users,login_user):
  if logined_user==False:
    print('You need to log in first\n')
  else:  
    friend=input('Please enter the name of your new friend:\n')
    if friend in users.keys():
      if len(users[logined_user][1])==0:
        list_of_new_friends=users[logined_user][1]+friend
        users[logined_user][1]=list_of_new_friends
      else:
        list_of_new_friends=users[logined_user][1]+','+friend
        users[logined_user][1]=list_of_new_friends
    else:
      print('Friend not found\n')  


def show_my_friends(users,login_user):
  if logined_user==False:
    print('You need to log in first\n')
  else:   
    print((users[logined_user])[1])


def menu():
  choice=int(input('1. Log in / change user\n2. Create new user\n3. Add friend\n4. Show my friends\n5. Exit\n'))
  return choice


def exit(users):
  file=open('users.txt','w')
  new_datas=''
  for i in users.keys():
    new_datas+=i+';'+users[i][0]+';'+users[i][1]+'\n'
  file.write(new_datas)
  quit()  


    
while True:
  choice=menu()
  if choice==1:
    logined_user=login_user(users)
  elif choice==2:
    register_user(users)    
  elif choice==3:
    add_friend(users,logined_user)     
  elif choice==4:
    show_my_friends(users,logined_user)
  elif choice==5:
    exit(users)
  else:
    print('Invalid option\n') 

   