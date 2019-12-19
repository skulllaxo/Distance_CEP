# -*- coding: utf-8 -*-
import json
import requests 
import pandas as pd
from bs4 import BeautifulSoup as bs
from DistanceCalc import DistanceCalc as dsc



class LatlongcalcSpider():

    
    def __init__(self,cep):
        self.allowed_domains = ['app.qualp.com.br']
        self.start_urls = 'http://app.qualp.com.br/'
        self.cep = cep

    def genlink(self):
        return requests.get(self.start_urls+'geocoder/get-coords?searchtext='+self.cep).text

    
    def get_lat(self):
        lat_lng_total = json.loads(self.genlink())
        lat = lat_lng_total['lat']
        self.result = lat
        return self.result



    def get_lng(self):
        lat_lng_total = json.loads(self.genlink())
        lng= lat_lng_total['lng']
        self.result = lng
        return self.result
    
       




if __name__ == '__main__':
    dest_orig = pd.read_csv('/Users/andrebalbinodasilva/Documents/PycharmProjects/calculo_distancia_cep/Destino_Origem.csv')
    dest_orig['Distancia'] = None

    ceps_to = dest_orig['Destino'].to_list()
    ceps_from = dest_orig['Origem'].to_list()
    

    list_lat_from = []
    list_lng_from = []
    list_lat_to = []
    list_lng_to = []

    print(len(dest_orig))

    for row in range (len(dest_orig)):
        latlng_from = LatlongcalcSpider(cep=dest_orig['Origem'][row])
        latlng_to = LatlongcalcSpider(cep=dest_orig['Destino'][row])


        export_dsc = dsc(lat_from = latlng_from.get_lat(),long_from = latlng_from.get_lng(),lat_to = latlng_to.get_lat(),long_to = latlng_to.get_lng())
        dest_orig['Distancia'][row] = export_dsc.get_distance()
        print(row)
    dest_orig.to_csv('Distancia_CEP.csv')

        

                 
    