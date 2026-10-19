import processor_json
import random
import json



mahasiswa = processor_json.read_json("data/mahasiswa-cs.json")
output_group = []
def add_new_file_group(filename,data_group):
    with open(f"data/Output/{filename}.json", "w") as f:
        json.dump(data_group, f,indent=4)  

def shuffle_data(spread_rule):
    shuffle_mhs = mahasiswa.copy()
    random.shuffle(shuffle_mhs)
    for index, i in enumerate(range(0, len(shuffle_mhs), spread_rule)):
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
    rule_spread_group = int(input("Masukkan jumlah mahasiswa per kelompok: 3 / 4 / 6: "))
    match rule_spread_group:
        case 3:
            print("Jumlah mahasiswa per kelompok: 3")
            final_data_group =shuffle_data(rule_spread_group)
            name_file_input = input("Masukkan nama file untuk menyimpan data grouping (contoh: group-3.json): ")
            add_new_file_group(name_file_input, final_data_group)
            
        case 4:
            print("Jumlah mahasiswa per group: 4")
            final_data_group = shuffle_data(rule_spread_group)
            name_file_input = input("Masukkan nama file untuk menyimpan data grouping (contoh: group-4.json): ")
            add_new_file_group(name_file_input, final_data_group)
            
        case 6:
            print("Jumlah mahasiswa per group: 6")
            final_data_group = shuffle_data(rule_spread_group)
            name_file_input = input("Masukkan nama file untuk menyimpan data grouping (contoh: group-4.json): ")
            add_new_file_group(name_file_input, final_data_group)

