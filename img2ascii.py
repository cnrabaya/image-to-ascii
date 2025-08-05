from PIL import Image
import os

def img2ascii(filename):
    img = Image.open(filename)
    width, height = img.size
    f = open(filename + "_ascii.txt", "w")

    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x,y))
            r, g, b = pixel[:3]
            rel_brightness = (0.299*r + 0.587*g + 0.114*b) / 255
            
            if (rel_brightness > 0.9):
                f.write(" ")
            elif (rel_brightness > 0.8 and rel_brightness <= 0.9):
                f.write(".")
            elif (rel_brightness > 0.7 and rel_brightness <= 0.8):
                f.write("'")
            elif (rel_brightness > 0.6 and rel_brightness <= 0.7):
                f.write("-")
            elif (rel_brightness > 0.5 and rel_brightness <= 0.6):
                f.write("-")
            elif (rel_brightness > 0.4 and rel_brightness <= 0.5):
                f.write("+")
            elif (rel_brightness > 0.3 and rel_brightness <= 0.4):
                f.write("*")
            elif (rel_brightness > 0.2 and rel_brightness <= 0.3):
                f.write("%")
            elif (rel_brightness > 0.1 and rel_brightness <= 0.2):
                f.write("$")
            else:
                f.write("#")
            
        f.write("\n")
    
    f.close()
    return

def main():
    filename = input("Enter the filename: ")
    while (not filename):
        filename = input("Enter the filename: ")
        if (filename == "exit"):
            break
        
    img2ascii(filename)

if __name__=="__main__":
    main()