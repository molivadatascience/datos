# -*- coding: utf-8 -*-
"""
Creado por Manuel Oliva
"""
from bs4 import BeautifulSoup as bs
import requests as req

def trae_euro_franco():    
    main_url = "https://www.emol.com/economia/"
    respuesta = req.get(main_url)    
    soup = bs(respuesta.text, "html.parser")
    entradas_euro = soup.find('span', 
                         {'id': 'cuEconomia_cuDivisasCommodites_RepDivisas_ValorDivisa_0'})    
    entradas_franco = soup.find('span', 
                         {'id': 'cuEconomia_cuDivisasCommodites_RepDivisas_ValorDivisa_14'})
#    str(entradas_euro)
#    str(entradas_franco)    
    #Euro
    frase = str(entradas_euro)
    pos_1 = frase.find('>$')
    #frase[pos_1+3:]
    pos_2 = frase.find('</')
    euro = float(frase[pos_1+3:pos_2].replace(',','.'))
    #Franco
    frase = str(entradas_franco)
    pos_1 = frase.find('>$')
    frase[pos_1+3:]
    pos_2 = frase.find('</')
    franco = float(frase[pos_1+3:pos_2].replace(',','.'))    
    return ([euro,franco])
    
moneda = trae_euro_franco()    
moneda[0]    
moneda[1]