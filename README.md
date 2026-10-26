# System Pembagi Kelompok CLI

Bagi daftar mahasiswa ke dalam kelompok secara acak, simpan setiap hasil sebagai arsip,
lalu ubah hasilnya tanpa mengulang dari nol. Python murni, tanpa library pihak ketiga.

> Dokumen ini versi Markdown. Versi tampilan web ada di
> [README.html](README.html) — buka di browser untuk tampilan penuh.

## Ringkasan

Membagi kelompok secara manual memakan waktu dan sering dianggap tidak adil. Kalau ada
perubahan — mahasiswa pindah, kelompok dibubarkan — hasilnya harus dibuat ulang dari awal.
Program ini mengacak pembagian, menyimpan setiap hasil sebagai arsip, dan memungkinkan
hasil itu diubah di tempat.

## Fitur

| # | Menu | Fungsi | Keterangan |
|---|---|---|---|
| 1 | Bagi kelompok | `grouping_data()` | Acak lalu bagi per kapasitas tetap (3, 4, atau 6 anggota) |
| 2 | Lihat Kelompok | `show_group()` | Pilih arsip, pilih nomor kelompok, lihat anggota |
| 3 | Hapus Kelompok | `remove_group()` | Nomor kelompok sisanya diurut ulang tanpa celah |
| 4 | Ubah Kelompok | `update_group()` | Ganti nama/NIM anggota; NIM duplikat ditolak |
| 0 | Keluar | `break` | Akhiri program |

## Instalasi

```bash
git clone https://github.com/AZZAMAF/System-Pembagi-Kelompok-CLI.git
cd System-Pembagi-Kelompok-CLI
python3 main.py
```

Tidak perlu `pip install` — hanya modul bawaan (`json`, `random`).

**Penting:** jalankan dari folder utama proyek, bukan dari dalam `Code/`.
Path `data/...` di dalam kode bersifat relatif.

## Struktur file

```text
Final_Project_CLI/
├── main.py                  menu utama + routing pilihan
├── Code/
│   ├── grouping.py          bagi, lihat, hapus, ubah kelompok
│   ├── menu.py              cetak menu dari JSON
│   └── processor_json.py    pembaca file JSON
├── data/
│   ├── mahasiswa-cs.json    36 mahasiswa (sumber, tidak pernah ditulis)
│   ├── menu-list.json       label menu
│   └── Output/              arsip hasil pembagian
└── Docs/                    PRD, brainstorming, panduan git
```

Catatan: `grouping.py` membaca `data/mahasiswa-cs.json` di level modul. Kalau file itu
diubah di luar program, perubahan baru terbaca setelah program dijalankan ulang.

## Format data

**`data/mahasiswa-cs.json`** — list of object:

```json
{ "nim": "26110300018", "nama": "Abdullah Azzam Firdaus" }
```

**`data/Output/<nama>.json`** — list of object:

```json
{
  "group": 1,
  "members": [
    { "nim": "26110300001", "nama": "Anugrah Yusuf Rekimsa" }
  ]
}
```

NIM disimpan sebagai teks supaya angka nol di depan tidak hilang.

## Status

Sudah jalan:

- Bagi kelompok per kapasitas tetap (3, 4, 6)
- Lihat kelompok
- Hapus kelompok + nomor diurut ulang
- Ubah nama/NIM anggota dengan cek duplikat

Belum dikerjakan (masih di PRD v5):

- Mode pembagian per **jumlah kelompok** — saat ini hanya kapasitas
- Menu kelola mahasiswa (tambah, lihat, ubah, hapus) — belum ada `mahasiswa.py`
- Validasi input angka — `int(input())` tanpa `try/except`, huruf/desimal membuat program berhenti
- Penomoran arsip otomatis — nama file diketik bebas, arsip lama bisa tertimpa
- Modul `riwayat.py` + skema arsip PRD (`id_grouping`, `mode_pembagian`, `belum_berkelompok`)
- Anggota tanpa kelompok setelah penghapusan

## Tim

UAS Programming 1 — Cakrawala University, Kelompok 1.

| Nama | NIM | Peran |
|---|---|---|
| Abdullah Azzam Firdaus | 26110300018 | show menu, Create group, Update Group |
| Ubay Abdillah | 26110300020 | Show group |
| M Fahmi Ramadhan | 26110300035 | Delete group · testing |
