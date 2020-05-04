msg = "Hola mundo"
msg = 'Hola mundo'

print(msg)
print(msg[2])
print(msg[5:10])
-----------------------------
>> Hola mundo
>> l
>> mundo


b = bytearray()
b.append(0x02)
b.append(0x10)
b.append(0x05)
b.append(0x10)
b.append(0x03)
print(b)
print(b[3])
print(len(b))
-----------------------------
>> bytearray(b'\x02\x10\x05\x10\x03')
>> 16
>> 5
