def cek_genap_ganjil(n):
    if n % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"


if __name__ == "__main__":
    # Pengujian menggunakan minimal 5 pernyataan assert
    assert cek_genap_ganjil(2) == "Genap"
    assert cek_genap_ganjil(5) == "Ganjil"
    assert cek_genap_ganjil(0) == "Genap"
    assert cek_genap_ganjil(100) == "Genap"
    assert cek_genap_ganjil(-3) == "Ganjil"

    print("Semua pengujian assert berhasil!")
