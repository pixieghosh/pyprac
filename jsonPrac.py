import json
import pickle 


#deserializing from json
with open('sample.json') as jsonfile:
    data = json.load(jsonfile)

#serializing to json
l1 = []
l1.append({'name': 'pix','age': 22, 'friends': ['madison', 'jen', 'zobee']})
l1.append({'name': 'dad','age': 54, 'friends': ['mom', 'pix', 'zobee']})
l1.append({'firstname': 'jen','age': 22, 'buds': ['madison', 'pix', 'zobee']})


with open('sample2.json', mode = 'w') as jsonfile:
    json.dump(l1,jsonfile)

    
with open('sample2.pkl', mode = 'wb') as jsonfile:
    pickle.dump(l1,jsonfile)
with open('sample2.pkl', mode = 'rb') as jsonfile:
    l2 = pickle.load(jsonfile)

class Person:
    def __init__(self, name, age, friends):
        self.name = name
        self.age = age
        self.friends = friends 

class PersonEncoder(json.JSONEncoder):
    def default(self, o):
        return {'name':o.name,'age':o.age,'friends':o.friends} 

#pix = Person('pix',22,['madison','jen'])
#with open('sample3.json', mode = 'w') as jsonfile:
 #   json.dump(pix,jsonfile,cls=PersonEncoder)

class PersonDecoder(json.JSONDecoder):
    def default(self, o):
        return Person(name = o['name'], age = o['age'], friends = o['friends'])

with open('sample3.json', mode = 'r') as jsonfile:
    person = json.load(jsonfile,cls=PersonDecoder)


