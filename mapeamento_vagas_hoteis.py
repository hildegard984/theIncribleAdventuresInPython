# -*- coding: utf-8 -*-
"""Mapeamento vagas Hoteis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YCAg-Oraync8boHw8HraAZvL2bLrM_Xx
"""

#dfNY = pd.read_csv("https://www.dropbox.com/s/8i2nw6bd5ha7vny/listingsNY.csv?dl=1")

#dfRJ = pd.read_csv("https://www.dropbox.com/s/yyg8hso7fbjf1ft/listingsRJ.csv?dl=1")

#Exercicio Parolar - Recriar o Script para o RJ

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
from matplotlib import pyplot

dfNY = pd.read_csv("https://www.dropbox.com/s/8i2nw6bd5ha7vny/listingsNY.csv?dl=1")

dfRJ = pd.read_csv("https://www.dropbox.com/s/yyg8hso7fbjf1ft/listingsRJ.csv?dl=1")

display(dfNY.head(5))
display(dfRJ.head(5))

display(dfNY.dtypes)
display(dfRJ.dtypes)

dfNY_clean = dfNY.dropna(subset=['name', 'host_name'], axis =0)#limpeza e tratamento dos dados
dfRJ_clean = dfNY.dropna(subset=['name', 'host_name'], axis =0)#limpeza e tratamento dos dados

grafico = ['price','minimum_nights']

for x in grafico:
  data_a = dfNY_clean[x]
  data_b = dfRJ_clean[x]
  data_2d = [data_a, data_b]
  plt.boxplot(data_2d, vert=False, labels=['New York','Rio de Janeiro'])
  plt.title(x)
  plt.show()

dfNY_out= dfNY_clean.copy()
dfNY_out.drop(dfNY_out[dfNY_out.price > 1100].index, axis=0, inplace=True)
dfNY_out.drop(dfNY_out[dfNY_out.minimum_nights > 4].index, axis=0, inplace=True)

dfRJ_out= dfNY_clean.copy()
dfRJ_out.drop(dfRJ_out[dfRJ_out.price > 1100].index, axis=0, inplace=True)
dfRJ_out.drop(dfRJ_out[dfRJ_out.minimum_nights > 4].index, axis=0, inplace=True)

grafico = ['price','minimum_nights']

for x in grafico:
  data_a = dfNY_out[x]
  data_b = dfRJ_out[x]
  data_2d = [data_a, data_b]
  plt.boxplot(data_2d, vert=False, labels=['New York','Rio de Janeiro'])
  plt.title(x)
  plt.show()

var = [
    'Entire home/apt',
    'Private room',
    'Shared room',
    'Hotel room',]

dado_var = {}
for i in var:
  dado_var[i] = [
      dfNY_out.loc[dfNY_out.room_type == i].shape[0]/dfNY_out.room_type.shape[0], dfRJ_out.loc[dfRJ_out.room_type == i].shape[0]/dfRJ_out.room_type.shape[0]
      ]

datacomp = pd.DataFrame(dado_var, index=['New York', 'Rio de Janeiro'])
datacomp.plot(kind= 'barh', stacked=True, figsize=(6,4), color=['c','m','y','orange'])
plt.legend(loc='lower left',bbox_to_anchor=(0.8,1.0))
plt.show()

import folium #biblioteca responsavel pelo mapa
import branca #biblioteca responsavel pelas cores

colormap = branca.colormap.linear.YlOrRd_09.scale(0, 1100) #define a escala de cores
colormap = colormap.to_step(index= [0,275,550,825,1100]) #define a escala de cores da legenda
colormap.caption = "Preço dos Imoveis"

m = folium.Map(location=[40.691895 ,-73.902734], titles = "stamentoner", zoom_start=11) #fonte de dados
#m = folium.Map(location=[-22.908333 ,-43.196388], titles = "stamentoner", zoom_start=11)

lat = [] #variavel de latitude
lon = [] #variavel de longitude
value = [] #variavel dos valor

data = {'lon':lon, 'lat':lat,'value':value}
for n in range(0,dfNY.shape[0]):
  lon.append(dfNY.longitude.values[n]) #puxa os valores de longitude
  lat.append(dfNY.latitude.values[n]) #puxa os valores de latitude
  value.append(dfNY.price.values[n]) #puxa os preços dos imoceis

for i in range(0, dfNY.shape[0]):
  preco = data['value'][i]
  if preco<= 275:
    print = '#f1f8d0'

  elif preco > 275 and preco <=550: #elif = se nao
    print = '#efc271'

  elif preco > 825 and preco <= 1100:
    print = '#efc271'

  else:
    print = '#8b2a40'

  folium.CircleMarker(
      location = [data['lat'][i],data['lon'][i]],
      radius = 2,
      color = print,
      line_color = print,
      fill_color = print,
      fill = True).add_to(m)

colormap.add_to(m)
m