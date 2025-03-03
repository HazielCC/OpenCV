import os

import cv2


def read_img(name_img):
    file = set_folder_root()
    file = os.path.join(CURRENT_DIRECTORY, name_img)
    img = cv2.imread(name_img)
    return img
