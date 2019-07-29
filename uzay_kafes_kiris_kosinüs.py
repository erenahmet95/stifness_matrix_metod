import numpy as np

### Bir Cubugun Doğrultu Kosinüs Vektörlerini Bulupyoruz
T = np.zeros((6, 6))

xi = 3.6
zi = 4.5
xj = -6.2
zj = 1.8
yi = 2.8
yj = 4.5
L: float = np.sqrt((yj - yi) ** 2 + (zj - zi) ** 2 + (xi - xj) ** 2)

ly = (xj - xi) / L
my = (yj - yi) / L
ny = (zj - zi) / L
Q = abs(np.sqrt(1 - ny ** 2))

t = [[my / Q, -ly / Q, 0], [ly, my, ny], [-ly * ny / Q, -my * ny / Q, Q]]

cubuk_transformasyon = list()
cubuk_transformasyon.append(t)
## Her Çubugun trasformasyon matrisi bu dizi içerisine depolanıp döngü ile çubugun genel
## transformasyon matrisi elde edilecek

sıfır_matris = np.zeros((3, 3))
cubuk_matrisleri = list()  ## Sistemin çubuk transformasyon matrisleri bu dizi içerisinden toplanacak
for i in cubuk_transformasyon:
    t1 = np.hstack((i, sıfır_matris))
    t2 = np.hstack((sıfır_matris, i))
    T = np.vstack((t1, t2))
    T = T.transpose(1, 0)

    cubuk_matrisleri.append(T)

kuvvet_kolonu = np.array((20, 0, 0, -20, 0, 0))
print(np.dot(cubuk_matrisleri, kuvvet_kolonu))
# Yük kolonu ile çarptıgımızda cubugun kuvvetlerinin müşterek koordinat sisteminde ki değerlerini bulmuş oluruz.
