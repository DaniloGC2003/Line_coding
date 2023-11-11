print(bytes([160, 160, 255]).decode('cp437'))

x = 'eae vei'
y = bytes([176, 160, 250]).decode('cp437')
print(y)

print(x.encode(encoding='cp437'))

print(ord('o'))
print(ord('ó'.encode('cp437')))


