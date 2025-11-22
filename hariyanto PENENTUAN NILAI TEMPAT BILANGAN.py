# Program Penentuan Nilai Tempat Bilangan hariyanto

try:
    n = input("Masukkan angkanya: ").strip()

    if not n.isdigit():
        print("Input harus berupa angka!")
    else:
        nilai = int(n)

        if 0 <= nilai <= 999999999999:

            # Daftar nilai tempat
            tempat = [
                (1000000, "Jutaan"),
                (100000,  "Ratusan Ribu"),
                (10000,   "Puluhan Ribu"),
                (1000,    "Ribuan"),
                (100,     "Ratusan"),
                (10,      "Puluhan"),
                (1,       "Satuan")
            ]

            print("\n==============================")
            print("  HASIL PEMECAHAN ANGKA")
            print("==============================")

            sisa = nilai

            for pembagi, nama in tempat:
                hasil = sisa // pembagi
                sisa = sisa % pembagi

                if nilai >= pembagi:
                    print(f"{nama:<15}: {hasil}")

            print("==============================")
            print("Pemecahan angka selesai!\n")

        else:
            print("Angka di luar batas yang ditentukan!")

except ValueError:
    print("Terjadi kesalahan! Masukkan angka yang valid.")

