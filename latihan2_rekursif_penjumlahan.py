def jumlah_rekursif(n):
    # Base case: S(1) = 1
    if n == 1:
        return 1
    # Rekursif: S(n) = n + S(n-1)
    return n + jumlah_rekursif(n - 1)


if __name__ == "__main__":
    n = int(input("Masukkan nilai n: "))
    if n < 1:
        print("Masukkan bilangan bulat positif (n >= 1).")
    else:
        hasil = jumlah_rekursif(n)
        print(f"Hasil penjumlahan 1 sampai {n} = {hasil}")