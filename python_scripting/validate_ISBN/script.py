import numpy

print("PROGRAMA PARA VALIDAR ISBN")
print("PROGRAM TO VALIDATE ISBN")

x=[]
z=0
print(z)
def main():
    with open('numbers.txt') as f: #name file.
        for rec in f:
            #print(rec[:])
            k=rec[:]
            extraer(k)               

def extraer(l):
    var1=int(l[0:1])
    var2=int(l[1:2])
    var3=int(l[2:3])
    var4=int(l[3:4])
    var5=int(l[4:5])
    var6=int(l[5:6])
    var7=int(l[6:7])
    var8=int(l[7:8])
    var9=int(l[8:9])
    var10=int(l[9:10])

    #determinamos la formula
    p = (var1*10) + (var2*9)+(var3*8)+(var4*7)+(var5*6)+(var6*5)+(var7*4)+(var8*3)+(var9*2)+(var10*1)
    if p%11 == 0:
        print(l[:])
        x.append(l[:])
           
main()

x2=[m[:-1]for m in x] # delete "\n"
print("list all ISBN valid: " , x2) # print all ISBN valide , imprimir todos los ISBN validos

#extra : sum of all elements. Convertir todos los ISBN en numeros y sumarlos. 
for g in x2:
    z=z+int(g)
print("the sum of all ISBN valid is: " , z)