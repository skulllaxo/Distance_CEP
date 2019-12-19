# -*- coding: utf-8 -*-
import requests
import json

class DistanceCalc():
    
    allowed_domains = ['osrm.qualp.com.br']
    start_urls = ['http://osrm.qualp.com.br/']

    def __init__(self,lat_from,long_from,lat_to,long_to):

        self.lat_from = str(lat_from)
        self.long_from = str(long_from)
        self.lat_to = str(lat_to)
        self.long_to = str(long_to)

        
        
    def gen_link(self):
        return requests.get('http://osrm.qualp.com.br/route/v1/driving/'+self.long_from+","+self.lat_from+";"+self.long_to+","+self.lat_to+'?overview=full&alternatives=false&steps=true').text
        

    def get_distance(self):
        total_request = json.loads(self.gen_link())
        #print(total_request)
        try:
            self.distance = float(total_request['routes'][0]['legs'][0]['distance'])
        except:
            self.distance = 'ERROR'
        return self.distance
