import os
from flask import Flask, jsonify
from operator import itemgetter
import copy 

app = Flask(__name__)

robo_co = {
    "id":  1,
    "first_name":"Robo",
    "last_name": "Cop",
    "age":16,
    "parents":[3,4],
    "kids":[7,5]
}

san_co = {
    "id":  2,
    "first_name":"San",
    "last_name": "Cop",
    "age":18,
    "parents":[3,4],
    "kids":[]
}

ema_co = {
    "id":  3,
    "first_name":"Ema",
    "last_name": "Cop",
    "age":100,
    "parents":[],
    "kids":[1,2]
}

cho_co = {
    "id":  4,
    "first_name":"cho",
    "last_name": "Cop",
    "age":100,
    "parents":[],
    "kids":[1,2]
}

tyga_co={
    "id":  5,
    "first_name":"tyga",
    "last_name": "Cop",
    "age":1,
    "parents":[1],
    "kids":[]
}

dani_fu={
    "id":  6,
    "first_name":"dani",
    "last_name": "Fu",
    "age":16,
    "parents":[],
    "kids":[5,7]
}

valentino_co={
    "id":  7,
    "first_name":"valentino",
    "last_name": "co",
    "age":0,
    "parents":[6,1],
    "kids":[]
}

family =[robo_co,san_co,ema_co,cho_co,dani_fu,valentino_co,tyga_co]


def get_member(a):
    for member in family:
        if a ==member["id"]:
            return member
    return jsonify({"Messsage":"member not found"})
    


def get_relatives_id(member,types):
    aux =[]
    for id in member[types]:
       
        aux.append(get_member(id))
        
    member[type]=aux 
    return member
    



  
@app.route('/')
def hello():
    sorted_age=sorted(family,reverse=True, key=itemgetter('age'))
    return jsonify(sorted_age)
    
@app.route('/<int:id>')
def bye(id):
    if id > 0:
        print(family)
        for i in family:
            if id== i["id"]:
                ele=copy.deepcopy(i)
                print(ele)
                x = ele["parents"]
                aux =[]
                for i in x:
                    aux.append(i)
                ele["parents"]=aux
                
                return jsonify({"status_code":200,"data":aux})
        return jsonify({"error"})
        
            
    
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))