
# O = boş, X = dolu
koltuklar = {
    "S1": ["0"] * 10,
    "S2": ["0"] * 10
}

seanslar = {
    "S1": "Batman - 20:00",
    "S2": "Space Odyssey - 18:30"
}

rezervasyonlar = []  

def seanslari_goster():
    print("\nSeanslar:")
    for sid in seanslar:
        print(sid, "->", seanslar[sid])

def koltuklari_goster(seans_id):
    print("\nKoltuklar (1-10):")
    dizi = koltuklar[seans_id]
    for i in range(10):
        print(i+1, dizi[i], end="   ")
    print("\nO=Boş  X=Dolu")

def rezervasyon_yap():
    seanslari_goster()
    seans_id = input("Seans seç (S1/S2): ").strip().upper()
    if seans_id not in seanslar:
        print("Yanlış seans.")
        return

    koltuklari_goster(seans_id)
    try:
        no = int(input("Koltuk numarası (1-10): "))
    except:
        print("Sayı gir.")
        return

    if no < 1 or no > 10:
        print("Aralık dışı.")
        return

    if koltuklar[seans_id][no-1] == "X":
        print("Bu koltuk dolu.")
        return

    rid = len(rezervasyonlar) + 1
    koltuklar[seans_id][no-1] = "X"
    rezervasyonlar.append((rid, seans_id, no))
    print(" Rezervasyon ok. ID:", rid)

def rezervasyonlari_goster():
    if not rezervasyonlar:
        print("Hiç rezervasyon yok.")
        return
    print("\nRezervasyonlar:")
    for r in rezervasyonlar:
        print("ID:", r[0], "|", seanslar[r[1]], "| Koltuk:", r[2])

def iptal_et():
    rezervasyonlari_goster()
    if not rezervasyonlar:
        return
    try:
        rid = int(input("İptal edilecek ID: "))
    except:
        print("Sayı gir.")
        return

    for r in rezervasyonlar:
        if r[0] == rid:
            seans_id = r[1]
            no = r[2]
            koltuklar[seans_id][no-1] = "O"
            rezervasyonlar.remove(r)
            print(" İptal edildi.")
            return

    print("ID bulunamadı.")

while True:
    print("\n1) Seanslar  2) Rezervasyon Yap  3) Rezervasyonlarım  4) İptal  0) Çıkış")
    secim = input("> ").strip()

    if secim == "1":
        seanslari_goster()
    elif secim == "2":
        rezervasyon_yap()
    elif secim == "3":
        rezervasyonlari_goster()
    elif secim == "4":
        iptal_et()
    elif secim == "0":
        print("Görüşürüz.")
        break
    else:
        print("Geçersiz seçim.")
