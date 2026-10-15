# PRD v5 — CLI Kelompok Mahasiswa (MVP)

Pemilik produk: Azzam · Status: draf untuk dikonfirmasi tim · 15 Oktober 2026

Catatan: bagian 1 sampai 3 adalah **draf asumsi** dari mentor. Ganti dengan kata-kata sendiri kalau tidak sesuai. Bagian lain sudah berupa keputusan.

## 1. Konteks produk

**Pengguna:** dosen pengampu mata kuliah yang membagi satu kelas (sekitar 20 sampai 40 mahasiswa) ke kelompok tugas.

**Masalah:** membagi kelompok secara manual memakan waktu, sering dianggap tidak adil, dan kalau ada perubahan (mahasiswa pindah, kelompok dibubarkan) hasilnya harus dibuat ulang dari awal.

**Solusi:** aplikasi CLI yang mengacak pembagian, menyimpan setiap hasil sebagai arsip, dan memungkinkan hasil itu diubah tanpa mengulang dari nol.

**Pemilik keputusan:** keputusan produk (apa yang dibuat dan tidak dibuat) ada di Azzam. Keputusan teknis (cara membuat sebuah modul) ada di anggota yang mengerjakan modul itu.

## 2. Definisi berhasil

**Skenario demo utama.** Dosen menjalankan aplikasi dengan 37 mahasiswa dari file sumber, membagi mereka menjadi 6 kelompok (7, 6, 6, 6, 6, 6), memindahkan satu anggota ke kelompok lain, menutup program, lalu membukanya lagi dan melihat hasil akhir yang sama. Selama itu program tidak crash dan file sumber tidak berubah.

Produk dianggap selesai kalau skenario ini bisa dijalankan dari menu utama oleh orang yang bukan pembuatnya, dan semua tes pada bagian 9 lulus.

## 3. Scope dan batas pemotongan

MVP mencakup menu 1 sampai 8. Karena tim pemula, pengerjaan dibagi per tahap dengan **garis potong** yang jelas:

| Tahap | Isi | Status |
| --- | --- | --- |
| Tahap 1 | Menu 5, 6, 7 (bagi, lihat, ubah kelompok). Data mahasiswa dibaca langsung dari file sumber. | Wajib. Urutan kerja: menu 5, 6, lalu 7 |
| Tahap 2 | Menu 1 sampai 4 (kelola mahasiswa) | Wajib, tapi dipotong lebih dulu kalau waktu habis |
| Lanjutan | Menu 8 (hapus kelompok): nomor kelompok diurut ulang, anggota tanpa kelompok ditempatkan manual atau otomatis | Setelah MVP stabil |

Tahap 1 dan tahap 2 dikerjakan paralel oleh orang berbeda, jadi tahap hanya menentukan prioritas, bukan urutan waktu. Kalau waktu habis, tahap 2 dipotong lebih dulu: daftar mahasiswa diubah dengan mengedit file sumber secara manual di luar aplikasi. Kalau menu 7 belum selesai, skenario demo diturunkan menjadi "bagi dan lihat hasil". Keputusan memotong diambil oleh pemilik produk.

**Tidak termasuk (dengan alasan):**

- Database, API, login, GUI, library pihak ketiga: tidak dibutuhkan untuk masalah ini dan menambah beban belajar.
- Mengedit file sumber: sumber dijaga tetap utuh sebagai data awal yang bisa dikembalikan.
- Pembagian otomatis anggota yang belum berkelompok: dosen cukup memindahkan manual lewat menu 7.
- Reset data kerja ke sumber, timestamp arsip, penulisan file yang atomik: berguna tapi bukan syarat skenario demo. Masuk fase lanjutan.

## 4. Istilah baku

Satu istilah untuk satu konsep, supaya tim tidak mengira ada dua fitur.

- **Data kerja:** daftar mahasiswa yang sedang aktif dan dikelola lewat menu 1 sampai 4.
- **Arsip:** satu file hasil pembagian di folder `output/`.
- **Belum berkelompok:** mahasiswa yang ada di sebuah arsip tetapi tidak berada di kelompok mana pun (muncul setelah hapus kelompok).
- **Ubah kelompok:** memindahkan satu anggota antar kelompok. Kata "edit" dan "update" tidak dipakai.

## 5. Menu

```text
===== CLI KELOMPOK MAHASISWA =====

A. MANAJEMEN MAHASISWA
1. Tambah anggota
2. Lihat anggota
3. Ubah anggota
4. Hapus anggota

B. MANAJEMEN KELOMPOK
5. Bagi kelompok
6. Lihat kelompok
7. Ubah kelompok
8. Hapus kelompok

0. Keluar
```

