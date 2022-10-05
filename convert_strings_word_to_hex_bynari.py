import binascii

word = "comoooo estassss bienbenidos a mugredev"
word_2byte = bytes(word, encoding='ascii')
word_hex = binascii.hexlify(word_2byte)
print(word_hex)

# output                :  b'636f6d6f6f6f****
# the output correct is :  b'\x63\x6f\x6d\x6f\x6f\x6f\x****