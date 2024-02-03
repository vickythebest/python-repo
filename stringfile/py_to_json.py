# python to json
# json to python
# can convert all datatypes
# making json readable(indentation, separator)
# list,tuples,set,dictionary



rd = {
    "name":"vivek",
    "age":43,
    "place":"india"
}

print(type(rd))
print(rd["name"])

import json
# converting python to json
pytojson=json.dumps(rd)

print(pytojson)
print(type(pytojson))
# print(pytojson["age"])

# convertingjson to pythhon code (loading)
jsontopy=json.loads(pytojson)
print(jsontopy)
print(type(jsontopy))

# organizing the data
pytonjson=json.dumps(rd,indent=4,sort_keys=True)
print(pytonjson)
