import numpy as np

T = np.zeros((6,6))

xi = 0
zi = 16.5
xj = 0
zj = 8.3
yi = 4.5
yj = 10.6
L: float = np.sqrt((yj-yi)**2+(zj-zi)**2)

ly = (xj - xi) / L
my = (yj - yi) / L
ny = (zj - zi) / L

t = [[my,ny,0],[-ny,my,0],[0,0,1]]

cubuk_dogrultu_kosinüs = list()

cubuk_dogrultu_kosinüs.append(t)
cubuk_dogrultu_kosinüs.append(t)
cubuk_dogrultu_kosinüs.append(t)
## Her Çubugun trasformasyon matrisi bu dizi içerisine depolanıp döngü ile çubugun genel
## transformasyon matrisi elde edilecek

sıfır_matris = np.zeros((3,3))
cubuk_kosinüs_matrisleri_transpos = list() ## Sistemin çubuk doğrultu kosinüs matrisleri bu dizi içerisinden toplanacak
cubuk_kosinüs_matrisleri = list()
for i in cubuk_dogrultu_kosinüs:

    t1=np.hstack((i,sıfır_matris))
    t2=np.hstack((sıfır_matris,i))
    T=np.vstack((t1,t2))
    cubuk_kosinüs_matrisleri.append(T)
    T_transpose = T.transpose(1,0)
    cubuk_kosinüs_matrisleri_transpos.append(T_transpose)




##### Cubuk Stifness MAtrislerinin Oluşturulması:

aix =1
ajx = 2
aiz = 3
ajz= 4
E = 5
Ix = 6
bx = 7
bz = 8
A = 9
G = 10
J = 11

Iz = 12
Ai = aix*E*Ix/L ## Yz Düzlemindeki Eğilme
Aj = ajx*E*Ix/L
B = bx*E*Ix/L

Ci = (aix+bx)*E*Ix/(L**2)
Cj = (ajx+bx)*E*Ix/(L**2)
D = (aix + ajx +2*bx)*E*Ix/(L**3)
S = A*E/L## Eksenel Rijitlik
T = G*J/L ## Burulma Rijitliği

Ei = aiz* E*Iz/L ## XY Düzlemindeki Eğilme için Temel Stifness Sayıları
Ej = ajz*E*Iz/L
F = bz*E*Iz/L


## Bir Döngü ile her cubugun kendi stifness matrix lerini oluşturup sistemin genel cubuk matrixlerini elde etmemiz gerekiyor
k_cubuk = [[S,0,0,-S,0,0],[0,D,Ci,0,-D,Cj],[0,Ci,Ai,0,-Ci,B],[-S,0,0,S,0,0],[0,-D,-Ci,0,D,-Cj],[0,Cj,B,0,-Cj,Aj]]

sistem_cubuk_matrix = [[[S,0,0,-S,0,0],[0,D,Ci,0,-D,Cj],[0,Ci,Ai,0,-Ci,B],[-S,0,0,S,0,0],[0,-D,-Ci,0,D,-Cj],[0,Cj,B,0,-Cj,Aj]],
                       [[S,0,0,-S,0,0],[0,D,Ci,0,-D,Cj],[0,Ci,Ai,0,-Ci,B],[-S,0,0,S,0,0],[0,-D,-Ci,0,D,-Cj],[0,Cj,B,0,-Cj,Aj]],
                       [[S,0,0,-S,0,0],[0,D,Ci,0,-D,Cj],[0,Ci,Ai,0,-Ci,B],[-S,0,0,S,0,0],[0,-D,-Ci,0,D,-Cj],[0,Cj,B,0,-Cj,Aj]]]



musterek_stifness = list()
for i in range(len(sistem_cubuk_matrix)):

    matrix = np.dot(sistem_cubuk_matrix[i],cubuk_kosinüs_matrisleri[i])

    matrix = np.dot(cubuk_kosinüs_matrisleri_transpos[i],matrix)

    musterek_stifness.append(matrix)




print(cubuk_kosinüs_matrisleri)
print(sistem_cubuk_matrix)
print("musterek matrix", musterek_stifness)
