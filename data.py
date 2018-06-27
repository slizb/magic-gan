
import pandas as pd
import imageio
import numpy as np
from keras.preprocessing.image import load_img, img_to_array

IMG_DIR = 'img/cropped/'
SIZE = (210, 210, 3)


# def load_frame(frame):
#     x = []
#     y = []
#     for ix, row in frame.iterrows():
#         img_path = IMG_DIR + row['img_file']
#         img = imageio.imread(img_path)
#         label = row['land_type']
#         x.append(img)
#         y.append(label)
#     x = np.asarray(x)
#     y = np.asarray(y)
#     return x, y

def load_frame(frame):
    x = []
    y = []
    for ix, row in frame.iterrows():
        img_path = IMG_DIR + row['img_file']
        img = load_img(img_path, target_size=SIZE)
        img_arr = img_to_array(img)
        label = row['land_type']
        x.append(img_arr)
        y.append(label)
    x = np.asarray(x)
    y = np.asarray(y)
    return x, y


def load_data():
    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')
    x_train, y_train = load_frame(train)
    x_test, y_test = load_frame(test)
    return x_train, y_train, x_test, y_test

