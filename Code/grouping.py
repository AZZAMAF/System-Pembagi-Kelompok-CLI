import processor_json

def grouping_data():
    mahasiswa = processor_json.read_json("../data/mahasiswa-cs.json")
    output_group = []
    # if mahasiswa is not None:
    #     for name in mahasiswa:
    #         print(f"{name}")
    # else:
    #     print("Data grouping tidak tersedia karena file mahasiswa-cs.json tidak ditemukan atau tidak valid.")
    rule_spread_group = int(input("Masukkan jumlah mahasiswa per kelompok: 3 / 4 / 6: "))
    match rule_spread_group:
        case 3:
            print("Jumlah mahasiswa per kelompok: 3")
            for index, i in enumerate(range(0, len(mahasiswa), rule_spread_group)):
                slice_mahasiswa = mahasiswa[i:i + rule_spread_group]
                data_group = {
                    "group": index + 1,
                    "members": slice_mahasiswa
                }
                output_group.append(data_group)
            print("Data grouping mahasiswa:")
            for group in output_group:
                # Ambil nama dari setiap dictionary anggota
                nama_anggota = [mhs['nama'] for mhs in group['members']]
                print(f"Kelompok {group['group']}: {', '.join(nama_anggota)}")
        case 4:
            print("Jumlah mahasiswa per group: 4")
            for index, i in enumerate(range(0, len(mahasiswa), rule_spread_group)):
                slice_mahasiswa = mahasiswa[i:i + rule_spread_group]
                data_group = {
                    "group": index + 1,
                    "members": slice_mahasiswa
                }
                output_group.append(data_group)
            print("Data grouping mahasiswa:")
            for group in output_group:
                # Ambil nama dari setiap dictionary anggota
                nama_anggota = [mhs['nama'] for mhs in group['members']]
                print(f"Kelompok {group['group']}: {', '.join(nama_anggota)}")
        case 6:
            print("Jumlah mahasiswa per group: 6")
            for index, i in enumerate(range(0, len(mahasiswa), rule_spread_group)):
                slice_mahasiswa = mahasiswa[i:i + rule_spread_group]
                data_group = {
                    "group": index + 1,
                    "members": slice_mahasiswa
                }
                output_group.append(data_group)
            print("Data grouping mahasiswa:")
            for group in output_group:
                # Ambil nama dari setiap dictionary anggota
                nama_anggota = [mhs['nama'] for mhs in group['members']]
                print(f"Kelompok {group['group']}: {', '.join(nama_anggota)}")

grouping_data()