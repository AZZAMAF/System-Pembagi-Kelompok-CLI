Pemetaan Struktur Data (Pengganti ERD)

    Entitas 1: Data Mahasiswa (Input)

        Bentuk Mentah: File absen_kelas.csv berisi daftar nama.

        Struktur di Python: List of Strings atau List of Dictionaries jika ingin memasukkan NIM.

        Contoh Visual: ["Andi", "Budi", "Siti", "Joko"]

    Entitas 2: Wadah Kelompok (Proses & Output)

        Bentuk Mentah: File hasil_kelompok.txt atau .json.

        Struktur di Python: Dictionary di mana Key adalah nama kelompok, dan Value adalah List anggota.

        Contoh Visual: {"Kelompok 1": ["Andi", "Siti"], "Kelompok 2": ["Budi", "Joko"]}

Brainstorming Alur Logika (Flowchart Konseptual)

    Fase Ingest (Tarik Data): Program membaca baris demi baris dari file .csv dan menyimpannya ke dalam List utama bernama daftar_mahasiswa.

    Fase Validasi: Program menghitung len(daftar_mahasiswa) dan meminta input jumlah kelompok dari user. Harus ada pengecekan keamanan: jika user memasukkan huruf atau angka yang lebih besar dari total mahasiswa, program memunculkan pesan error dan meminta input ulang.

    Fase Shuffle: Urutan indeks di dalam List daftar_mahasiswa diacak posisinya secara acak.

    Fase Distribusi: Ini core logic-nya. Program menyiapkan wadah (Dictionary) kosong sesuai jumlah kelompok. Kemudian program melakukan looping (perulangan) pada List yang sudah diacak, dan memasukkan nama satu per satu ke tiap kelompok secara bergantian (bisa menggunakan operator modulo) agar jumlah anggota terbagi rata.

    Fase Ekspor: Program membaca Dictionary hasil distribusi dan menulis ulang isinya ke dalam file teks baru agar siap di-copy-paste ke grup obrolan.