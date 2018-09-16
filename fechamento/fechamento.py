import utils
import PIL
from PIL import Image

def convolution(image_name, kernel, new_image):
    image = Image.open(image_name)

    width = range(0, image.size[0])
    height = range(0, image.size[1])
    
    image_data = []
    
    offset_x = (kernel.get('width', 0) - 1) / 2
    offset_y = (kernel.get('height', 0) - 1) / 2
    
    for x in width:
        for y in height:
            conv_r = 0
            conv_g = 0
            conv_b = 0
            
            for kx in range(0, kernel.get('width', 0)):
                x_coord = x + kx - offset_x
                if x + kx < offset_x or x_coord >= image.size[0]:
                    continue
                for ky in range(0, kernel.get('height', 0)):
                    y_coord = y + ky - offset_y
                    if y + ky < offset_y or y_coord >= image.size[1]:
                        continue
                    kernel_pixel = kernel.get('matrix', [])[kx][ky]
                    image_pixel = image.getpixel((x_coord, y_coord))
                    
                    conv_r += (image_pixel[0] * kernel_pixel)
                    conv_g += (image_pixel[1] * kernel_pixel)
                    conv_b += (image_pixel[2] * kernel_pixel)
                
            if conv_r > 255:
                conv_r = 255
            if conv_r < 0:
                conv_r = 0
            if conv_g > 255:
                conv_g = 255
            if conv_g < 0:
                conv_g = 0
            if conv_b > 255:
                conv_b = 255
            if conv_b < 0:
                conv_b = 0
                
            image_data.append({
                'coordinates': (x, y),
                'pixel': (conv_r, conv_g, conv_b)
            })
            
    utils.create_new_image('{}.jpg'.format(new_image), image_data)

erode_kernel = {
    'width': 3,
    'height': 3,
    'matrix': [[1,0,1],[0,0,0],[1,0,1]]
}

dilate_kernel = {
    'width': 3,
    'height': 3,
    'matrix': [[0,1,0],[1,1,1],[0,1,0]]
}
convolution('../ab.jpg', dilate_kernel, 'closing_first_phase')
convolution('closing_first_phase.jpg', erode_kernel, 'closing')