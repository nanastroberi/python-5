def penjumlahan(a, b):
    return a + b


def pengurangan(a, b):
    return a - b


def perkalian(a, b):
    return a * b


def pembagian(a, b):
    if b == 0:
        return "Error: Tidak dapat membagi dengan nol"
    return a / b


if __name__ == "__main__":
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))

    print()
    print("Penjumlahan:", penjumlahan(a, b))
    print("Pengurangan:", pengurangan(a, b))
    print("Perkalian:", perkalian(a, b))
    print("Pembagian:", pembagian(a, b))