def kod_numarası_düzlem_kafes(koordinatlar):
    import numpy as np

    import itertools
    koordinatlar = koordinatlar
    baslangıc = []
    bitis = [ ]

    for i in koordinatlar:
        baslangıc.append([i[0],i[1]])
        bitis.append([i[2],i[3]])

    dugum_koordinatarı = set()


    for i in baslangıc:


        for j in baslangıc :

            if j == i :

                dugum_koordinatarı.add((i[0],i[1]))

    for i in baslangıc:


        for j in bitis  :

            if j == i :

                dugum_koordinatarı.add((i[0],i[1]))

    for i in bitis  :


        for j in bitis  :

            if j == i :

                dugum_koordinatarı.add((i[0],i[1]))

    dugum_koordinatarı = list(dugum_koordinatarı)
    ### Kümeler İndeksleme Desteklemediği için Veriyi Listeye çevirmek daha iyi



    x = 1
    y = 2

    dugum_kodları = dict()
    for i in dugum_koordinatarı:

        dugum_kodları[i] = (x,y)

        x += 2
        y += 2


    dugum_permutasyon = list(itertools.permutations(list(dugum_kodları.keys()),2)) ### Permütasyon ile düğüm noktalarının oluşturacağı tüm koordinatları hesapladık
    ### sözlük.keys() metdo ile key değerlerini aldık



    olusacak_dugum_koordinatarı= list() ### Dugum kodları için bos liste
    for i in dugum_permutasyon :
        test = list(np.hstack((i[0],i[1])))
        olusacak_dugum_koordinatarı.append(test)

    global yeni_cubuk_koordinatları

    yeni_cubuk_koordinatları = list()

    nihai_kod_numaraları = list()

    result = dict()



    ### Olusan Permutasyonlar var olan sistem koordinatları içerisinde aranır eğer bu koordinatlar bulunursa
    ### Cubukların koordinatları bulunmuş olur , Daha sonra Başlangıc ve Bitiş noktalarına atanan kod lar Sözlükten
    ### Alınır ve birleştirilerek Çubugun kod numarası oluşturulur
    ### Sistem bu şekilde cubukları yeniden düzenleyerek Yeniden Sıralandırmasını Yapar


    for i in olusacak_dugum_koordinatarı:


        for j in koordinatlar:

            if i == j :
                yeni_cubuk_koordinatları.append(i)
                kod_numarası1 = dugum_kodları[tuple(i[:2])]
                kod_numarası2 = dugum_kodları[tuple(i[2:])]


                nihai_kod_numaraları.append(tuple(np.hstack((list(kod_numarası1),list(kod_numarası2)))))



    result[tuple(nihai_kod_numaraları)] = tuple(yeni_cubuk_koordinatları)
    result["dugum_adeti"] = len(dugum_koordinatarı)
    return result


