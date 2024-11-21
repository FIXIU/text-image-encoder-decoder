# Text-Image Encoder/Decoder

A program I've made in python as I couldn't figure out how to use the opencv library in c++ to do that.

## Table of Contents

- [Text-Image Encoder/Decoder](#text-image-encoderdecoder)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Functions](#functions)
  - [How does it work](#how-does-it-work)

## Features

- Encode text into an image
- Decode text from an image
- Simple menu interface

## Requirements

- Python 3.x
- Pillow library
- Tkinter library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/FIXIU/text-image-encoder-decoder.git
    cd random-image-encoder-decoder
    ```

2. Install the required libraries:

    ```sh
    pip install pillow
    ```

## Usage

1. Run the program.
2. Follow the menu prompts to encode or decode text.

## Functions

```py
createImage(text)
```

Encodes the given text into an image.

```py
decodeImage(image)
```

Decodes the text from the given image.

```py
createImageName(text)
```

Creates a filename for the image based on the text (e. g. "Quick example" = Quickexample.png).

```py
selectAndDecodeImage()
```

Opens a file dialog to select an image and decodes the text from it.

```py
menu()
```

Displays the menu and handles user input.

## How does it work

Each pixel represents 3 ASCII characters, each of the RGB values representing one character.
