l = [1, 2, 3, 4, 5 ];
print(l)
for i in l:
    print(i)
----------------------
>>
[1, 2, 3, 4, 5]
1
2
3
4

l = [1, 2, 3, 4, 5 ];
print(l[2])
print(l[-1])
print(l[1:3])
----------------------
>> 3
>> 5
>> [2, 3]

l.append(6)
l.remove(2) #por valor
print(l)
----------------------
>> [1, 3, 4, 5, 6]


lista = [1, 2, 3, 4, 5 ];
cantidad_elementos = len(lista)
print(cantidad_elementos)
----------------------
>> 5
