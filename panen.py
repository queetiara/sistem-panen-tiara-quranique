def hitung_total_panen(jumlah_karung, berat_per_karung):
    total = jumlah_karung * berat_per_karung
    return total

jumlah_karung = 12
berat_per_karung = 25

total_panen = hitung_total_panen(jumlah_karung, berat_per_karung)

print("Total hasil panen :", total_panen, "kg")