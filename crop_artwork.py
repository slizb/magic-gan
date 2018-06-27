import os
import random
import imageio


raw_images = os.listdir('./img')
sample_images = random.sample(raw_images, 50)

for raw_image in raw_images:
    try:
        img = imageio.imread('img/' + raw_image, format='jpg')
        crop = img[47:240, 30:-32]
        imageio.imsave('img/cropped/' + raw_image + '.jpg', crop)
    except:
        print('could not write: ', raw_image)
