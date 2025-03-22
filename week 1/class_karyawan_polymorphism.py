class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.__nama = nama
        self.__id_karyawan = id_karyawan
        self.__absensi = []

    def tambah_absensi(self, waktu):
        self.__absensi.append(waktu)

    def get_absensi(self):
        return self.__absensi

    def get_nama(self):
        return self.__nama
        
class KaryawanRemote(Karyawan): 
    def __init__(self, nama, id_karyawan, lokasi):
        super().__init__(nama, id_karyawan)
        self.lokasi = lokasi 
    
    def get_lokasi(self):
        return self.lokasi
        
class HR:
    def lihat_absensi(self, karyawan):
        print(f"Absensi {karyawan.get_nama()}: {karyawan.get_absensi()}")

class Manajer(HR):
    def lihat_absensi(self, karyawan):
        print(f"Manajer memeriksa absensi {karyawan.get_nama()} dengan detail: {karyawan.get_absensi()}")


karyawan1 = Karyawan("Ali", 101)
karyawan1.tambah_absensi("2025-03-22 08:15")
print(karyawan1.get_nama())
print(karyawan1.get_absensi())

hr = HR()
manajer = Manajer()

hr.lihat_absensi(karyawan1)
manajer.lihat_absensi(karyawan1)
