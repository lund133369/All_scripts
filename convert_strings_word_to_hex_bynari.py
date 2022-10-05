import binascii

word = "comoooo estassss"
word_2byte = bytes(word, encoding='ascii')
word_hex = binascii.hexlify(word_2byte)

correct = ''.join('\\x{:02x}'.format(c) for c in word_2byte)

print("normal",word_hex)
print("correct",correct)

# output                :  b'636f6d6f6f6f****
# the output correct is :  b'\x63\x6f\x6d\x6f\x6f\x6f\x****