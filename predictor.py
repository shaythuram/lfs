#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 17:45:50 2020

@author: shayyyyyy
"""



import fastbook
fastbook.setup_book()
from fastbook import *
from fastai.vision.widgets import *
import base64

learn_inf = load_learner('./Pneumonia_Predictor_first_optim.pkl')


def pred(img_fpath):
    with open(img_fpath, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    imgdata = base64.b64decode(encoded_string)
    filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)
    x = learn_inf.predict('./some_image.jpg')
    
    return print(x)


pred('./positive.jpg')
