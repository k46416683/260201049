chosen_story=input('Enter a file path:')
file=open(chosen_story,'r')
letters_list=[]
story=''
memory=[]

for i in file:
  story+=i[:-1]+' '

words_in_story=story.split(' ')

counter=0
for i in words_in_story:

  if '“' in i:
    words_in_story[counter]=words_in_story[counter][1:]

  elif '”' in i:
    words_in_story[counter]=words_in_story[counter][:-2]

  if '.' in i:
    words_in_story[counter]=words_in_story[counter][:-1]

  if ',' in i:
    words_in_story[counter]=words_in_story[counter][:-1]   
  if "'" in i:
    words_in_story[counter]=words_in_story[counter][:-2]+words_in_story[counter][:1]
  counter+=1  
    
print(words_in_story)

while True:

  letters=input('Enter a list of letters:')

  if letters=='':
    print('Invalid input.')

  elif letters=='quit':
    print('Goodbye!')
    quit()

  else:  
    for a in letters:
      if a.isalpha():
        letters_list.append(a.lower())
    print(letters_list)



  for i in letters_list:
    for x in words_in_story:
      if i in x.lower():
        memory.append(x)
    if len(memory)==0:
      print(i+':'+'Letters not found!')
    else:      
      longest_letter_mem=max(memory, key=len).lower()
      memory=[]
      print(i+':'+longest_letter_mem) 

  memory=[]
  longest_letter_mem=''