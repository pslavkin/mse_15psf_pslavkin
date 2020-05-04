l = (1, 2, 3, 4, 5);
print(l[2])
print(l[-1])
print(l[1:3])
l.append(6) #ERROR no hay append
l.remove(2) #ERROR no hay remove
--------------------------------
>> 3
>> 5
>> (2, 3)


d = {"color":"red","state":True,"id":27}
print(d)
print(d["state"])
d["key"]="value"
print(d)
--------------------------------
>> {'state': True, 'color': 'red', 'id': 27}
>> True
>> {'state': True, 'color': 'red', 'key': 'value', 'id': 27}
