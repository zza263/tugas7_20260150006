import modul_evaluasi


def input_angka_valid(prompt, min_val, max_val):
    """Meminta input angka (float) dalam rentang min_val sampai max_val.
    Program tidak akan crash jika pengguna memasukkan teks."""
    while True:
        try:
            nilai = float(input(prompt))
            if nilai < min_val or nilai > max_val:
                print(f"  [Warning] Angka harus di antara {min_val:g} dan {max_val:g}. Coba lagi.")
                continue
            return nilai
        except ValueError:
            print("  [Error] Input harus berupa angka, bukan huruf/teks. Coba lagi.")


def proses_kelayakan():
    """Mengambil data dari pengguna lalu menampilkan hasil evaluasi."""
    print("\n--- Input Data Calon Asisten Laboratorium ---")
    nama = input("Nama                       : ").strip()
    nim = input("NIM                        : ").strip()
    hadir = input_angka_valid("Jumlah kehadiran (0-14)   : ", 0, 14)
    tugas = input_angka_valid("Nilai Tugas (0-100)       : ", 0, 100)
    ucp1 = input_angka_valid("Nilai UCP 1 (0-100)       : ", 0, 100)
    ucp2 = input_angka_valid("Nilai UCP 2 (0-100)       : ", 0, 100)

    persentase = modul_evaluasi.hitung_presentase_presentasi(hadir)
    nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
    status = modul_evaluasi.cek_kelayakan_aslab(persentase, nilai_akhir)

    print("\n" + "=" * 45)
    print("       HASIL EVALUASI KELAYAKAN ASLAB")
    print("=" * 45)
    print(f"Nama                : {nama}")
    print(f"NIM                 : {nim}")
    print(f"Kehadiran           : {hadir:g} dari 14 pertemuan")
    print(f"Persentase Presensi : {persentase:.2f}%")
    print(f"Nilai Tugas         : {tugas:g}")
    print(f"Nilai UCP 1         : {ucp1:g}")
    print(f"Nilai UCP 2         : {ucp2:g}")
    print(f"Nilai Akhir         : {nilai_akhir:.2f}")
    print("-" * 45)
    print(f"STATUS              : {status}")
    print("=" * 45)


def main():
    while True:
        print("\n=== SISTEM EVALUASI KELAYAKAN ASISTEN LAB AI ===")
        print("1. Hitung Kelayakan")
        print("2. Keluar")
        try:
            pilihan = int(input("Pilih menu (1/2): "))
        except ValueError:
            print("  [Error] Pilihan menu harus berupa angka 1 atau 2.")
            continue

        if pilihan == 1:
            proses_kelayakan()
        elif pilihan == 2:
            print("Terima kasih. Program selesai.")
            break
        else:
            print("  [Warning] Pilihan tidak tersedia. Pilih 1 atau 2.")


if __name__ == "__main__":
    main()