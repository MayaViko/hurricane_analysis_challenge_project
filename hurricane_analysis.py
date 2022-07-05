# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

conversion = {"M": 1000000,
              "B": 1000000000}
def update_damages (damages):    
    updated_damage_list = []    
    for item in damages:        
        if "B" in item:
          item = item.strip("B")
          item = float(item)
          item =  item * conversion["B"]
          updated_damage_list.append(item)
        elif "M" in item:
          item = item.strip("M")
          item = float(item)
          item = item * conversion["M"]
          updated_damage_list.append(item)
        else:
          updated_damage_list.append(item)         
    return updated_damage_list

damages_2 = update_damages(damages)
print(damages_2)

# write your construct hurricane dictionary function here:

def new_hurricane_list(name, month, year,max_sustained_winds, area_affected, damage, death):    
  hurricane_dictionary = {}
  for i in range(0,len(name)):        
    hurricane_dictionary[i] = {
      "Name": name[i],
      "Months": month[i],
      "Year": year[i],
      "Max sustained winds": max_sustained_winds[i],
      "Areas affected": area_affected[i],
      "Damage": damage [i],
      "Death": death[i]
      }    
  return hurricane_dictionary

new_hurricane = new_hurricane_list(names,months, years, max_sustained_winds, areas_affected, damages_2, deaths)
print (new_hurricane)


# write your construct hurricane by year dictionary function here:

def new_hurricane_list_by_year(name, month,year,max_sustained_winds, area_affected, damage, death):    
  hurricane_dictionary = {}
  for i in range(0,len(year)):        
    hurricane_dictionary[i] = {
      "Name": name[i],
      "Months": month[i],
      "Year": year[i],
      "Max sustained winds": max_sustained_winds[i],
      "Areas affected": area_affected[i],
      "Damage": damage [i],
      "Death": death[i]
      }    
  return hurricane_dictionary

new_hurricane_by_year = new_hurricane_list_by_year(names,months, years, max_sustained_winds, areas_affected, damages_2, deaths)
print (new_hurricane_by_year)

# write your count affected areas function here:

def count_of_damaged_areas (area_affected):    
  damaged_areas = {}
  for area in areas_affected:
    for i in area:
      if i in damaged_areas:
        damaged_areas[i] += 1
      else:
        damaged_areas[i] = 0        
  return damaged_areas

damaged_area_count = count_of_damaged_areas(areas_affected)
print(damaged_area_count)

# write your find most affected area function here:

def area_affected_most (damaged_area_count):    
  max_area_count = 0
  max_area_name = ''    
  for area in damaged_area_count:
    if damaged_area_count[area] > max_area_count:
      max_area_count = damaged_area_count[area]
      max_area_name = area
  return max_area_count, max_area_name

most_frequently_affected_area = area_affected_most (damaged_area_count)
print(most_frequently_affected_area)

# write your greatest number of deaths function here:

def deadliest_hurricane (new_hurricane):    
  number_of_deathes = 0
  hurricane_name = ''    
  for hurricane in new_hurricane:
    if new_hurricane [hurricane]["Death"] > number_of_deathes:
      number_of_deathes = new_hurricane[hurricane]["Death"]
      hurricane_name = new_hurricane[hurricane]["Name"]
  return hurricane_name, number_of_deathes

# find highest mortality hurricane and the number of deaths

deadly_hurricane = deadliest_hurricane(new_hurricane)
print(deadly_hurricane)

# write your catgeorize by mortality function here:

def mortality_rating (new_hurricane):
  mortality_rating_list = {0:[], 1: [], 2: [], 3: [], 4:[]}    
  for hurricane in new_hurricane:    
    death_rate = 0
    death = new_hurricane[hurricane]["Death"]
    if death == 0:
      death_rate = 0
    elif death <= 100:
      death_rate = 1
    elif death <= 500:
      death_rate = 2
    elif death <= 1000:
      death_rate = 3
    else:
      death_rate = 4  
    if death_rate not in mortality_rating_list:
      mortality_rating_list[death_rate] = new_hurricane[hurricane]
    else:
      mortality_rating_list[death_rate].append(new_hurricane[hurricane])  
  return mortality_rating_list

mortality_rate = mortality_rating (new_hurricane)
print(mortality_rate) 

# write your greatest damage function here:

def most_damage_hurricane (new_hurricane):    
  most_damage = 0
  hurricane_name = ''    
  for hurricane in new_hurricane:
    if new_hurricane [hurricane]["Damage"] == "Damages not recorded":
      continue 
    if new_hurricane [hurricane]["Damage"] > most_damage:
      most_damage = new_hurricane[hurricane]["Damage"]
      hurricane_name = new_hurricane[hurricane]["Name"]
  return hurricane_name, most_damage

# find highest damage inducing hurricane and its total cost

damage_hurricane = most_damage_hurricane(new_hurricane)
print(damage_hurricane)

# write your catgeorize by damage function here:

# Rating Hurricanes by Damage

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def damages_rating (new_hurricane):
  damages_rating_list = {0:[], 1: [], 2: [], 3: [], 4:[]}    
  for hurricane in new_hurricane:    
    damage_rate = 0
    damage = new_hurricane[hurricane]["Damage"]   
    if damage == 'Damages not recorded':
      continue
    elif damage == damage_scale[0]:
      damage_rate = 0
    elif damage <= damage_scale[1]:
      damage_rate = 1
    elif damage <= damage_scale[2]:
      damage_rate = 2
    elif damage <= damage_scale[3]:
      damage_rate = 3
    else:
      damage_rate = 4  
    if damage_rate not in damages_rating_list:
      damages_rating_list[damage_rate] = new_hurricane[hurricane]
    else:
      damages_rating_list[damage_rate].append(new_hurricane[hurricane])  
  return damages_rating_list

damage_rate = damages_rating (new_hurricane)
print(damage_rate) 
