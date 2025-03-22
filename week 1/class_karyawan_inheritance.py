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

karyawan_remote = KaryawanRemote("Ali", 102, "Surabaya")
print(karyawan_remote.get_nama()) 
print(karyawan_remote.get_lokasi())
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

karyawan_remote = KaryawanRemote("Ali", 102, "Surabaya")
print(karyawan_remote.get_nama()) 
print(karyawan_remote.get_lokasi())
