import googlemaps

class Maps:
    def __init__(self):
        self.gmaps = googlemaps.Client(key='AIzaSyD71mRI1zB3YORBH48S6yzNPZ91eZbZWaI')

    def getCoordenada(self,endereco):
        response = self.gmaps.geocode(endereco)
        dic = response[0]['geometry']['location']
        dic['nome'] = str(response[0]['formatted_address'])
        print(str(response[0]['formatted_address']))
        return dic

    def montaGeocode(self,cidades):
        string = ""
        for i in cidades:
            #string+=self.getCoordenada(i)['nome']+"|"
            string += i+"|"
            #string+=str(self.getCoordenada(i)['lat'])+","+str(self.getCoordenada(i)['lng'])+"|"
        return string

    def getMatrixDistance(self,origins,destinations):
        geocode_result = self.gmaps.distance_matrix(origins=origins, destinations=destinations, mode='driving')
        return self.constroiMatrixDistance(geocode_result)

    def constroiMatrixDistance(self,geocode):
        #print(len(geocode['destination_addresses']))
        distances = []
        for i in geocode['destination_addresses']:
            #print(i.split(' ', 1)[0])
            distances.append(i.split(' ', 1)[0])
        dic = {}
        for i in range(len(geocode['destination_addresses'])):
            dic[str(distances[i])] = {}
            #print(geocode['rows'][i])
            for j in range(len(geocode['destination_addresses'])):
                #print(geocode['rows'][i]['elements'][j]['distance']['value'])
                dic[str(distances[i])][str(distances[j])] = geocode['rows'][i]['elements'][j]['distance']['value']
        print(dic)
        return dic
'''
pt = Maps()

geo = pt.montaGeocode(['curvelo-mg','corinto-mg','luz-mg'])
mat = pt.getMatrixDistance(geo,geo)
'''