import time

def tampilkan_petunjuk():
    print("=" * 40)
    print("🚀 Selamat datang di Game Hecker Lamer v2 🚀")
    print("=" * 40)
    print("Aturan permainan:")
    print("1. Jawab 10 pertanyaan dengan benar untuk membuktikan kamu seorang hecker sejati.")
    print("2. Setiap jawaban benar bernilai 10 poin.")
    print("3. Kamu punya **10 detik** untuk menjawab setiap soal.")
    print("4. Salah menjawab? Kamu mendapat satu kesempatan ulang.")
    print("Ketik huruf jawaban (a, b, c, d) untuk memilih.")
    print("=" * 40)

def tampilkan_soal(soal, jawaban_benar):
    kesempatan = 2
    while kesempatan > 0:
        print("\n" + soal['pertanyaan'])
        for opsi in soal['opsi']:
            print(opsi)
        
        # Timer untuk jawaban
        start_time = time.time()
        jawaban = input("Jawaban Anda (a/b/c/d): ").lower()
        elapsed_time = time.time() - start_time

        if elapsed_time > 10:
            print("⏰ Waktu habis! Jawaban tidak dihitung.")
            return 0
        elif jawaban == jawaban_benar:
            print("✅ Benar!")
            return 10
        else:
            kesempatan -= 1
            if kesempatan > 0:
                print("❌ Salah! Coba lagi.")
            else:
                print(f"❌ Salah! Jawaban yang benar adalah {jawaban_benar.upper()}.")

    return 0

# Daftar soal dan jawaban
daftar_soal = [
    {"pertanyaan": "1. Apa singkatan dari CPU?", "opsi": ["a. Central Programming Unit", 
                                                          "b. Central Processing Unit", 
                                                          "c. Central Power Unit", 
                                                          "d. Central Protocol Unit"], "jawaban": "b"},
    {"pertanyaan": "2. Apa fungsi dari RAM?", "opsi": ["a. Penyimpanan permanen", 
                                                       "b. Memori sementara", 
                                                       "c. Memproses data grafis", 
                                                       "d. Menghubungkan perangkat keras"], "jawaban": "b"},
    {"pertanyaan": "3. Apa perintah Linux untuk membuat direktori?", "opsi": ["a. mkdir", 
                                                                              "b. cd", 
                                                                              "c. rmdir", 
                                                                              "d. ls"], "jawaban": "a"},
    {"pertanyaan": "4. Siapa penemu Python?", "opsi": ["a. Guido van Rossum", 
                                                       "b. Dennis Ritchie", 
                                                       "c. James Gosling", 
                                                       "d. Linus Torvalds"], "jawaban": "a"},
    {"pertanyaan": "5. Port default untuk HTTP adalah?", "opsi": ["a. 21", 
                                                                  "b. 22", 
                                                                  "c. 80", 
                                                                  "d. 443"], "jawaban": "c"},
    {"pertanyaan": "6. Dalam sistem biner, angka 10 adalah?", "opsi": ["a. 1", 
                                                                       "b. 2", 
                                                                       "c. 3", 
                                                                       "d. 4"], "jawaban": "b"},
    {"pertanyaan": "7. Apa nama protokol yang digunakan untuk email?", "opsi": ["a. FTP", 
                                                                               "b. HTTP", 
                                                                               "c. SMTP", 
                                                                               "d. SNMP"], "jawaban": "c"},
    {"pertanyaan": "8. Bahasa pemrograman apa yang paling sering digunakan untuk *web development*?", "opsi": ["a. C++", 
                                                                                                               "b. Python", 
                                                                                                               "c. JavaScript", 
                                                                                                               "d. Java"], "jawaban": "c"},
    {"pertanyaan": "9. Apa itu IP Address?", "opsi": ["a. Identitas komputer di jaringan", 
                                                      "b. Protokol untuk keamanan data", 
                                                      "c. Nama domain internet", 
                                                      "d. Alat untuk mengirim data"], "jawaban": "a"},
    {"pertanyaan": "10. Apa kegunaan Git?", "opsi": ["a. Membuat aplikasi", 
                                                     "b. Mengelola versi kode", 
                                                     "c. Debugging program", 
                                                     "d. Menganalisis data"], "jawaban": "b"}
]

def main():
    tampilkan_petunjuk()
    skor = 0

    for soal in daftar_soal:
        skor += tampilkan_soal(soal, soal['jawaban'])

    print("\nGame selesai!")
    print(f"Skor Anda: {skor}/100")
    if skor == 100:
        print("🎉 Selamat! Kamu adalah seorang hecker sejati!")
    elif skor >= 70:
        print("👍 Bagus! Kamu memiliki potensi menjadi hecker.")
    elif skor >= 40:
        print("🙂 Lumayan, tapi masih butuh belajar.")
    else:
        print("😅 Terus belajar, lamer!")

if __name__ == "__main__":
    main()