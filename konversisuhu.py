def konversi_suhu(nilai, unit):
    unit = unit.upper()
    if unit == 'C':
        hasil = (nilai * 9/5) + 32
        return f"{nilai} °C sama dengan {hasil:.2f} °F"
    elif unit == 'F':
        hasil = (nilai - 32) * 5/9
        return f"{nilai} °F sama dengan {hasil:.2f} °C"
    else:
        return "Unit tidak valid! Gunakan 'C' atau 'F'."

print("--- Program Konversi Suhu ---")
input_nilai = float(input("Masukkan nilai suhu: "))
input_unit = input("Masukkan satuan awal (C/F): ")

print(konversi_suhu(input_nilai, input_unit))