def pangkat_tiga (x): 
    c = x*x*x
    return(c)

x = float(input("nilai x adalah "))
c = x*x*x
print(f"{c}")

# fungsi max

def Max2 (A, B): 
    A = int
    B = int
    return (A, B)
    
A = int(input("A adalah "))
B = int(input("B adalah "))
    
if (A >= B): 
        max = A
else: 
        max = B
    
print (f"max adalah {max}")

def CetakNama (nama): 
    print ("Hello, " + nama + "!")
    return

nama = str(input("Masukkan nama: "))
N = int(input("berapa kali diiulang: "))

for i in range(N):
    print (f"hello {nama} !")
    
from math import * 

N = float(input("masukkan bilangan = "))
print ("akar dari {N} = str(sqrt(N))")