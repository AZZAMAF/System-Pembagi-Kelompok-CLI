from Code import processor_json
import random
import json



mahasiswa = processor_json.read_json("data/mahasiswa-cs.json")

def add_new_file_group(filename,data_group):
    with open(f"data/Output/{filename}.json", "w") as f:
        json.dump(data_group, f,indent=4)  

def shuffle_data(spread_rule):
    shuffle_mhs = mahasiswa.copy()
    random.shuffle(shuffle_mhs)
    output_group = []
    for index, i in enumerate(range(0, len(shuffle_mhs), spread_rule)):
        # print(range(0, len(shuffle_mhs), spread_rule))
        slice_mahasiswa = shuffle_mhs[i:i + spread_rule]
        data_group = {
            "group": index + 1,
            "members": slice_mahasiswa
        }
        output_group.append(data_group) 
    return output_group
    
    # print("Data grouping mahasiswa:")
    # for group in output_group:
    # # Ambil nama dari setiap dictionary anggota
    #     nama_anggota = [mhs['nama'] for mhs in group['members']]
    #     print(f"Kelompok {group['group']}: {', '.join(nama_anggota)}")
    
def grouping_data():
    # if mahasiswa is not None:
    #     for name in mahasiswa:
    #         print(f"{name}")
    # else:
    #     print("Data grouping tidak tersedia karena file mahasiswa-cs.json tidak ditemukan atau tidak valid.")
    rule_group = int(input("Masukkan jumlah mahasiswa per kelompok: 3 / 4 / 6: "))
    # print(f"Jumlah mahasiswa per kelompok: {rule_group}")
    match rule_group:
        case 3:
            print("Jumlah mahasiswa per kelompok: 3")
            final_data_group = shuffle_data(rule_group)
            # print(final_data_group)
            name_file_input = input("Masukkan nama file untuk menyimpan data grouping (contoh: group-3.json): ")
            add_new_file_group(name_file_input, final_data_group)
            
        case 4:
            print("Jumlah mahasiswa per group: 4")
            final_data_group = shuffle_data(rule_group)
            name_file_input = input("Masukkan nama file untuk menyimpan data grouping (contoh: group-4.json): ")
            add_new_file_group(name_file_input, final_data_group)
            
        case 6:
            print("Jumlah mahasiswa per group: 6")
            final_data_group = shuffle_data(rule_group)
            name_file_input = input("Masukkan nama file untuk menyimpan data grouping (contoh: group-4.json): ")
            add_new_file_group(name_file_input, final_data_group)
        case _:
            print("Pilihan tidak valid. Silakan pilih jumlah mahasiswa per kelompok yang tersedia (3 / 4 / 6).")


#---------- UBAY


# 2. Fungsi utama untuk melihat/cek isi kelompok
def show_group():
    
    nama_file = input("Masukkan nama file grouping (sama seperti saat menyimpan): ")
    data_group = processor_json.read_json("data/output/" + nama_file + ".json")
   
    nomor = int(input("Masukkan nomor kelompok: "))

    # Cari kelompok yang nomornya sama dengan input (looping)
    for kelompok in data_group:
        if kelompok["group"] == nomor:
            print(f"\nKelompok {nomor}")
            # enumerate dipakai untuk membuat nomor urut 1, 2, 3, ...
            for urutan, mhs in enumerate(kelompok["members"], 1):
                print(f"{urutan}. {mhs['nama']} - {mhs['nim']}")
            return

    # Kalau perulangan selesai dan tidak ketemu, berarti nomor kelompok tidak ada
    print("Kelompok tidak ditemukan.")


def remove_group():
    # 1. Minta nama file JSON
    nama_file = input("Masukkan nama file grouping (contoh: group-3): ")
    path_file = f"data/Output/{nama_file}.json"

    # 2. Baca isi file JSON pakai helper processor_json
    data_group = processor_json.read_json(path_file)

    if not data_group:
        print("File tidak ditemukan atau data kosong.")
        return

    # 3. Minta nomor kelompok yang mau dihapus
    nomor_hapus = int(input("Masukkan nomor kelompok yang ingin dihapus: "))

    # 4. Filter data: simpan kelompok yang TIDAK dihapus
    new_data_group = []
    kelompok_ditemukan = False

    for kelompok in data_group:
        if kelompok["group"] == nomor_hapus:
            kelompok_ditemukan = True
        else:
            new_data_group.append(kelompok)

    if not kelompok_ditemukan:
        print(f"Kelompok nomor {nomor_hapus} tidak ditemukan.")
        return

    # 5. Rapikan ulang nomor kelompok sisanya (1, 2, 3...)
    for index, kelompok in enumerate(new_data_group, 1):
        kelompok["group"] = index

    # 6. Simpan kembali data yang sudah di-update
    add_new_file_group(nama_file, new_data_group)
    print(
        f"Berhasil menghapus Kelompok {nomor_hapus} dari file '{nama_file}.json'!\n"
    )