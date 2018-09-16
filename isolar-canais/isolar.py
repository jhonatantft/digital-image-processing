import PIL
from PIL import Image

def pixelProcRed(intensity):
    return intensity

def pixelProcBlue(intensity):
    return 0

def pixelProcGreen(intensity):
    return 0

image     = Image.open("../eye.jpg")
multiBands      = image.split()
redBand      = multiBands[0].point(pixelProcRed)
greenBand    = multiBands[1].point(pixelProcGreen)
blueBand     = multiBands[2].point(pixelProcBlue)
# redBand.show()
# greenBand.show()
# blueBand.show()

newImage = Image.merge("RGB", (redBand, greenBand, blueBand))
image_response = PIL.Image.new(image.mode, image.size)

width, height = newImage.size

for i in range(0, width):
    for j in range(0, height):
        pixel1 = newImage.getpixel((i,j))
        image_response.putpixel((i,j),(pixel1[0], pixel1[1], pixel1[2]))
 
# newImage.show()
image_response.save('isolar.jpg', 'JPEG')

