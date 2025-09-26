import random

def main():
    #! Dapatkan angka acak dari 1 - 10
    angka_acak = random.randint(1, 10)
    print("Tebak Angka, coba tebak angka dari 1 - 10 (Kesempatan 5x)")

    #! Cek kalau user tekan (CTRL + C) agar tidak ada error
    try:

        #! Looping dari 1 - 6, atau 5x, Bisa juga 0 - 5, itu 5x juga
        #! Tapi biar mudah di hitung pakai 1 - 6
        for count in range(1, 6):

            #! Cek apakah user memasukkan input selain angka
            try:

                #! Ambil tebakan dari user
                user_input = int(input("Masukkan Tebakan: "))

                #! Jika Jawaban Benar
                if user_input == angka_acak:
                    print(f"Tebakan Benar! {angka_acak}")

                    #! Looping Dihentikan, program selesai
                    break

                #! Jika tebakan salah tapi lebih besar
                elif user_input > angka_acak:
                    print(f"Terlalu besar!. Kesempatan tinggal {5 - count}")
                
                #! Jika tebakan salah tapi lebih kecil
                elif user_input < angka_acak:
                    print(f"Terlalu Kecil!. Kesempatan tinggal {5 - count}")
                
                # Jika kesempatan habis, beritahu jawaban yang benar
                if count == 5:
                    print(f"Kesempatan Habis!... Jawaban Yang Benar: {angka_acak}")

            except ValueError:
                #! Jika bukan angka
                print("Hanya Boleh Angka")

    except KeyboardInterrupt:
        #! Jika CTRL + C
        print("\nPaksa Berhenti!")

# Eksekusi program
if __name__ == "__main__":
    main()