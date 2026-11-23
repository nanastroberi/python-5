"""
Latihan 3 — Debugging (Jawaban Pertanyaan):
1. Apakah terdapat syntax error?
   Tidak terdapat syntax error (program dapat dijalankan tanpa error sintaks).
2. Apakah terdapat logic error?
   Ya, terdapat logic error pada rumus luas segitiga:
   menggunakan operator '+' (alas + tinggi / 2) seharusnya '*' ((alas * tinggi) / 2).
3. Berapa output program sebelum diperbaiki?
   Luas: 14.0  (karena 8 / 2 = 4.0, lalu 10 + 4.0 = 14.0)
4. Bagaimana perbaikannya?
   Ubah baris `luas = alas + tinggi / 2` menjadi `luas = (alas * tinggi) / 2`.
5. Berapa output yang seharusnya?
   Luas: 40.0  (karena (10 * 8) / 2 = 40.0)
"""


def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    return luas


if __name__ == "__main__":
    hasil = luas_segitiga(10, 8)
    print("Luas:", hasil)