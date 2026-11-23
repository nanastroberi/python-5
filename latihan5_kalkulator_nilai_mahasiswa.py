def hitung_rata_rata(tugas, uts, uas):
    return (tugas + uts + uas) / 3


def cek_grade(rata_rata):
    if rata_rata >= 85:
        return "A"
    elif rata_rata >= 75:
        return "B"
    elif rata_rata >= 65:
        return "C"
    elif rata_rata >= 60:
        return "D"
    else:
        return "E"


def cek_kelulusan(rata_rata):
    if rata_rata >= 60:
        return "LULUS"
    else:
        return "TIDAK LULUS"


def uji_skenario():
    # Skenario 1: Contoh dari modul (Andi: 80, 75, 90 -> 81.67, B, LULUS)
    rata1 = hitung_rata_rata(80, 75, 90)
    assert round(rata1, 2) == 81.67
    assert cek_grade(rata1) == "B"
    assert cek_kelulusan(rata1) == "LULUS"

    # Skenario 2: Nilai sangat baik (Grade A, LULUS)
    rata2 = hitung_rata_rata(90, 88, 92)
    assert cek_grade(rata2) == "A"
    assert cek_kelulusan(rata2) == "LULUS"

    # Skenario 3: Nilai cukup (Grade C, LULUS)
    rata3 = hitung_rata_rata(70, 68, 72)
    assert cek_grade(rata3) == "C"
    assert cek_kelulusan(rata3) == "LULUS"

    # Skenario 4: Batas minimal lulus (Grade D, LULUS)
    rata4 = hitung_rata_rata(60, 60, 60)
    assert cek_grade(rata4) == "D"
    assert cek_kelulusan(rata4) == "LULUS"

    # Skenario 5: Di bawah batas lulus (Grade E, TIDAK LULUS)
    rata5 = hitung_rata_rata(50, 55, 58)
    assert cek_grade(rata5) == "E"
    assert cek_kelulusan(rata5) == "TIDAK LULUS"


def main():
    nama = input("Nama mahasiswa: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    rata_rata = hitung_rata_rata(tugas, uts, uas)
    grade = cek_grade(rata_rata)
    status = cek_kelulusan(rata_rata)

    print()
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Grade: {grade}")
    print(f"Status: {status}")


if __name__ == "__main__":
    uji_skenario()
    main()