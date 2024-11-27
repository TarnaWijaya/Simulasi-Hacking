import random
import time
import sys

def animasi_tulisan(teks, delay=0.03):
    """Menampilkan teks dengan animasi."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def tampilkan_petunjuk():
    print("=" * 50)
    animasi_tulisan("🎮 Selamat Datang di Game Hecker Lamer (V4) 🎮")
    print("=" * 50)
    animasi_tulisan("📜 Peraturan:")
    animasi_tulisan("1. Jawab 10 pertanyaan untuk membuktikan diri sebagai hecker sejati.")
    animasi_tulisan("2. Setiap jawaban benar bernilai 10 poin.")
    animasi_tulisan("3. Kamu memiliki 3 nyawa. Jawaban salah akan mengurangi nyawa.")
    animasi_tulisan("4. Pilih level kesulitan: Mudah, Sedang, atau Sulit.")
    print("=" * 50)

def pilih_level():
    print("\n🔰 Pilih Level Kesulitan:")
    print("1. Mudah (Soal Umum)")
    print("2. Sedang (Soal Intermediate)")
    print("3. Sulit (Soal Lanjutan)")
    pilihan = input("Masukkan nomor level (1/2/3): ").strip()
    if pilihan in ["1", "2", "3"]:
        return int(pilihan)
    else:
        print("❌ Pilihan tidak valid! Default ke 'Mudah'.")
        return 1

def tampilkan_soal(soal, jawaban_benar, nyawa):
    print("\n📝 " + soal['pertanyaan'])
    for opsi in soal['opsi']:
        print(opsi)
    jawaban = input("⚡ Jawaban Anda (a/b/c/d): ").lower()
    if jawaban == jawaban_benar:
        animasi_tulisan("✅ Benar!")
        return 10, nyawa
    else:
        animasi_tulisan(f"❌ Salah! Jawaban yang benar adalah {jawaban_benar.upper()}.")
        return 0, nyawa - 1

# Kumpulan soal berdasarkan level
soal_mudah = [
    {"pertanyaan": "1. Apa singkatan dari WWW?", 
     "opsi": ["a. World Wide Web", "b. Wide World Web", "c. Web World Wide", "d. World Web Wide"], 
     "jawaban": "a"},
    {"pertanyaan": "2. Perangkat penyimpanan yang bersifat permanen adalah?", 
     "opsi": ["a. RAM", "b. ROM", "c. CPU", "d. GPU"], 
     "jawaban": "b"}
]

soal_sedang = [
    {"pertanyaan": "1. Port default untuk HTTPS adalah?", 
     "opsi": ["a. 22", "b. 80", "c. 443", "d. 8080"], 
     "jawaban": "c"},
    {"pertanyaan": "2. Apa fungsi utama dari database?", 
     "opsi": ["a. Menyimpan data", "b. Memproses data", "c. Menghapus data", "d. Menganalisis data"], 
     "jawaban": "a"}
]

soal_sulit = [
    {"pertanyaan": "1. Algoritma enkripsi yang menggunakan kunci publik dan privat adalah?", 
     "opsi": ["a. RSA", "b. MD5", "c. SHA-256", "d. AES"], 
     "jawaban": "a"},
    {"pertanyaan": "2. Apa itu Docker?", 
     "opsi": ["a. Alat untuk mengelola container", "b. Protokol jaringan", 
              "c. Bahasa pemrograman", "d. Sistem operasi"], 
     "jawaban": "a"}
]

# Pilihan soal berdasarkan level
level_soal = {
    1: soal_mudah,
    2: soal_sedang,
    3: soal_sulit
}

def main():
    tampilkan_petunjuk()
    skor = 0
    nyawa = 3

    # Memilih level kesulitan
    level = pilih_level()
    soal_terpilih = random.sample(level_soal[level], 2)  # Mengambil 2 soal sesuai level

    for index, soal in enumerate(soal_terpilih):
        print(f"\n🔹 Soal {index + 1} (Nyawa: {nyawa})")
        poin, nyawa = tampilkan_soal(soal, soal['jawaban'], nyawa)
        skor += poin

        if nyawa <= 0:
            animasi_tulisan("\n💀 Kamu kehabisan nyawa! Game over!")
            print(f"Skor akhir Anda: {skor}/20")
            return

    print("\n🎮 Game selesai!")
    print(f"🎯 Skor Anda: {skor}/20")
    if skor == 20:
        animasi_tulisan("🏆 Luar biasa! Kamu adalah seorang hecker sejati!")
    elif skor >= 10:
        animasi_tulisan("✨ Hebat! Kamu punya potensi jadi hecker!")
    else:
        animasi_tulisan("💡 Terus belajar, lamer!")

if __name__ == "__main__":
    main()