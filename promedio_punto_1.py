#!/usr/bin/env python3
import pandas as pd

def load_data(ubicacion_datos):    
    datos = pd.read_csv(ubicacion_datos, sep = '\t')
    return datos

#Retornar el promedio de la variable indice de masa corporal
#INICIO DE CODIGO
def calcular_imc(serie):
    #Modificar la linea donde dice None
    promedio_BMI = None

    return promedio_BMI
#FIN DE CODIGO