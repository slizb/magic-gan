
import pandas as pd
import os

PATH = 'img/cropped'

img_files = os.listdir(PATH)

def split_frame(df):
    train = df.sample(frac=0.8, random_state=42)
    holdout = df.drop(train.index)
    return train.reset_index(drop=True), holdout.reset_index(drop=True)


df = pd.DataFrame(img_files, columns=['img_file'])
df['land_type'] = df['img_file'].str.split('_').apply(lambda x: x[0])


train, test = split_frame(df)

train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)