Di setiap langkah input, pengguna bisa mengetik `0` untuk membatalkan dan kembali ke menu.

## 6. Keputusan teknis yang sudah dikunci

| # | Topik | Keputusan |
| --- | --- | --- |
| K1 | File kerja | Saat mulai: jika `mahasiswa-kerja.json` ada, baca itu. Jika tidak, baca file sumber. File kerja baru dibuat saat perubahan pertama disimpan. File sumber tidak pernah ditulis. Selama menu 1 sampai 4 belum dibuat, program membaca file sumber langsung dan tidak membuat file kerja. |
| K2 | Jumlah kelompok dari kapasitas | Jumlah kelompok = pembulatan ke atas dari (jumlah mahasiswa dibagi kapasitas). Anggota lalu dibagi seimbang. Contoh: 10 mahasiswa, kapasitas 4 menjadi 3 kelompok berukuran 4, 3, 3. |
| K3 | Keseimbangan | Pada saat pembagian, selisih ukuran antar kelompok maksimal 1. Setelah diubah manual lewat menu 7, keseimbangan tidak dipaksa. |
| K4 | Penomoran arsip | Nomor baru = nomor terbesar yang ada di `output/` ditambah 1. `id_grouping` harus sama dengan nomor di nama file. |
| K5 | Menimpa arsip | Menu 5 tidak pernah menimpa arsip lama. Menu 7 dan 8 mengubah arsip yang dipilih pengguna di tempat. |
| K6 | Snapshot | Arsip menyimpan salinan nim dan nama saat pembagian. Perubahan data kerja sesudahnya tidak mengubah arsip. |
| K7 | Path | Program dijalankan dari folder utama proyek. README menjelaskan ini. |
| K8 | Cara lapor error | Fungsi logika tidak memakai `input()` atau `print()`. Kegagalan validasi dilaporkan dengan satu gaya yang sama di seluruh modul (disepakati tim sebelum mulai). |

## 7. Persyaratan fungsional

### Aturan data mahasiswa (menu 1 sampai 4)

