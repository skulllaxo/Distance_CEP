from DistanceCalc import DistanceCalc as dsc
from LatLongCalc import LatlongcalcSpider

class DistanceCalculator():
    def __init__(self,cep1,cep2):
        self.cep1 = cep1
        self.cep2 = cep2
    
    def calculator(self):
        latlng_from = LatlongcalcSpider(cep=self.cep1)
        latlng_to = LatlongcalcSpider(cep=self.cep2)


        calc_dsc = dsc(lat_from = latlng_from.get_lat(),long_from = latlng_from.get_lng(),lat_to = latlng_to.get_lat(),long_to = latlng_to.get_lng())
        distance =  calc_dsc.get_distance()
        return distance


distance = DistanceCalculator('04836-180','04543-000')
print(distance.calculator())
