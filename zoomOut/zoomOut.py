import cv2
import numpy as np
import PIL
from PIL import Image
import utils

def zoom_out(image_name, step):
    image = Image.open(image_name)
    
    width = range(0, image.size[0], step)
    height = range(0, image.size[1], step)
    
    image_data = []
    new_x = 0
    new_y = 0
    
    for x in width:
        new_y = 0
        for y in height:
            quadrants = [(x, y), (x + 1, y), (x, y + 1), (x + 1, y + 1)]
            
            int_rgb_total = 0
            for quadrant in quadrants:
                if x <= image.size[0] and y <= image.size[1]:
                    pixel = image.getpixel((x,y))
                    int_rgb_total += utils.getIfromRGB(pixel)
                else:
                    quadrants.remove(quadrant)
            new_pixel_int = round(int_rgb_total / len(quadrants))
            
            new_pixel = utils.getRGBfromI(int(new_pixel_int))
            image_data.append({
                'coordinates': (new_x, new_y),
                'pixel': new_pixel
            })
            new_y = new_y + 1
        new_x = new_x + 1
    utils.create_new_image('zoom_out.jpg', image_data)
    
zoom_out('../grama.jpg', 4)