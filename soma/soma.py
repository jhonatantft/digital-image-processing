import PIL
from PIL import Image

image1 = Image.open("gow.jpg")
image2 = Image.open("eye.jpg")

squared_image = ( 0, 0, 600, 350)
cropped_image1 = image1.crop(squared_image)
cropped_image2 = image2.crop(squared_image)

image_response = PIL.Image.new(cropped_image1.mode, cropped_image1.size)
width, height = cropped_image1.size

for i in range(0, width):
    for j in range(0, height):
        pixel1 = cropped_image1.getpixel((i,j))
        pixel2 = cropped_image2.getpixel((i,j))
        image_response.putpixel((i,j),((pixel1[0] + pixel2[0]), (pixel1[1] + pixel2[1]), (pixel1[2] + pixel2[2])))
 
# image_response.show()
image_response.save('soma.jpg', 'JPEG')
