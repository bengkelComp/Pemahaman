from abc import ABC, abstractmethod

class Absensi(ABC):
    @abstractmethod
    def catat_absensi(self, waktu):
        pass

class AbsensiKaryawan(Absensi):
    def __init__(self, nama):
        self.nama = nama
        self.absensi = []

    def catat_absensi(self, waktu):
        self.absensi.append(waktu)
        print(f"Absensi {self.nama} dicatat pada {waktu}")

karyawan_absensi = AbsensiKaryawan("Dewi")
karyawan_absensi.catat_absensi("2025-03-22 09:00")
