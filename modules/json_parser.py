import json
import os

# Load used_hashes from a JSON file
def load_used_hashes(file_path):
    """
    Load used_hashes from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: The loaded used_hashes from the JSON file, or an empty list if the file doesn't exist.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return []

# Save used_hashes to a JSON file
def save_used_hashes(file_path, used_hashes):
    """
    Save used_hashes to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        used_hashes (list): The used_hashes to be saved.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        json.dump(used_hashes, file)

def load_config(config_path):
    """
    Load a configuration from a JSON file.

    Args:
        config_path (str): The path to the JSON file.

    Returns:
        dict: The loaded configuration from the JSON file.
    """
    with open(config_path, 'r') as file:
        return json.load(file)