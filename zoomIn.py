import PIL
from PIL import Image

def zoomIn(picture):
    width, height = picture.size

    for i in range(0, width):
        for j in range (0, height):
            pixel = picture.getpixel(( i, j))
            newImage(picture, pixel)



def newImage(picture, pixel):
    width, height = picture.size

    croped = picture.crop(width - i, width - i, height - j, height - j)
    for i in range(0, width):
        for j in range(0, height):

    # #image_response.show()

image = Image.open('gow.jpg')
image_response = PIL.Image.new(image.mode, image.size)
zoomIn(image)
image_response.save('zoomedIn.jpg', 'JPEG')