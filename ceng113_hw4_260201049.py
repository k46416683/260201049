#260201049
#here there are variables that need to assign at the begin
pegasus_hp=550
hero_hp=3000
pegasus_lose=15
hero_lose=10
hero_speed=20
pegasus_speed=50
total_time=0


def file_reading():#this function reads the task list file and return a task list
  task_file=open('TaskList.txt','r')
  task_list=task_file.readlines()

  for i in range(len(task_list)):
    task_list[i]=task_list[i].replace('\n','')
    task_list[i]=[task_list[i].split(',')[0],task_list[i].split(',')[1],task_list[i].split(',')[2],task_list[i].split(',')[3]]
  return task_list

task_list=file_reading()


def print_remaining_task(task_list):#this function printing task table recursively
  if len(task_list)==0:
    pass
  else:
    print(str('| '+ task_list[0][0] +'\t \t| '+ task_list[0][1] +'\t\t\t|\t '+ task_list[0][2] +'\t|\t '+ task_list[0][3] +' \t|\t'))
    return print_remaining_task(task_list[1:])

#here ı print necessary things that menu has     
print('Welcome to Hero’s 5 Labors!') 
print('Remaining HP for Hero : ',hero_hp) 
print('Remaining HP for Pegasus : ',pegasus_hp)
print('Here are the tasks left that hero needs to complete:')
print('-----------------------------------------------------')
print('| TaskName  | ByFootDistance| ByPegasus | HPNeeded  | ')
print('-----------------------------------------------------')
print_remaining_task(task_list)
print('-----------------------------------------------------')

task_list2=task_list
def remove_task(task_list,task,task_list2):#here ı remove completed task from task list recursively
  if task==task_list2[0][0]:
    return task_list.remove(task_list2[0])
  return remove_task(task_list,task,task_list2[1:])


while True:#main program start from here
  passed_time=0
  tasks=[]#ı used this tasks list for just take task names 
  for i in task_list:
    tasks.append(i[0])

  if len(task_list)==0:#this if statement true when only game finished
    print('Congratulations, you have completed the task.')
    name=input('What is your name :')
    Hall_of_fame=open('Hall_of_fame.txt','a+')#ı used a+ for apending name and time to hall of fame txt if there is no file then file will created thanks to a+
    Hall_of_fame.write(name+','+str(total_time)+'\n')
    Hall_of_fame.close()
    Hall_of_fame=open('Hall_of_fame.txt','r')
    names={}
    data=[]
    for i in Hall_of_fame:#here ı create special list for sorting
      names['names']=i.split(',')[0]
      names['finish_time']=int(i.split(',')[1][:-1])
      data.append(names)
      names={}

    def myFunc(e):#this function will return the finish_time for sorting
      return e['finish_time']

    data.sort(key=myFunc)


    print('Hall Of Fame')
    print('--------------------------')
    print('| Name\t\t| Finish Time |')
    print('--------------------------')
    counter=0
    for i in data:#this for loop printing first 3 names that finished the game ı used counter for printing just for 3 names
      name=str(i['names'])
      finish_time=str(i['finish_time'])
      if counter==3:
        exit()
      print('| '+(name)+'\t\t| '+(finish_time)+' hour\t |')
      print('--------------------------')
      counter+=1

    exit()


  task=input('Where should hero go next?').capitalize()
  if task not in tasks:#when the user enter wrong task the program start asking again
    print('Invalid Input')
  else:
    place=tasks.index(task)#this variable find the list place in 2dlist
    while True:
      travel_type=input('How do you want to travel?(Foot/Pegasus)').capitalize()
      if travel_type not in ('Pegasus','Foot'):
        print('Invalid Input')
      elif travel_type=='Foot' and task in ('Task1','Task2'):
        print('You cannot go there by foot.')
      else:

        if pegasus_hp<pegasus_lose*(int(task_list[place][2]))/pegasus_speed and travel_type=='Pegasus':
          if task in ('Task1' ,'Task2'):
            print('Game over')
            exit()

          else:

            print('Pegasus does not have enough HP.')

        else:


          if travel_type=='Pegasus':    
     
            passed_time=int(task_list[place][2])/pegasus_speed
            hero_hp-=int(task_list[place][3])
            pegasus_hp-=passed_time*pegasus_lose
            total_time+=int(passed_time)
            print('Hero defeated the monster.')
            print('Time passed :',total_time,'hour\n' )
            print('Remaining HP for Hero :',int(hero_hp)) 
            print('Remaining HP for Pegasus:',int(pegasus_hp),'\n')

          elif travel_type=='Foot':

            passed_time=int(task_list[place][1])/hero_speed
            hero_hp-=int(task_list[place][3])+passed_time*hero_lose
            total_time+=int(passed_time)
            print('Hero defeated the monster.')
            print('Time passed :',total_time ,'hour\n')
            print('Remaining HP for Hero :',int(hero_hp)) 
            print('Remaining HP for Pegasus:',int(pegasus_hp),'\n')

          while True:#this while loop implent go home part

            travel_type=input('How do you want to go home?(Foot/Pegasus)').capitalize()
            if travel_type not in ('Pegasus','Foot'):

              print('Invalid Input')

            elif travel_type=='Foot' and task in ('Task1','Task2'):

              print('You cannot go there by foot.')
            
              

            else:

              if pegasus_hp<pegasus_lose*(int(task_list[place][2]))/pegasus_speed and travel_type=='Pegasus':

                if task in ('Task1' ,'Task2'):
                  print('Game over')
                  exit()

                else:

                  print('Pegasus does not have enough HP.')

              else:

                if travel_type=='Pegasus':   

                  passed_time=int(task_list[place][2])/pegasus_speed
                  pegasus_hp-=passed_time*pegasus_lose
                  total_time+=int(passed_time)
                  print('Hero defeated the monster.')
                  print('Hero arrived home.')
                  print('Time passed :',total_time,'hour\n')
                  remove_task(task_list,task,task_list2)
                  if task_list==[]:#ı control the game if it finish or not to not write task list again
                    break 
                  print('Remaining HP for Hero :',int(hero_hp)) 
                  print('Remaining HP for Pegasus:',int(pegasus_hp),'\n')
                  
                  print('-----------------------------------------------------')
                  print('| TaskName  | ByFootDistance| ByPegasus | HPNeeded  | ')
                  print('-----------------------------------------------------')
                  print_remaining_task(task_list)
                  print('-----------------------------------------------------')
                  break

                elif travel_type=='Foot':

                  passed_time=int(task_list[place][1])/hero_speed
                  hero_hp-=passed_time*hero_lose
                  total_time+=int(passed_time)
                  print('Hero defeated the monster.')
                  print('Hero arrived home.')
                  print('Time passed :',total_time,'hour\n' )
                  remove_task(task_list,task,task_list2)
                  if task_list==[]:#ı control the game if it finish or not to not write task list again
                    break 
                  print('Remaining HP for Hero :',int(hero_hp)) 
                  print('Remaining HP for Pegasus:',int(pegasus_hp),'\n')
                  
                  

                  print('--------------------------------------------------------')
                  print('| TaskName  | ByFootDistance| ByPegasus | HPNeeded  | ')
                  print('--------------------------------------------------------')
                  print_remaining_task(task_list)
                  print('-----------------------------------------------------')
                  break
          break
    