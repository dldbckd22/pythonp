import json

customer={
    'id':152322,
    'name':'강진수',
    'history':[
        {'date':'2015-04-01','item':'iPhone'},
        {'date':'2016-09-18','item':'monitor'},
        ]
}

print(type(customer))

jsonresult=json.dumps(customer)

print(type(jsonresult))

with open('D:\\ai\\pythonp\\basic\\mymod\\data.json','wt') as f:
    json.dump(customer,f,indent=4)

cu=json.loads(jsonresult)

print(cu)
print(type(cu))
cu={}
with open('D:\\ai\\pythonp\\basic\\mymod\\data.json','rt') as f:
    cu=json.load(f)

print(cu)
print(type(cu))