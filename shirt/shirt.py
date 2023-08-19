import sys
from os.path import splitext
from PIL import Image,ImageOps

def main():
    check_command_line_args()
    try:
        imagefile =Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirtfile =Image.open("shirt.png")
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile,size)
    muppet.paste(shirtfile,shirtfile)
    muppet.save(sys.argv[2])
















def check_command_line_args():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])
    if check_extention(file1[1]) == False:
        sys.exit("invalid input")
    if check_extention(file2[1]) == False:
        sys.exit("Invalid output")
    if file1[1].lower() != file2[1].lower():
        sys.exit("Input and output have different extensions")

def check_extention(file):
    if file in [".jpg", ".jpeg",".png"]:
        return True
    return False

if __name__ == "__main__":
    main()