from PIL import Image
from random import randint
import tkinter as tk
from tkinter import filedialog

def createImage(text):
    if len(text) % 3 != 0:
        width = round(len(text) / 3) + 1
    else:
        width = round(len(text) / 3)
    currentLetter = 0
    userImage = Image.new('RGB', (width, 1))
    for x in range(width):
        if currentLetter + 2 < len(text):
            r = ord(text[currentLetter])
            g = ord(text[currentLetter + 1])
            b = ord(text[currentLetter + 2])
        elif currentLetter + 1 < len(text):
            r = ord(text[currentLetter])
            g = ord(text[currentLetter + 1])
            b = 0
        elif currentLetter < len(text):
            r = ord(text[currentLetter])
            g = 0
            b = 0
        else:
            r = 0
            g = 0
            b = 0
        userImage.putpixel((x, 0), value = (r, g, b))
        currentLetter += 3

    return userImage

def decodeImage(image):
    text = ""
    for x in range(image.width):
        r, g, b = image.getpixel((x, 0))
        text += chr(r) + chr(g) + chr(b)

    return text

def createImageName(text):
    text = text.replace(" ", "")
            
    return text

def selectAndDecodeImage():
    root = tk.Tk()
    root.withdraw() # hides the window
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        image = Image.open(file_path)
        if image.mode != "RGB":
            print("The image must be in RGB mode")
            return
        if image.height != 1:
            print("The image must have a height of 1 pixel")
            return
        decoded_text = decodeImage(image)
        print(f"Decoded text: {decoded_text}")

def menu():
    print("1. Encode text")
    print("2. Decode image")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        text = input("Enter the text to encode: ")
        userImage = createImage(text)
        print(f"Encoded text: {text}, showing image...")
        userImage.show()
        print(f"Saving image {createImageName(text) + ".png"}...")
        userImage.save(createImageName(text) + ".png")
    elif choice == "2":
        selectAndDecodeImage()
    elif choice == "3":
        return
    else:
        print("Invalid choice")
    menu()

menu()