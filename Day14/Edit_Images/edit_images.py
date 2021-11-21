from PIL import Image,ImageEnhance,ImageFilter
import glob, os, pdb

# how to change extension(pdf, png, jpg,---)

# img1 = Image.open('dog1.jpg')
# img1.save('dog1.png')
# img1.show()


# img2 = Image.open('dog2.jpg')
# img2.save('dog2.png')
# img2.show()
 
# img3 = Image.open('dog3.jpg')
# img3.save('dog3.png')
# img3.show()

# resize image

# MAX_SIZE = (250, 250)
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')

# all image's extension change 

# for item in os.listdir():   
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename, extension = os.path.splitext(item)  # extract filename
#         img1.save(f'{filename}.png')

#sharpness

# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(5).save('dog1edited_sharpness.jpg')  
# 0:blurry,1:orignal,1.5:increase sharpness

# color

# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(2).save('dog1edited_color.jpg')
# 0:black and white, 1:orignal, 1.5:increase color 

# brightness

# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.5).save('dog1edited_brightness.jpg')
# 0:black image,1:orignal,1.5:increase brightness

# contrast
# img1 = Image.open('dog1.jpg')
# enhancer = ImageEnhance.Contrast(img1)
# enhancer.enhance(1.5).save('dog1edited_contrast.jpg')
# 0:gray,1: orignal,1.5: increase contrast

# image blur

# img1 = Image.open('dog1.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius=4)).save('dog1edited_gb.png')
# by default radius = 2