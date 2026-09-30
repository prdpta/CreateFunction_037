import math

luas_lingkaran = lambda r: math.pi * (r ** 2)

print("--- Program Hitung Luas Lingkaran ---")
input_jari = float(input("Masukkan panjang jari-jari (r): "))

hasil_luas = luas_lingkaran(input_jari)
print(f"Luas lingkaran dengan jari-jari {input_jari} adalah: {hasil_luas:.2f}")