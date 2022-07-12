from tkinter import Image
import easyocr
reader = easyocr.Reader(["en", 'en'], gpu=False)
import PIL
from PIL import ImageDraw

im = PIL.Image.open(r"C:\\Users\\hp\\Desktop\\5.jpeg")
im

 # OCR & Get bounding boxes.
bounds = reader.readtext(r'C:\\Users\\hp\\Desktop\\5.jpeg')
bounds

 # Draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=8):
     draw = ImageDraw.Draw(image)
     for bound in bounds:
         p0, p1, p2, p3 = bound[0]
         draw.line([*p0, *p1, *p3], fill=color, width=width)
     return Image

draw_boxes(im, bounds)

im.save(r"C:\\Users\\hp\\Desktop\\5.jpeg")

len(bounds)

for i in bounds:
    print(i[1])

f = open(r'C:\\Users\\hp\\Desktop\\5.jpeg.txt',encoding="utf-8")

for i in bounds:
    print(i[1])
    f.write(i[1])
