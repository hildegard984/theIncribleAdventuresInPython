# -*- coding: utf-8 -*-
"""Marchine_learn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ylZvK7BfbTOjvNC_uz_FYGLGsqKxkhIq
"""

!pip install deep_daze

#https://huggingface.co/facebook/galactica-120b  modelos de ensino

from tqdm.notebook import trange #quando rodar a biblioteca no ambiente local retirar o ".notebook"
from IPython.display import Image, display #biblioteca do display
from deep_daze import Imagine #biblioteca para gerar imagens

TEXT = 'bicycle ' #@param{type:"string"}
NUM_LAYERS = 32 #@param{type:"number"}
SAVE_EVERY = 20 #@param{type:"number"}
IMAGE_WIDTH = 256 #@param{type:"number"}
SAVE_PROGRESS = True #@param{type:"boolean"}
LEARNING_RATE = 1e-5 #@param{type:"number"}
ITERATIONS = 1100 #@param{type:"number"}

model = Imagine(
    text = TEXT,
    num_layers= NUM_LAYERS,
    save_every= SAVE_EVERY,
    image_width=IMAGE_WIDTH,
    lr= LEARNING_RATE,
    save_progress=SAVE_PROGRESS,
    iterations=ITERATIONS
)

for epoch in trange(20, desc= 'epoch'):
    for i in trange(ITERATIONS, desc='iteration'):
      model.train_step(epoch,i)
      if i % model.save_every !=0:
        continue
      filename = TEXT.replace(' ','_')
      image = Image(f'./{filename}.jpg')
      #image = Image('./'+ {filename}+'.jpg')
      display(image)