# Tugas Refactoring SOLID - Sistem Registrasi Mahasiswa

## Deskripsi Tugas
Repository ini berisi implementasi refactoring kode sistem registrasi mahasiswa untuk memenuhi prinsip SOLID, khususnya SRP, OCP, dan DIP.

## Struktur File
| Nama File | Penjelasan |
| :--- | :--- |
| `sebelum_refactoring.py` | Kode awal yang melanggar prinsip SOLID (God Class). |
| `sesudah_refactoring.py` | Kode hasil perbaikan menggunakan Abstraksi dan Dependency Injection. |
| `order_solid.py` | Latihan praktikum (kasus Order). |

## Analisis SOLID

### 1. Masalah pada Kode Lama (Code Smell)
Pada `sebelum_refactoring.py`, terdapat kelas `SistemRegistrasi` yang melakukan terlalu banyak tugas:
- **Pelanggaran SRP (Single Responsibility Principle):** Satu kelas mengurus validasi SKS, validasi Prasyarat, dan logika persetujuan sekaligus.
- **Pelanggaran OCP (Open/Closed Principle):** Menggunakan logika kondisional (`if/else`) yang menyatu dengan kode utama. Jika ingin menambah validasi baru, kita harus memodifikasi kelas tersebut.

### 2. Solusi Refactoring
Pada `sesudah_refactoring.py`, kode dipecah menjadi bagian modular:
- **Penerapan DIP (Dependency Inversion Principle):** Dibuat interface `IValidationRule` sebagai kontrak. `RegistrationService` tidak bergantung pada kelas konkret, tapi pada abstraksi.
- **Penerapan SRP:** Setiap aturan validasi (`SksLimitRule`, `PrerequisiteRule`) dipisah menjadi kelas sendiri.
- **Penerapan OCP:** Menggunakan **Dependency Injection**. `RegistrationService` menerima daftar aturan dari luar melalui constructor.

### 3. Pembuktian Challenge
Sesuai instruksi tugas, ditambahkan kelas baru `JadwalBentrokRule`. Aturan ini berhasil disuntikkan ke dalam sistem tanpa mengubah satu baris pun kode pada `RegistrationService`, membuktikan sistem sudah fleksibel (Open for Extension).
