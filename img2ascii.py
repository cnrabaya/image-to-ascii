from PIL import Image

# Compresses image for high resolution images
def ResizeImage(img, new_width = 200):
    width, height = img.size
    aspect_ratio = height / width

    # Makes new height smaller to compensate for height of ASCII characters
    compensation_factor = 0.55 
    new_height = int(aspect_ratio * new_width * compensation_factor) 

    return img.resize((new_width, new_height))

def Img2ASCII(filename, isCompressed):
    # ASCII characters used:
    chars = """ .-':_,=;+!)]}0X#%$@"""

    # List is reversed so that lower index = lower brightness
    reversed_chars = chars[::-1]
    ASCII_dict = {i: ch for i, ch in enumerate(reversed_chars)}
    
    img = Image.open(filename)
    
    if isCompressed.lower() == 'y':
        new_width = int(input("Enter new width (px): "))
        img = ResizeImage(img, new_width)
    width, height = img.size

    # Output file name:
    f = open(filename + "_ascii.txt", "w")

    # Iterates through each pixel, converts RGB value to intensity and writes equivalent ASCII value
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x,y))
            r, g, b = pixel[:3]
            rel_brightness = (0.299*r + 0.587*g + 0.114*b) / 255
            ascii_index = round(rel_brightness*(len(ASCII_dict)-1))
            f.write(ASCII_dict[ascii_index])
        f.write("\n")
    f.close()
 
    print("Image converted: ", filename + "_ascii.txt")
    return

def main():
    filename = input("Enter the filename: ")
    while (not filename):
        filename = input("Enter the filename: ")
        if (filename == "exit"):
            break
    isCompressed = input("Compress Image? [Y or N]: ")  
    Img2ASCII(filename, isCompressed)

if __name__=="__main__":
    main()