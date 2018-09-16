import PIL
from PIL import Image

image1 = Image.open("../gow.jpg")

image_response = PIL.Image.new(image1.mode, image1.size)
width, height = image1.size

for i in range(0, width):
    for j in range(0, height):
        pixel1 = image1.getpixel((i,j))

        a = pixel1[0]
        b = pixel1[1]
        c = pixel1[2]
        d = (a + b + c) / 3

        if d > 122:
            pixel0 = 255
        else:
            pixel0 = 0

        if d > 122:
            pixel1 = 255
        else:
            pixel1 = 0

        if d > 122:
            pixel2 = 255
        else:
            pixel2 = 0

        image_response.putpixel((i,j),(pixel0 , pixel1, pixel2))
 
image_response.show()
image_response.save('limiar.jpg', 'JPEG')
