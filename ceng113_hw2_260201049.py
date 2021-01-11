provinces=open('provinces.txt','r')
provinces_list=[]
provinces_dict={}
possible_cities=[]
travel_types={'Car':90,'Motorcycle':80,'Bicycle':25}
distances=[]
closest_city_finder=[]
closest_cities_distance=[]

for i in provinces:

  provinces_list.append(i)

for i in range(len(provinces_list[:-1])):

  provinces_list[i]=provinces_list[i][:-1]

for i in provinces_list:

  city=i.split(',')[0]
  x=i.split(',')[1]
  y=i.split(',')[2]
  xy=[float(x),float(y)]
  provinces_dict[city]=xy

while True:
  possible_cities=[]
  departure=input('Departure province:\n').upper()

  if departure not in provinces_dict.keys():

    print('Province not found!')


    for i in provinces_dict.keys():

      if i.startswith(departure):

        possible_cities.append(i)
        

    if len(possible_cities)>1:
      
      possible_cities.sort()
      possible_cities=((str(possible_cities))[1:-1]).replace("'",'').replace(' ','')
      
      print('Possible provinces:'+possible_cities)
    

    elif len(possible_cities)==1:
      
      possible_cities.sort()
      possible_cities=((str(possible_cities))[1:-1]).replace("'",'').replace(' ','')
      
      print('Possible province:'+possible_cities)
    
    


    else:
      
      pass
  
  else:
    while True:

      possible_cities=[]
      arrival=input('Arrival province:\n').upper()

      if departure==arrival:
        print('Enter a different province!')

      elif arrival not in provinces_dict.keys():

        print('Province not found!')

        for i in provinces_dict.keys():

          if i.startswith(arrival):

            possible_cities.append(i)


        if len(possible_cities)>1:
          possible_cities.sort()
          possible_cities=((str(possible_cities))[1:-1]).replace("'",'').replace(' ','')
          
          print('Possible provinces:'+possible_cities)

        elif len(possible_cities)==1:
          possible_cities.sort()
          possible_cities=((str(possible_cities))[1:-1]).replace("'",'').replace(' ','')
          
          print('Possible province:'+possible_cities)

        else:
          pass
          

      else:
        while True:
          travel=input('Enter travel type:\n')
          travel=travel[0].upper()+travel[1:].lower()
          if travel not in travel_types.keys():
            pass
          else:
            print('\nI am calculating the distance between '+departure+' and '+arrival+' ...\n')
            km=round(((((provinces_dict[departure][0]-provinces_dict[arrival][0])**2+(provinces_dict[departure][1]-provinces_dict[arrival][1])**2)**0.5)*100),2)
            print('Distance: '+str(km)+' km')
            hour=(km/travel_types[travel])//1
            minute=((km/travel_types[travel])%1)*60
            print('Approximate travel time with '+travel.upper()+': '+str(int(hour))+' hours '+str(int(minute))+' minutes')
            distances={}
            for i in provinces_dict:
              km=(((((provinces_dict[departure][0]-provinces_dict[i][0])**2+(provinces_dict[departure][1]-provinces_dict[i][1])**2))))**0.5
              
              distances[km]=i

            closest_city_finder=sorted(distances.keys())  
            closest_cities=distances[closest_city_finder[1]],distances[closest_city_finder[2]],distances[closest_city_finder[3]]
            closest_cities=list(closest_cities)
            closest_cities.sort()
            print('Recommended places close to '+departure+':'+(closest_cities)[0]+','+closest_cities[1]+','+closest_cities[2])







            break
        break      
    break          
                        


      


      




        



        


    

  


