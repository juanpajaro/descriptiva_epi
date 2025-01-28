#!/usr/bin/env python3
import pandas as pd
import unittest
from desviacion_punto_2 import calcular_std

class TestDesviacion(unittest.TestCase):
    def test_calculo_desviacion(self):
        data_prueba = [30, 20, 10, 40, 50]
        serie_prueba = pd.Series(data=data_prueba)
        #std = serie_prueba.std()
        #print("valor_medica: {}".format(std))
        testcase = serie_prueba
        expected = 15.8114
        self.assertAlmostEqual(calcular_std(testcase), expected, places=4)

unittest.main()