table_data = [
    ['aaaaaa', 'b', 'cccc'],
    ['aaaaaaaaaa', 'b', 'c'], 
    ['aaa', 'bbbbbbbbbb', 'cccc']
]
for row in table_data:
    print("{: >20} {: >20} {: >20}".format(*row))