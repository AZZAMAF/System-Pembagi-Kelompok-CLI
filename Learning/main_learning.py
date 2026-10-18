import json
import shutil


# Path file asal dan folder tujuan dari folder utama proyek
path_asal = "data/data.json"
path_tujuan = "data/kelompok/tes.json"  # Bisa diberi nama baru, misal data_kelompok.json

# Copy file
shutil.copy(path_asal, path_tujuan)

print("File berhasil disalin ke folder Kelompok!")

with open(path_tujuan, "r") as file:
    data = json.load(file)
    # data.append({"nim": "103000", "nama": "Suep"})  # Menambahkan data baru
    print(data)
with open(path_tujuan,"a")as file:
    data.append({"nim": "103000", "nama": "Suep"})  # Menambahkan data baru
    print(data) 
with open(path_tujuan, "w") as file:
    json.dump(data, file, indent=2)  # Menyimpan data kembali ke file JSON dengan format yang rapi