import numpy as np

import time


### Bir Cubugun Doğrultu Kosinüs Vektörlerini Bulupyoruz

import duzlem_kafes_kod_numarası


"""
    
Sistem Türleri : 

1: Düzlem Kafes 
2: Düzlem Çerçeve 



    
    
    
    
"""

while True:

    input_value = input("Sistem Türünü Seçiniz Geometriyi Bitirmek için q ya basınız")

    if input_value == "1":

        import duzlem_kafes_kod_numarası
        system_coordinate = list()
        cubuk_numarası = 1
        while True :

            coord = input("Cubuk Koordinat Değerlerini Giriniz,Bitirmek İçin q ya basınız ")

            if coord == "q":

                break



            coord = [float(i) for i in coord]
            system_coordinate.append(coord)


    if input_value == "q":

        print("Sistem bitti "
             )
        break





koordinatlar4 = [[0,0,0,4],[0,4,4,4],[4,0,4,4],[0,0,4,0],[4,0,0,4],[0,0,4,4]]


A=6
E = 3




cubuk_dogrultu_kosinüs = list()

T = np.zeros((4,4))

koordinatlar = duzlem_kafes_kod_numarası.kod_numarası_düzlem_kafes(koordinatlar4)

koordinat_verileri = list(koordinatlar.values()) ## Fonksiyondan elde ettiğimiz yeni koordinat verileri bu listede toplanıyor

cubuk_stifness_matrix2 = list()


for i in koordinat_verileri[0] :

    yi = i[0]
    zi = i[1]
    yj = i[2]
    zj = i[3]

    L: float = np.sqrt((yj-yi)**2+(zj-zi)**2)

    S = A*E/L
    my = (yj - yi) / L
    ny = (zj - zi) / L
    t = [[my,ny],[-ny,my]]

    cubuk_stifness_matrix =[[S,0.,-S,0.],[0.,0.,0.,0.],[-S,0.,S,0.],[0.,0.,0.,0.]]

    cubuk_stifness_matrix2.append(cubuk_stifness_matrix)

    cubuk_dogrultu_kosinüs.append(t)




## Her Çubugun trasformasyon matrisi bu dizi içerisine depolanıp döngü ile çubugun genel
## transformasyon matrisi elde edilecek

sıfır_matris = np.zeros((2,2))

cubuk_matrisleri_transpose = list() ## Sistemin çubuk doğrultu kosinüs matrisleri bu dizi içerisinden toplanacak

cubuk_dogrultu_matrisleri = list()

for i in cubuk_dogrultu_kosinüs:

    t1=np.hstack((i,sıfır_matris))

    t2=np.hstack((sıfır_matris,i))

    T=np.vstack((t1,t2))

    T_transpose = T.transpose(1,0)

    cubuk_dogrultu_matrisleri.append(T)

    cubuk_matrisleri_transpose.append(T_transpose)









musterek_stifness = list()
for i in range(len(koordinat_verileri[0])):

    matrix = np.dot(cubuk_stifness_matrix2[i],cubuk_dogrultu_matrisleri[i])

    matrix = np.dot(cubuk_matrisleri_transpose[i],matrix)

    musterek_stifness.append(matrix)



# Cubuk Eksen takımlarına göre Verilmiş olan stifnes matrislerini, müşterek eksen takımlarına çevirdik
# Üçlü çarpı formulu kullanıldı.


#### Sözlükteki verileri kopyalayarak bir önceki değerlerin değişmesini engelledik, Daha sonra dugum adet verisini alıp

### Sözlükten Bu veriyi silip kopyaladığımız veri üzerinden kod numaralarını alıp Sistemin Stifness Matrixi'ni oluşturacak

### Kombinasyonları Tanımladık
coordinates = koordinatlar.copy()

nodes_nummers = coordinates["dugum_adeti"]

coordinates.pop("dugum_adeti")
code_nummers  = list(coordinates.keys())
system_length = nodes_nummers * 2


system_matrix = np.zeros((system_length,system_length))

#######
stifness_index = [1,2,3,4] ### Her Cubuk için Oluşturulacak sıralı kodlar , Karşılarına Sistemin Kodları gelecek

## Ana sistem Matrisini oluşturacak veri elde edilmiş olacak


stifness_index2 = list()

for i in stifness_index:
    for j in stifness_index:
        stifness_index2.append([i,j])





system_index = list()
system_index2 = list()
for i in code_nummers[0]:

    for j in list(i):

        for k in list(i):


            system_index.append([j,k])

system_index2 = np.hstack((len(code_nummers[0])*stifness_index2,system_index))


for i in musterek_stifness:
    for j in system_index2 :

        system_matrix[j[2]-1][j[3]-1] =  system_matrix[j[2]-1][j[3]-1] + i[j[0]-1][j[1]-1]
import timeit



print(system_matrix)

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
