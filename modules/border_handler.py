from PIL import Image
from tqdm import tqdm
import os

def apply_borders(output_path, offset, show_cli=False):
    # Directory containing the border images
    borders_dir = r"sources\borders"

    # Get the total number of files in the output path directory
    total_files = len(os.listdir(output_path))

    # Create a progress bar to track the border application process
    with tqdm(total=total_files, disable=False) as pbar:
        # Iterate over each file in the output path directory
        for filename in os.listdir(output_path):
            # Check if the file is a PNG image
            if filename.endswith(".png"):
                # Determine the border image based on the filename prefix
                border_card_str = ""

                if "rn" in filename[0:8]:
                    border_card_str = "rnjesus.png"
                
                elif "le" in filename[0:8]:
                    border_card_str = "legendary.png"
                
                elif "ep" in filename[0:8]:
                    border_card_str = "epic.png"
                
                elif "ra" in filename[0:8]:
                    border_card_str = "rare.png"
                
                elif "un" in filename[0:8]:
                    border_card_str = "uncommon.png"
                
                elif "co" in filename[0:8]:
                    border_card_str = "common.png"

                else:
                    border_card_str = "none.png"
                
                # Open the border image and the image to be pasted
                border_image = Image.open(os.path.join(borders_dir, border_card_str)).convert("RGBA")
                img_to_paste = Image.open(os.path.join(output_path, filename)).convert("RGBA")

                # Paste the image onto the border image at the specified offset
                border_image.paste(img_to_paste, (offset[0], offset[1]))

                # Open the border image again to avoid overwriting the original
                border_image2 = Image.open(os.path.join(borders_dir, border_card_str)).convert("RGBA")

                # Paste the border image onto itself to create a border effect
                border_image.paste(border_image2, (0, 0), border_image2)

                # Save the final image with the applied border
                border_image.save(os.path.join(output_path, filename), "PNG")
                
                # Update the progress bar and display a message if show_cli is True
                pbar.update(1)
                if show_cli:
                    pbar.message(f"Border with {border_card_str} applied to {filename} at {output_path}")