- NIM disimpan sebagai teks. Spasi di awal dan akhir dibuang. Tidak boleh kosong, hanya boleh berisi angka (data nyata: 11 digit), dan harus unik.
- Nama: spasi di awal dan akhir dibuang, tidak boleh kosong. Nama yang sama antar mahasiswa boleh, karena identitas adalah NIM. Tanda petik dan titik diterima (contoh data: Mu'adz, L.S), dan kapitalisasi tidak diubah.
- NIM tidak bisa diubah lewat menu 3. Menu 3 hanya mengubah nama.
- Menu 4 meminta konfirmasi sebelum menghapus.
- Menu 2 menampilkan daftar bernomor, diurutkan sesuai urutan di file. Jika kosong, tampilkan pesan.
- Setiap perubahan langsung disimpan ke data kerja. Pesan sukses hanya muncul setelah penyimpanan berhasil.

### Bagi kelompok (menu 5)

1. Tolak jika mahasiswa kurang dari 2.
2. Pengguna memilih mode: jumlah kelompok, atau kapasitas maksimum per kelompok.
3. Mahasiswa diacak, lalu dibagi sesuai K2 dan K3.
4. Hasil ditampilkan, lalu disimpan sebagai arsip baru sesuai K4.
5. Nama file arsip ditampilkan. Jika penyimpanan gagal, tampilkan pesan gagal dan jangan klaim berhasil.

**Tabel kasus tepi pembagian** (dipakai juga sebagai tes):

| Mahasiswa | Mode | Input | Hasil |
| --- | --- | --- | --- |
| 10 | Jumlah kelompok | 3 | Diterima: 4, 3, 3 |
| 10 | Jumlah kelompok | 1 | Diterima: satu kelompok berisi 10 |
| 10 | Jumlah kelompok | 10 | Diterima: 10 kelompok masing-masing 1 |
| 10 | Jumlah kelompok | 11 | Ditolak: melebihi jumlah mahasiswa |
| 10 | Jumlah kelompok | 0 atau negatif atau bukan angka | Ditolak |
| 10 | Kapasitas | 4 | Diterima: 3 kelompok, 4, 3, 3 |
| 10 | Kapasitas | 5 | Diterima: 2 kelompok, 5 dan 5 |
| 10 | Kapasitas | 1 | Diterima: 10 kelompok masing-masing 1 |
| 10 | Kapasitas | 10 atau lebih | Diterima: satu kelompok berisi 10 |
| 10 | Kapasitas | 0 atau negatif atau bukan angka | Ditolak |
| 1 | Apa pun | Apa pun | Ditolak: mahasiswa kurang dari 2 |
| 2 | Jumlah kelompok | 2 | Diterima: 1 dan 1 |

**Data uji nyata:** file sumber berisi 37 mahasiswa (NIM 26110300001 sampai 26110300037). Hasil yang harus keluar:

| Mode | Input | Hasil |
| --- | --- | --- |
| Jumlah kelompok | 6 | 6 kelompok: 7, 6, 6, 6, 6, 6 |
| Kapasitas | 5 | 8 kelompok: 5, 5, 5, 5, 5, 4, 4, 4 |
| Kapasitas | 4 | 10 kelompok: tujuh berisi 4 dan tiga berisi 3 |
| Jumlah kelompok | 37 | 37 kelompok masing-masing 1 |
| Kapasitas | 37 atau lebih | 1 kelompok berisi 37 |
| Jumlah kelompok | 38 | Ditolak |

### Lihat kelompok (menu 6)

1. Tampilkan daftar arsip, diurutkan berdasarkan angka (arsip 2 sebelum arsip 10).
2. Jika belum ada arsip, tampilkan pesan dan kembali ke menu.
3. Pengguna memilih satu arsip, program menampilkan setiap kelompok dan anggotanya, beserta daftar "belum berkelompok" jika ada.
4. Jika satu arsip rusak, lewati dengan peringatan. Program tidak boleh crash.

### Ubah kelompok (menu 7)

1. Pengguna memilih arsip.
2. Pengguna memilih anggota yang akan dipindahkan (berdasarkan NIM) dan kelompok tujuan. Anggota boleh berasal dari kelompok mana pun atau dari daftar "belum berkelompok".
3. Tolak jika kelompok asal akan menjadi kosong (gunakan menu 8 untuk itu).
4. Tolak jika arsip memakai mode kapasitas dan kelompok tujuan akan melebihi kapasitas.
5. Simpan perubahan ke arsip itu. Tampilkan hasil singkat setelah berhasil.

### Hapus kelompok (menu 8, lanjutan)

1. Pengguna memilih arsip dan kelompok yang akan dihapus, lalu diminta konfirmasi.
2. Kelompok itu benar-benar dihapus dari file arsip.
3. Kelompok yang tersisa dinomori ulang mulai dari 1 tanpa celah, dan `jumlah_kelompok` diperbarui. Contoh: ada 5 kelompok, kelompok 4 dihapus, sisanya menjadi kelompok 1 sampai 4.
4. Anggota kelompok yang dihapus masuk daftar "belum berkelompok" di arsip yang sama, dan daftar itu ditampilkan ke pengguna.
5. Pengguna memilih cara menempatkan mereka: manual (dipindahkan satu per satu lewat menu 7) atau otomatis (disebar ke kelompok yang ada dengan aturan keseimbangan K3).

## 8. Format file

**Data mahasiswa (sumber dan kerja):** daftar objek berisi `nim` (teks) dan `nama` (teks).

**Arsip pembagian:** satu objek berisi `id_grouping`, `mode_pembagian` (`jumlah_kelompok` atau `kapasitas`), `jumlah_kelompok`, `kapasitas_anggota` (angka atau kosong), `kelompok` (daftar berisi `nomor_kelompok` dan `anggota` berisi pasangan `nim` dan `nama`), dan `belum_berkelompok` (daftar anggota, kosong secara bawaan).

## 9. Rencana pengujian

Setiap fitur diuji manual oleh minimal satu anggota selain pembuatnya. Daftar tes:

- [ ] File sumber tidak berubah setelah semua operasi menu 1 sampai 4.
- [ ] Data yang ditambah, diubah, dan dihapus tetap ada setelah program ditutup dan dibuka lagi.
- [ ] NIM kosong, NIM duplikat, dan nama kosong ditolak tanpa mengubah data.
- [ ] Semua baris pada tabel kasus tepi (bagian 7) menghasilkan hasil yang tertulis.
- [ ] Setiap mahasiswa muncul tepat sekali di hasil pembagian.
- [ ] Dua kali bagi menghasilkan dua arsip dengan nomor berbeda. Jika arsip bernomor tengah dihapus manual, arsip baru tetap tidak menimpa apa pun.
- [ ] Daftar arsip terurut angka. Satu arsip yang sengaja dirusak tidak membuat program crash.
- [ ] Menu 7: pemindahan berhasil, ditolak jika kelompok asal jadi kosong, ditolak jika melebihi kapasitas.
- [ ] Menu 8: anggota masuk ke "belum berkelompok", nomor kelompok terurut ulang, jumlah kelompok benar.
- [ ] Pilihan menu yang tidak valid di semua layar tidak membuat program crash.
- [ ] Skenario demo utama (bagian 2) berhasil dijalankan dari awal sampai akhir.

## 10. Pembagian kerja dan urutan

| Modul | Isi | Pemegang |
| --- | --- | --- |
| `grouping.py` | Validasi parameter, pengacakan, algoritma pembagian | Azzam |
| `riwayat.py` | Penomoran dan penyimpanan arsip, baca arsip, ubah kelompok (menu 7), hapus kelompok (menu 8, lanjutan) | Azzam |
| `mahasiswa.py` | Muat data dari file sumber, simpan, tambah, ubah, hapus mahasiswa (menu 1 sampai 4) | Anggota A |
| `main.py` | Menu, navigasi, validasi input angka, tampilan daftar arsip dan isi kelompok (menu 6) | Anggota B |

Prioritas: tahap 1 (menu 5, 6, lalu 7), tahap 2 (menu 1 sampai 4), lalu lanjutan (menu 8). Tahap 1 dan 2 dikerjakan paralel oleh orang berbeda. Azzam menulis lembar tugas tiap anggota (input, output, kasus uji), dan sebelum mulai tim menyepakati satu halaman kontrak antar modul: nama fungsi, masukan, keluaran, dan cara lapor error (K8).

## 11. Risiko

| Risiko | Penanganan |
| --- | --- |
| Tiga orang membuat format data berbeda | Kontrak antar modul disepakati sebelum coding |
| Azzam jadi penghambat karena logika inti dipegang satu orang | Tugas anggota lain dibuat paralel dan tidak menunggu logika inti, dengan kontrak antar modul sebagai pegangan |
| Program mati saat menulis file dan merusak data | Ditolak: mahasiswa kurang dari 2Diterima sebagai risiko MVP. Ditangani di fase lanjutan |
| Aturan pembagian ditafsirkan berbeda | Tabel kasus tepi menjadi acuan tunggal |

## 12. Kontrak antar modul

Semua orang membaca bagian ini sebelum mulai. Kalau ada yang mau diubah, bilang ke Azzam dulu supaya tiga modul tetap cocok saat digabung.

**Bentuk data mahasiswa di memori:** daftar, tiap item berisi `nim` (teks) dan `nama` (teks). Sama persis dengan file JSON.

**Bentuk arsip:** sesuai bagian 8.

**Cara lapor error (K8):** fungsi yang gagal validasi melempar `ValueError` dengan pesan berbahasa Indonesia yang siap ditampilkan. `main.py` menangkapnya lalu mencetak pesan itu. Fungsi di `mahasiswa.py`, `grouping.py`, dan `riwayat.py` tidak memakai `input()` atau `print()`.

| Modul | Fungsi (nama usulan) | Masukan | Keluaran |
| --- | --- | --- | --- |
| `mahasiswa.py` | `muat_mahasiswa` | tidak ada | daftar mahasiswa |
| `mahasiswa.py` | `simpan_mahasiswa` | daftar mahasiswa | tidak ada |
| `mahasiswa.py` | `tambah_mahasiswa` | daftar, nim, nama | daftar yang diperbarui |
| `mahasiswa.py` | `ubah_nama` | daftar, nim, nama baru | daftar yang diperbarui |
| `mahasiswa.py` | `hapus_mahasiswa` | daftar, nim | daftar yang diperbarui |
| `grouping.py` | `bagi_per_jumlah` | daftar, jumlah kelompok | daftar kelompok (tiap kelompok = daftar mahasiswa) |
| `grouping.py` | `bagi_per_kapasitas` | daftar, kapasitas | daftar kelompok |
| `riwayat.py` | `simpan_arsip` | hasil pembagian, mode, parameter | nomor arsip baru |
| `riwayat.py` | `daftar_arsip` | tidak ada | daftar nomor arsip, terurut angka, arsip rusak dilewati |
| `riwayat.py` | `baca_arsip` | nomor arsip | isi arsip |
| `riwayat.py` | `pindahkan_anggota` | nomor arsip, nim, nomor kelompok tujuan | tidak ada |

Semua fungsi yang gagal melempar `ValueError` dengan pesan yang jelas.

## 13. Lembar tugas

Tiap tugas selesai kalau semua kasus uji di bawahnya lulus dan satu anggota lain sudah mencobanya dari menu.

### Anggota A: `mahasiswa.py` (menu 1 sampai 4)

**Yang dibuat:** fungsi pada tabel kontrak untuk `mahasiswa.py`.

**Aturan:**

- Muat: jika `mahasiswa-kerja.json` ada, baca itu. Jika tidak, baca file sumber. File sumber tidak pernah ditulis.
- Simpan: selalu ke `mahasiswa-kerja.json`.
- NIM: spasi ujung dibuang, tidak kosong, hanya angka, unik.
- Nama: spasi ujung dibuang, tidak kosong. Karakter lain dan kapitalisasi dibiarkan.
- File tidak ada, JSON rusak, atau struktur salah: lempar `ValueError` dengan pesan jelas, jangan menimpa file.

**Kasus uji:**

| Aksi | Hasil yang benar |
| --- | --- |
| Muat data pertama kali | 37 mahasiswa, file kerja belum ada |
| Tambah NIM `26110300018` | Ditolak, NIM sudah dipakai |
| Tambah NIM `abc` | Ditolak, bukan angka |
| Tambah NIM kosong atau nama berisi spasi saja | Ditolak, data tidak berubah |
| Tambah NIM `26110300038` dengan nama `Budi` | Berhasil, jadi 38 mahasiswa |
| Ubah nama NIM `26110300006` | Nama berubah, NIM tetap |
| Ubah nama NIM yang tidak ada | Ditolak |
| Hapus NIM yang ada | Berhasil, jadi satu lebih sedikit |
| Tutup dan jalankan ulang program | Perubahan masih ada |
| Cek file sumber setelah semua tes | Isinya tidak berubah |

### Anggota B: `main.py` (menu, navigasi, tampilan)

**Yang dibuat:** menu utama, loop yang berjalan sampai pilihan `0`, pemanggilan fungsi modul lain, penangkapan `ValueError`, tampilan daftar mahasiswa, daftar arsip, dan isi kelompok.

**Aturan:**

- Pilihan menu bukan angka atau di luar menu: tampilkan pesan, ulangi menu.
- Input jumlah kelompok dan kapasitas: tolak nol, negatif, desimal, dan bukan angka.
- Di tiap langkah input, `0` membatalkan dan kembali ke menu.
- Tampilan daftar mahasiswa bernomor sesuai urutan file. Tampilan kelompok memuat nomor kelompok dan anggotanya (NIM dan nama).
- Pesan sukses hanya muncul setelah fungsi modul berhasil tanpa error.

**Kasus uji:**

| Aksi | Hasil yang benar |
| --- | --- |
| Menu: ketik `abc`, `9`, kosong | Pesan salah, menu muncul lagi, program tidak crash |
| Menu: ketik `0` | Program keluar |
| Jumlah kelompok: `0`, `-1`, `3.5`, `abc` | Ditolak dengan pesan |
| Input apa pun lalu ketik `0` | Kembali ke menu tanpa mengubah data |
| Lihat kelompok saat belum ada arsip | Pesan, kembali ke menu |
| Lihat kelompok, pilih nomor arsip yang tidak ada | Pesan, kembali ke menu |
| Lihat kelompok, pilih arsip yang valid | Semua kelompok dan anggotanya tampil |

### Azzam: `grouping.py` dan `riwayat.py` (menu 5, 6 sisi data, 7)

**Yang dibuat:** dua mode pembagian, penomoran dan penyimpanan arsip, daftar dan pembacaan arsip, pemindahan anggota.

**Kasus uji:** tabel kasus tepi dan data uji nyata pada bagian 7, ditambah:

| Aksi | Hasil yang benar |
| --- | --- |
| Bagi dua kali berturut-turut | Arsip 1 dan arsip 2, tidak saling menimpa |
| Hapus arsip 1 manual lalu bagi lagi | Arsip baru bernomor 3 |
| Dua arsip lalu 10 arsip | Daftar terurut angka, arsip 2 sebelum arsip 10 |
| Satu arsip dirusak manual | Dilewati dengan peringatan, program tidak crash |
| Pindah anggota ke kelompok yang ada | Anggota hanya ada di kelompok tujuan |
| Pindah anggota yang membuat kelompok asal kosong | Ditolak |
| Pindah ke kelompok penuh pada arsip mode kapasitas | Ditolak |
| Setiap mahasiswa pada hasil pembagian | Muncul tepat sekali |
