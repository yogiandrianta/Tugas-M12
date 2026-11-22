#1
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

daftar_karyawan = [
    Karyawan("Javier", 5000000),
    Karyawan("Dimas", 4500000),
    Karyawan("El Faiz", 4000000),
    Karyawan("Aldrich", 5500000),
    Karyawan("Gibran", 6000000)
]

for k in daftar_karyawan:
    print(f"Karyawan {k.nama} memiliki gaji {k.gaji}.")

#2
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        self.energi = 100  
    def lembur(self):
        print(f"{self.nama} sedang lembur!") 
        self.energi -= 30
        self.gaji += 200000 

siti = Karyawan("Siti", 5000000)
print(f"Karyawan {siti.nama} memiliki gaji {siti.gaji}.")

siti.lembur()
print(f"Sisa energi {siti.nama}: {siti.energi}")
print(f"Gaji terbaru {siti.nama}: {siti.gaji}\n")

daftar_karyawan = [
    Karyawan("Siti", 5000000),
    Karyawan("Budi", 6500000),
    Karyawan("Andi", 5500000),
    Karyawan("Dewi", 7000000),
    Karyawan("Rizky", 6000000),
]

for k in daftar_karyawan:
    print(f"Karyawan {k.nama} memiliki gaji {k.gaji}.") 
    k.lembur()
    print(f"Sisa energi {k.nama}: {k.energi} | Gaji terbaru: {k.gaji}\n")

#3
class Barang:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

baju = Barang("Baju", 100000)

baju.harga = 75000

print(f"Harga terbaru {baju.nama}: {baju.harga}")

#4
class RekeningBank:
    def __init__(self, nama_pemilik, saldo=0):
        self.nama_pemilik = nama_pemilik
        self.saldo = saldo

    def menabung(self, nominal):
        self.saldo += nominal
        print(f"Berhasil menabung Rp{nominal}. Saldo sekarang: Rp{self.saldo}")

    def tarik_tunai(self, nominal):
        if self.saldo >= nominal:
            self.saldo -= nominal
            print(f"Berhasil menarik Rp{nominal}. Saldo sekarang: Rp{self.saldo}")
        else:
            print("Maaf, saldo tidak mencukupi.")

rekening_saya = RekeningBank("Yogi")
rekening_saya.menabung(500000)
rekening_saya.tarik_tunai(200000)
rekening_saya.tarik_tunai(400000)