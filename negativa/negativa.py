import PIL
from PIL import Image

img = Image.open("../gow.jpg") 
image_response = PIL.Image.new(img.mode, img.size)

width, height = img.size

for i in range(0, width):
    for j in range(0, height):
        pixel = img.getpixel((i,j))
        image_response.putpixel((i,j),(abs(pixel[0] - 255), abs(pixel[1] - 255), abs(pixel[2] - 255)))

image_response.show()
image_response.save('negative.jpg', 'JPEG')
