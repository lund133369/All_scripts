resultado=[]
resultado2=[]
bytes="01001000 01101111 01101100 01100001 00100000 01110000 01110010 01110101 01100101 01100010 01100001 00100000 01110100 01100101 01110011 01110100"

lista_bytes=bytes.split() #coloca en una lista cada elemento de los bytes
for x in lista_bytes :
    resultado.append(int(x,2))       #aqui se agrega codificado en ascci
    resultado2.append(chr(int(x,2))) #aqui se agrega en palabras
print(resultado)            #ASCII
print(resultado2)           #LISTA
print(''.join(resultado2))  #PALABRA