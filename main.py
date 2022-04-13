from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

root = Tk()
filename = ""


def add_watermark():
    # Create an Image Object from an Image
    global filename

    # Opening Image
    img = Image.open(filename)

    # Creating draw object
    draw = ImageDraw.Draw(img)

    # Creating text and font object
    text = "Pu Yang.com"
    watermark_font = ImageFont.load_default()

    # Positioning Text
    textwidth, textheight = draw.textsize(text, watermark_font)
    width, height = img.size
    x = width / 2 - textwidth / 2 + 100
    y = height - textheight - 30

    # Applying text on image via draw object
    draw.text((x, y), text, font=watermark_font)

    # Saving the new image
    img.show()



def upload(event=None):
    global filename
    filename = filedialog.askopenfilename()
    label1 = Label(root, text="Your file has been upload")
    print('Selected:', filename)
    label1.pack()
    button = Button(root, text="Add watermark to this image", command=add_watermark)
    button.pack()


root.geometry("500x300")
myLabel = Label(root, text="Add Watermark To Your Image", font=("Arial", 22, "bold"))
myButton = Button(root, text="upload image", command=upload)

myLabel.pack()
myButton.pack()

root.mainloop()
