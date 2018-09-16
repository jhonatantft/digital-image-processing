from PIL import Image
from random import randint
import itertools

def get_image_pixels(image_name):
    image = Image.open(image_name)
    width_iterator = range(0, image.size[0])
    height_iterator = range(0, image.size[1])
    coordinates_list = list(itertools.product(width_iterator, height_iterator))
    pixel_list = []
    for x in width_iterator:
        for y in height_iterator:
            pixel_list.append({
                'coordinates': (x,y),
                'pixel': image.getpixel((x,y)) 
            })
    return pixel_list

def create_new_image(image_name, image_data):
    width = max(set([data.get('coordinates', (0,0))[0] for data in image_data])) + 1
    height = max(set([data.get('coordinates', (0,0))[1] for data in image_data])) + 1
    image = Image.new('RGB', (width, height))
    for pixel_data in image_data:
        image.putpixel(pixel_data.get('coordinates', (0,0)), pixel_data.get('pixel', (0,0,0)))
    image.save(image_name, 'JPEG')
    image.show()


def getRGBfromI(RGBint):
    blue =  RGBint & 255
    green = (RGBint >> 8) & 255
    red =   (RGBint >> 16) & 255
    return (red, green, blue)

def getIfromRGB(rgb):
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    RGBint = (red<<16) + (green<<8) + blue
    return RGBint