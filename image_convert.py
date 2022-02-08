from PIL import Image, ImageOps
import glob

for filename in glob.glob('./cards/*.png'): #assuming gif
    im=Image.open(filename)
    gray_image = ImageOps.grayscale(im)
    new_title = filename.split('/')[2]
    gray_image.save('./grayscale/'+new_title)
