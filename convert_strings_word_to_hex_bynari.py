import binascii

word = "comoooo estassss bienbenidos a mugredev"
word_2byte = bytes(word, encoding='ascii')
word_hex = binascii.hexlify(word_2byte)
print(word_hex)