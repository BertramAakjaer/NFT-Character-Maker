# **NFT-Character-Maker**

> [!NOTE]
>  If you're using any other OS than windows this will not work, because it is depending on the python libary **os** which is made for windows only, [see this doc for more info :)](https://docs.python.org/3/library/os.html)

NFT-Character-Maker is a Python CLI tool designed to generate a collection of unique and custom characters, likewise to the known Bored Apes. This tool is made to create fun characthers for `non-comercial use`, and shall just be used for fun. The tool allows you to create characters with various accessories and rarity levels, making each character distinct. It can also be used to add borders around the characthers showing the highest rarity. This feature is made to make things like trading cards.

## Features

- **Customizable Accessories**: Generate characters with different accessories which is currently hats, eyes, mouths, and chests. Which can be given a specific rarity and will be applied such as.
- **Rarity Levels**: Assign rarity levels to accessories to create a diverse collection of characters.
- **Cache Management**: Save to cache to avoid duplicate characters and clear the cache with a .bat file.
- **Border Application**: Optionally add borders to the generated characters.
- **Automatic Stopping**: The program will stop by itself if the number of pictures the user wants to create cant be realized.
- **Modularity**: Different ways to run the program (More under usage)

## Quickinfo about the program
A code for generated images is used. The code is 8 degits and could look like the following:

- `00000000`
- `un00co00`
- `unlera00`

The concept is very simple we have different rairty types and each type has its own code:

| Rarity type     | Code          |
|---------------- |---------------|
|     None        |    `00`       |
|     Common      |     `co`      |
|     Uncommon    |      `un`     |
|     Rare        |       `ra`    |
|     Legenday    |     `le`      |
|     RNGesus     |     `rn`      |

The code is applied in the following order:

1. **Hats**
2. **Eyes**
3. **Mouth**
4. **Chest** 

So this code `un00co00`implies the following:

1. The **hat** is `Uncommon`
2. The **eyes** are `None`
3. The **mouth** is `Common`
4. The **Chest** is `None`

## Setup
> [!IMPORTANT]
> [Git](https://git-scm.com/downloads) is needed to clone this repository, else you can just download the files as a `.zip`

1. Clone the repository:
    ```bash
    $ git clone https://github.com/yourusername/NFT-Character-Maker.git
    $ cd NFT-Character-Maker
    ```

2. Install the required dependencies:
    ```bash
    $ pip install -r requirements.txt
    ```

## Configuration

The `config.json` file is used to modify the procent

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
- **Subfolder_categories**: For choosing the chance of getting a cosmetic applied.
- **Rarity_procentage**: Choosing the chance for getting a specific rarity of a cosmetic.
- **Border_offset**: The offset for the pictures in the border so they can be alligned with a hole in the template.

If the `is_active` is set to `true`, then the path variable will be used as the output path.

## Usage
The tool can be run by using three different modes

### Run the tool in CLI mode

```bash
$ python3 nft_maker.py
```

You will be prompted to clear the cache, add borders, and specify the maximum number of images to generate. With the proper debugging feedback.

### Run with command-line flags (arguments)

- `-c`: Clear the cache.
- `-i {number}`: Number of characters to generate.
- `-b`: Add borders to the generated characters.

Example:

```bash
$ python3 nft_maker.py -c -i 50 -b
```

### Run with .bat files
Double click on of the following `.bat` files in the root of the directory
- `clear_cache.bat`: Clear the cache and output folder.
- `make_100_files.bat`: Generate 100 files and create borders.
- `make_500_files.bat`: Generate 500 files and create borders.
- `make_1000_files.bat`: Generate 1000 files and create borders.

## Example input/output
Will be added later :)

## Libaries used

- [Pillow](https://python-pillow.org/) for image processing.
- [tqdm](https://tqdm.github.io/) for progress bars.
- [Random](https://docs.python.org/3/library/random.html) for random number generation.


## License

This project is licensed under the [`MIT Licence`](LICENSE)



##  **Socials**
>  [aakjaer.site](https://www.aakjaer.site) &nbsp;&middot;&nbsp;
>  GitHub [@BertramAakjær](https://github.com/BertramAakjaer) &nbsp;&middot;&nbsp;
>  Twitter [@BertramAakjær](https://twitter.com/BertramAakjaer)