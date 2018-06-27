
import pandas as pd
import os

PATH = 'img/cropped'

img_files = os.listdir(PATH)

df = pd.DataFrame(img_files, columns=['img_file'])
df['land_type'] = df['img_file'].str.split('_').apply(lambda x: x[0])

df.to_csv('df.csv', index=False)
