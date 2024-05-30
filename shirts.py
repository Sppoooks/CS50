import PIL
import sys

input_image = PIL.Image.open(sys.argv[1])
cropped_image = PIL.ImageOps.fit(input_image)