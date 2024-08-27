import random as ra
import os

def roll_accessory_rarity(dict_rarities):
  rarity = "none"
  for accessory, probability in dict_rarities.items():
    if ra.uniform(0, 1) <= probability:
      rarity = accessory
      if ra.random() < 0.8:
        break
  return rarity

def roll_accessories(dict_accesories, dict_rarities):
  accessory_arr = [] 
  for accessory_path, probability in dict_accesories.items():
    if ra.uniform(0, 1) <= probability:
      rarity = roll_accessory_rarity(dict_rarities)
      
      if rarity == "none":
        continue
      
      accessory_arr.append(os.path.join(accessory_path, rarity))

  return accessory_arr

def find_rarity(str):
  # Determine the rarity based on the string
  if "uncommon" in str:
    return "un"
  if r"common" in str:
    return "co"
  if "rare" in str:
    return "ra"
  if "epic" in str:
    return "ep"
  if "legendary" in str:
    return "le"
  if "rnjesus" in str:
    return "rn"

def save_rarity(arr):
  if arr == []:
    return "00000000"
  
  temp_str = ""
  
  for i in arr:
    if "chest" in i and temp_str == "":
      temp_str += f"{find_rarity(i)}"
      if i != arr[-1]:
        continue
    elif temp_str == "":
      temp_str += "00"
  
    if "mouth" in i and len(temp_str) == 2:
      temp_str += f"{find_rarity(i)}"
      if i != arr[-1]:
        continue
    elif len(temp_str) == 2: 
      temp_str += "00"
      
    if "eyes" in i and len(temp_str) == 4:
      temp_str += f"{find_rarity(i)}"
      if i != arr[-1]:
        continue
    elif len(temp_str) == 4: 
      temp_str += "00"
    
    if "hats" in i and len(temp_str) == 6:
      temp_str += f"{find_rarity(i)}"
    elif len(temp_str) == 6: 
      temp_str += "00"

  # Rearrange the string to match the desired format
  temp_str = temp_str[6:8] + temp_str[4:6] + temp_str[2:4] + temp_str[0:2]

  return temp_str
