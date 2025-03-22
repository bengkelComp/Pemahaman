class Karyawan:
    def __init__(self, nama, id_karyawan):
        self.__nama = nama # Atribut private
        self.__id_karyawan = id_karyawan
        self.__absensi = []  # List untuk menyimpan data absensi

    def tambah_absensi(self, waktu):
        self.__absensi.append(waktu)

    def get_absensi(self):
        return self.__absensi

    def get_nama(self):
        return self.__nama

karyawan1 = Karyawan("Ali", 101)
karyawan1.tambah_absensi("2025-03-22 08:15")
print(karyawan1.get_nama())
print(karyawan1.get_absensi())
