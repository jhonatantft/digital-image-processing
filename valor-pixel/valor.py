from PIL import Image

image = Image.open('../grama.jpg') 

pixel = image.load()

print pixel[200,10] 
