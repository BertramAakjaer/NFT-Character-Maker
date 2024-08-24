import os
import random as ra
from PIL import Image
import json
import hashlib
from tqdm import tqdm


# Load used_hashes from a JSON file
def load_used_hashes(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Save used_hashes to a JSON file
def save_used_hashes(file_path, used_hashes):
    with open(file_path, 'w') as file:
        json.dump(used_hashes, file)

def load_config(config_path):
    with open(config_path, 'r') as file:
        return json.load(file)

subfolders_standard = [r"sources\background", r"sources\figure"]

config = load_config('config.json')
subfolder_procentages = config['subfolder_categories']
rarity_procentages = config['rarity_procentage']

subfolders_hats = r"sources\hats"
subfolders_eyes = r"sources\eyes"
subfolders_mouth = r"sources\mouth"
subfolders_chest = r"sources\chest"

hats_procentage = subfolder_procentages["hats_procentage"]
eyes_procentage = subfolder_procentages["eyes_procentage"]
mouth_procentage = subfolder_procentages["mouth_procentage"]
chest_procentage = subfolder_procentages["chest_procentage"]

common_procentage = rarity_procentages["common_procentage"]
uncommon_procentage = rarity_procentages["uncommon_procentage"]
rare_procentage = rarity_procentages["rare_procentage"]
epic_procentage = rarity_procentages["epic_procentage"]
legendary_procentage = rarity_procentages["legendary_procentage"]
rnjesus_procentage = rarity_procentages["rnjesus_procentage"]

dict_accesories = {
  subfolders_chest: chest_procentage,
  subfolders_mouth: mouth_procentage,
  subfolders_eyes: eyes_procentage,
  subfolders_hats: hats_procentage
}

dict_roll_random = {
  "common": common_procentage,
  "uncommon": uncommon_procentage,
  "rare": rare_procentage,
  "epic": epic_procentage,
  "legendary": legendary_procentage,
  "rnjesus": rnjesus_procentage
}

reversed_dict_roll_random = dict(reversed(list(dict_roll_random.items())))

# Initialize used_hashes
used_hashes_file = 'hash_cache.json'
used_hashes = load_used_hashes(used_hashes_file)

new_output_path = config['path']
new_output_path_active = config['is_active']

def roll_accessory_rarity():
  rarity = "none"
  for accessory, probability in reversed_dict_roll_random.items():
    if ra.uniform(0, 1) <= probability:
      rarity = accessory
      if ra.random() < 0.8:
        break
  return rarity

def roll_accessories():
  accessory_arr = [] 
  for accessory_path, probability in dict_accesories.items():
    if ra.uniform(0, 1) <= probability:
      rarity = roll_accessory_rarity()
      
      if rarity == "none":
        continue
      
      accessory_arr.append(os.path.join(accessory_path, rarity))

  return accessory_arr

def overlay_images(image_list, output_folder="output"):
  base_image = Image.open(image_list[0])
  
  for image_path in image_list[1:]:
    if "background" in image_path:
      continue
    
    overlay_image = Image.open(image_path)
    base_image.paste(overlay_image, (0, 0), overlay_image) 

  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  return base_image

def find_rarity(str):
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
    if "hats" in i and temp_str == "":
      temp_str += f"{find_rarity(i)}"
      if i != arr[-1]:
        continue
    elif temp_str == "":
      temp_str += "00"
  
    if "eyes" in i and len(temp_str) == 2:
      temp_str += f"{find_rarity(i)}"
      if i != arr[-1]:
        continue
    elif len(temp_str) == 2: 
      temp_str += "00"
      
    if "mouth" in i and len(temp_str) == 4:
      temp_str += f"{find_rarity(i)}"
      if i != arr[-1]:
        continue
    elif len(temp_str) == 4: 
      temp_str += "00"
    
    if "chest" in i and len(temp_str) == 6:
      temp_str += f"{find_rarity(i)}"
    elif len(temp_str) == 6: 
      temp_str += "00"
  
  return temp_str

def is_unique(arr):
  # Convert image_arr to a string and compute its MD5 hash
  image_arr_str = ''.join(arr)
  md5_hash = hashlib.md5(image_arr_str.encode()).hexdigest()
    
  if md5_hash not in used_hashes:
    used_hashes.append(md5_hash)
    save_used_hashes(used_hashes_file, used_hashes)
    return True
  return False

def delete_cache():
  if os.path.exists(used_hashes_file):
    os.remove(used_hashes_file)
    
  if not new_output_path_active:
    output_dir = r"output"
  else:
    output_dir = new_output_path 
    
  file_list = os.listdir(output_dir)

  for i in file_list:
    if ".gitkeep" in i:
      file_list.remove(i)

  for file_name in file_list:
    file_path = os.path.join(output_dir, file_name)
    if os.path.isfile(file_path):
      os.remove(file_path)
  
  used_hashes.clear()

def main():
  cache_clear = input("Clear cache? (Y/n) ")
  
  if not "n" in cache_clear.lower():
    delete_cache()
    
  max_images = int(input("Max images : "))
  
  out_numerate = 0
  
  duplicate_autostop = 0
  
  with tqdm(total=max_images) as pbar:
    while out_numerate <= max_images:
      
      if duplicate_autostop >= 500:
        pbar.close()
        print("Duplicate autostop reached, stopping program to save resources")
        break
      
      image_arr = []
      
      folders_to_choose_search = []
      
      for i in subfolders_standard:
        folders_to_choose_search.append(i)
        
      temp_accesories = roll_accessories()
      rarity_code = save_rarity(temp_accesories)

      if temp_accesories != []:
        for i in temp_accesories:
          folders_to_choose_search.append(i)
      
      for i in folders_to_choose_search:
        if len(os.listdir(i)) == 1:
          continue

        not_gitkeep = False
        temp_file = ""

        while not not_gitkeep:
            temp_file = ra.choice(os.listdir(i))
            if ".gitkeep" in temp_file:
              continue
            else:
              not_gitkeep = True
              break


        image_arr.append(os.path.join(i, temp_file))
      
      if is_unique(image_arr):
        image_arr_str = ''.join(image_arr)
        md5_hash = str(hashlib.md5(image_arr_str.encode()).hexdigest())
              
        result_image = overlay_images(image_arr)
        if not new_output_path_active:
          result_image.save(os.path.join("output", f"{rarity_code}_{md5_hash}.png"))
          
          message_to_user = os.path.join("output", f"rubber_{md5_hash}.png created")
        else:
          result_image.save(os.path.join(new_output_path, f"{rarity_code}_{md5_hash}.png"))
          
          message_to_user = os.path.join(new_output_path, f"rubber_{md5_hash}.png created")
        
        duplicate_autostop = 0
        out_numerate += 1
        pbar.update(1)
        
      else:
        duplicate_autostop += 1
        
        image_arr_str = ''.join(image_arr)
        md5_hash = str(hashlib.md5(image_arr_str.encode()).hexdigest())
        
        message_to_user = f"Image({md5_hash}) already exists, skips round !!"
      
      pbar.write(message_to_user)

if __name__ == "__main__":
  main()