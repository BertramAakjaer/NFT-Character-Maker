# NFT-Character-Maker

NFT-Character-Maker is a Python CLI tool designed to generate a collection of unique and custom characters, similar to the well-known Bored Apes. This tool allows you to create characters with various accessories and rarity levels, making each character distinct. It can also be used to add borders around the characthers showing the highest rarity.

## Features

- **Customizable Accessories**: Generate characters with different accessories such as hats, eyes, mouths, and chests.
- **Rarity Levels**: Assign rarity levels to accessories to create a diverse collection of characters.
- **Image Overlay**: Combine multiple images to create the final character.
- **Cache Management**: Clear cache to avoid duplicate characters.
- **Border Application**: Optionally add borders to the generated characters.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/NFT-Character-Maker.git
    cd NFT-Character-Maker
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

Edit the `config.json` file to customize the tool's behavior:

```json
{
    "subfolder_categories": {
        "hats_procentage": 0.5,
        "eyes_procentage": 0.5,
        "mouth_procentage": 0.4,
        "chest_procentage": 0.2
    },
    "rarity_procentage": {
        "common_procentage": 0.5,
        "uncommon_procentage": 0.3,
        "rare_procentage": 0.2,
        "epic_procentage": 0.1,
        "legendary_procentage": 0.01,
        "rnjesus_procentage": 0.001
    },
    "path": "",
    "is_active": false,
    "border_offset": [37, 15]
}
```
## Usage

Run the tool in CLI mode:

```bash
python3 nft_maker.py
```

You will be prompted to clear the cache, add borders, and specify the maximum number of images to generate.

### Command-Line Arguments

- `-c`: Clear the cache.
- `-i {number}`: Number of characters to generate.
- `-b`: Add borders to the generated characters.

Example:

```bash
python nft_maker.py -c -i 50 -b
```

## License

This project is licensed under the MIT License. See the [`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FC%3A%2FUsers%2Fbertr%2FOneDrive%2FNFT%20Project%2FNFT-Character-Maker%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Users\bertr\OneDrive\NFT Project\NFT-Character-Maker\LICENSE") file for details.


## Acknowledgements

- [Pillow](https://python-pillow.org/) for image processing.
- [tqdm](https://tqdm.github.io/) for progress bars.
- [rand](https://docs.rs/rand/latest/rand/) for random number generation.