# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 12:11:08 2023

@author: marin
"""

#importação dos pacotes
import pandas as pd
import numpy as np
import seaborn as sns


#Importação da base de dados
#Cria o objeto df_mobile (da classe Dataframe)
df_airline = pd.read_csv ("./datasets/Airline_Dataset_Updated_v2.csv")

#Verificação das características básicas da base de dados
df_airline.head()
df_airline.tail()
df_airline.index
df_airline.columns
df_airline.shape
df_airline.info()
df_airline.describe(include='all')
