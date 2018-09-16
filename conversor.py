import PIL
from PIL import Image

# def grayscale(picture):
#     width, height = picture.size

#     for i in range(0, width):
#         for j in range(0, height):
#             pixel=picture.getpixel((i,j))
#             avg = (pixel[0] + pixel[1] + pixel[2]) / 3
#             image_response.putpixel((i,j),(avg, avg, avg))
#     #image_response.show()

# image = Image.open('gow.jpg')
# image_response = PIL.Image.new(image.mode, image.size)
# grayscale(image)
# image_response.save('grayImage.jpg', 'JPEG')


def incrementChannel(picture):
    width, height = picture.size

    for i in range(0, width):
        for j in range(0, height):
            pixel=picture.getpixel((i,j))
            image_response.putpixel((i,j),(pixel[0] + 50, pixel[1] + 50, pixel[2] + 50))
    image_response.show()

image = Image.open('gow.jpg')
image_response = PIL.Image.new(image.mode, image.size)
incrementChannel(image)
image_response.save('incrementedImage.jpg', 'JPEG')

# Zoom in

