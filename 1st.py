def penjumlahan(x, y):
    return x + y


def pengurangan(x, y):
    return x - y


def perkalian(x, y):
    return x * y


def pembagian(x, y):
    if y == 0:
        return "Error! Pembagian oleh nol tidak dapat dilakukan."
    else:
        return x / y


while True:
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi yang ingin Anda lakukan:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan in ('1', '2', '3', '4'):
        bilangan1 = float(input("Masukkan bilangan pertama: "))
        bilangan2 = float(input("Masukkan bilangan kedua: "))

        if pilihan == '1':
            print("Hasil penjumlahan:", penjumlahan(bilangan1, bilangan2))
        elif pilihan == '2':
            print("Hasil pengurangan:", pengurangan(bilangan1, bilangan2))
        elif pilihan == '3':
            print("Hasil perkalian:", perkalian(bilangan1, bilangan2))
        elif pilihan == '4':
            print("Hasil pembagian:", pembagian(bilangan1, bilangan2))

        ulangi = input("\nApakah Anda ingin melanjutkan? (ya/tidak): ")
        if ulangi.lower() != 'ya':
            break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")