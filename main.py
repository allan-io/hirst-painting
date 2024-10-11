import colorgram
from PIL import Image

img = Image.open("hirst.jpg")

color_palate = colorgram.extract(img, 10)

color_list = []
for color in color_palate:
    color_tuple = (color.rgb[0], color.rgb[1], color.rgb[2])
    color_list.append(color_tuple)

print(color_list)