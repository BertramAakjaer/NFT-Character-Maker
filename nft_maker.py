import os, hashlib, argparse
import random as ra
from PIL import Image
from tqdm import tqdm
from modules.json_parser import *
from modules.border_handler import apply_borders
from modules.rarity_accesories import *

# Handle flags
parser = argparse.ArgumentParser(description="Script for making NFTs")
parser.add_argument('-c', '--cacheClear', action='store_true', help="Clear output cache")
parser.add_argument('-i', '--iterations', type=int, help="An integer number for output iterations")
parser.add_argument('-b', '--borders', action="store_true", help="Add borders")

# Define subfolders for standard categories
subfolders_standard = [r"sources\background", r"sources\figure"]

# Load configuration from JSON file
config = load_config('config.json')
subfolder_procentages = config['subfolder_categories']
rarity_procentages = config['rarity_procentage']

# Set output path based on configuration
if config['is_active'] == True:
  output_path = config['path']
else: 
  output_path = r"output"

# Define subfolders for specific accessory categories
subfolders_hats = r"sources\hats"
subfolders_eyes = r"sources\eyes"
subfolders_mouth = r"sources\mouth"
subfolders_chest = r"sources\chest"

# Get percentages for each accessory category
hats_procentage = subfolder_procentages["hats_procentage"]
eyes_procentage = subfolder_procentages["eyes_procentage"]
mouth_procentage = subfolder_procentages["mouth_procentage"]
chest_procentage = subfolder_procentages["chest_procentage"]

# Get percentages for each rarity level
common_procentage = rarity_procentages["common_procentage"]
uncommon_procentage = rarity_procentages["uncommon_procentage"]
rare_procentage = rarity_procentages["rare_procentage"]
epic_procentage = rarity_procentages["epic_procentage"]
legendary_procentage = rarity_procentages["legendary_procentage"]
rnjesus_procentage = rarity_procentages["rnjesus_procentage"]

# Create a dictionary to map accessory categories to their percentages
dict_accesories = {
  subfolders_chest: chest_procentage,
  subfolders_mouth: mouth_procentage,
  subfolders_eyes: eyes_procentage,
  subfolders_hats: hats_procentage
}

# Create a dictionary to map rarity levels to their percentages
dict_roll_random = {
  "common": common_procentage,
  "uncommon": uncommon_procentage,
  "rare": rare_procentage,
  "epic": epic_procentage,
  "legendary": legendary_procentage,
  "rnjesus": rnjesus_procentage
}

# Reverse the dictionary to prioritize the most rare items
reversed_dict_roll_random = dict(reversed(list(dict_roll_random.items())))

# Initialize used_hashes
used_hashes_file = 'hash_cache.json'
used_hashes = load_used_hashes(used_hashes_file)

# Function to overlay multiple images
def overlay_images(image_list):
  base_image = Image.open(image_list[0])
  
  for image_path in image_list[1:]:
    if "background" in image_path:
      continue
    
    overlay_image = Image.open(image_path)
    base_image.paste(overlay_image, (0, 0), overlay_image) 

  if not os.path.exists(output_path):
    os.makedirs(output_path)

  return base_image

# Function to check if an image combination is unique
def is_unique(arr):
  # Convert image_arr to a string and compute its MD5 hash
  image_arr_str = ''.join(arr)
  md5_hash = hashlib.md5(image_arr_str.encode()).hexdigest()
    
  if md5_hash not in used_hashes:
    used_hashes.append(md5_hash)
    save_used_hashes(used_hashes_file, used_hashes)
    return True
  return False

# Function to clear the cache
def clear_cache():
  if os.path.exists(used_hashes_file):
    os.remove(used_hashes_file)
    
  file_list = os.listdir(output_path)

  for i in file_list:
    if ".gitkeep" in i:
      file_list.remove(i)

  for file_name in file_list:
    file_path = os.path.join(output_path, file_name)
    if os.path.isfile(file_path):
      os.remove(file_path)
  
  used_hashes.clear()

# Function to combine accessories and create NFTs
def combine_accesories(max_images, show_cli=False):
  out_numerate = 0
  duplicate_autostop = 0

  with tqdm(total=max_images, disable=False) as pbar:
    while out_numerate <= max_images - 1:
      
      if duplicate_autostop >= 500:
        pbar.close()
        if show_cli:
          print("Duplicate autostop reached, stopping program to save resources")
        break
      
      image_arr = []
      folders_to_choose_search = []

      for i in subfolders_standard:
        folders_to_choose_search.append(i)
        
      temp_accesories = roll_accessories(dict_accesories, reversed_dict_roll_random)
      rarity_code = save_rarity(temp_accesories)

      if temp_accesories != []:
        for i in temp_accesories:
          folders_to_choose_search.append(i)
      
      for i in folders_to_choose_search:
        if len(os.listdir(i)) == 1 and ".gitkeep" in os.listdir(i)[0]:
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
        result_image.save(os.path.join(output_path, f"{rarity_code}_{md5_hash}.png"))
        
        if show_cli:
          pbar.write(os.path.join(output_path, f"rubber_{md5_hash}.png created"))

        duplicate_autostop = 0
        out_numerate += 1
        pbar.update(1)
        
      else:
        duplicate_autostop += 1
        
        if show_cli:
          image_arr_str = ''.join(image_arr)
          md5_hash = str(hashlib.md5(image_arr_str.encode()).hexdigest())
          
          pbar.write(f"Image({md5_hash}) already exists, skips round !!")
  pbar.close()

# Function to run the script in command-line interface mode
def main_cli():
  cache_clear = input("Clear cache? (Y/n) ")
  
  if not "n" in cache_clear.lower():
    clear_cache()

  add_border = input("Add border? (Y/n) ")
    
  max_images = int(input("Max images : "))

  combine_accesories(max_images, True)

  if not "n" in add_border.lower():
    apply_borders(output_path, config['border_offset'], True)

# Entry point of the script
if __name__ == "__main__":
  args = parser.parse_args()

  if not any(vars(args).values()):
    main_cli()
  else:
      if args.cacheClear:
        clear_cache()
      if args.iterations:
        combine_accesories(args.iterations)
      if args.borders:
        apply_borders(output_path, config['border_offset'])
