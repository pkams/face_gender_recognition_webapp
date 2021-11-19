import pandas as pd
import glob
from tqdm import tqdm
import cv2
import numpy as np
import os

def open_image(path):
    im = cv2.imread(path)
    size = im.size
    return im, size

def image_preprocess(im, shape):
    resized = cv2.resize(im, shape, cv2.INTER_CUBIC)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    flatten = gray.flatten()
    return flatten


if __name__ == '__main__':
    files_path = glob.glob('data/cropped/**/*.jpg', recursive=True)
    shape = (100,100)
    image_list = []
    gender_list = []
    for path in tqdm(files_path):
        im, size = open_image(path)
        if size > 100:
            image = image_preprocess(im, shape)
            image_list.append(image)
            gender_list.append(os.path.basename(os.path.dirname(path)))
        else:
            continue
    df = pd.DataFrame(np.array(image_list))
    df['gender'] = gender_list
    df.to_csv('data/dataframe_100x100.csv', index=None)