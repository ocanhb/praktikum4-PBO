# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:09:21 2024

@author: ocanh
"""

class Student:
    # deklarasi variabel (instance dan class)
    data_pribadi = "--- Data pribadi ---"  # variabel class

    # constructor untuk inisialisasi objek student
    def __init__(self, nama="", nim="", nilai=""):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    # method untuk mencetak data siswa
    def print_data(self):
        print("Nama :", self.nama)
        print("Nim :", self.nim)
        print("Nilai :", self.nilai)

    # method statis untuk validasi nilai
    @staticmethod
    def validate_nilai(nilai):
        try:
            nilai = float(nilai)
            if 0 <= nilai <= 100:
                return True
            else:
                return False
        except ValueError:
            return False


def main():
    # Meminta pengguna untuk memasukkan data pribadi siswa
    print("--- Data pribadi ---")
    nama_siswa = input("Nama : ")
    nim_siswa = input("Nim : ")
    nilai_siswa = input("Nilai : ")

    # Membuat objek-objek teman
    teman1 = Student()
    teman2 = Student()
    teman3 = Student()

    # Meminta pengguna untuk memasukkan data teman
    print("--- Data Teman 1 ---")
    teman1.nama = input("Nama : ")
    teman1.nim = input("Nim : ")
    teman1.nilai = input("Nilai : ")

    print("--- Data Teman 2 ---")
    teman2.nama = input("Nama : ")
    teman2.nim = input("Nim : ")
    teman2.nilai = input("Nilai : ")

    print("--- Data Teman 3 ---")
    teman3.nama = input("Nama : ")
    teman3.nim = input("Nim : ")
    teman3.nilai = input("Nilai : ")

if __name__ == "__main__":
    main()
