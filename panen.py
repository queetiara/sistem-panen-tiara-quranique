def hitung_total_panen(jumlah_karung, berat_per_karung):
    total = jumlah_karung * berat_per_karung
    return total

def input_data_panen():
    komoditas = input("Nama komoditas: ")
    jumlah = float(input("Jumlah hasil panen (kg): "))
    return komoditas, jumlah
    
def hitung_diskon(total_harga, persen_diskon):
    potongan = total_harga * persen_diskon / 100
    harga_akhir = total_harga - potongan
    return harga_akhir

jumlah_karung = 12
berat_per_karung = 25
harga_per_kg = 8000

total_panen = hitung_total_panen(jumlah_karung, berat_per_karung)
total_harga = total_panen * harga_per_kg
harga_akhir = hitung_diskon(total_harga, 5)

print("Total hasil panen :", total_panen, "kg")
print("Total harga : Rp", total_harga)
print("Harga setelah diskon : Rp", harga_akhir)
