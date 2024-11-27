import random
import time

def tampilkan_petunjuk():
    print("=" * 50)
    print("💻 Selamat Datang di Game Hecker Lamer (V3) 💻")
    print("=" * 50)
    print("📜 Peraturan:")
    print("1. Jawab 10 pertanyaan untuk membuktikan kamu seorang hecker sejati.")
    print("2. Jawaban benar bernilai 10 poin.")
    print("3. Jawab dengan cepat (<5 detik) untuk mendapatkan bonus +5 poin!")
    print("=" * 50)

def tampilkan_kategori():
    print("\n📂 Pilih Kategori Soal:")
    print("1. Teknologi Umum")
    print("2. Sistem Operasi")
    print("3. Pemrograman")
    pilihan = input("Masukkan nomor kategori (1/2/3): ").strip()
    if pilihan in ["1", "2", "3"]:
        return int(pilihan)
    else:
        print("❌ Pilihan tidak valid! Default ke 'Teknologi Umum'.")
        return 1

def tampilkan_soal(soal, jawaban_benar):
    print("\n📝 " + soal['pertanyaan'])
    for opsi in soal['opsi']:
        print(opsi)
    start_time = time.time()
    jawaban = input("⚡ Jawaban Anda (a/b/c/d): ").lower()
    end_time = time.time()

    if jawaban == jawaban_benar:
        waktu_jawab = end_time - start_time
        if waktu_jawab < 5:
            print("✅ Benar! +5 Bonus Cepat!")
            return 15
        print("✅ Benar!")
        return 10
    else:
        print(f"❌ Salah! Jawaban yang benar adalah {jawaban_benar.upper()}.")
        return 0

# Kumpulan soal berdasarkan kategori
soal_teknologi_umum = [
    {"pertanyaan": "1. Apa kepanjangan dari IoT?", 
     "opsi": ["a. Internet of Technology", 
              "b. Internet of Things", 
              "c. Information of Technology", 
              "d. Internet of Tools"], 
     "jawaban": "b"},
    {"pertanyaan": "2. Protokol standar untuk transfer data di internet adalah?", 
     "opsi": ["a. HTTP", 
              "b. FTP", 
              "c. SMTP", 
              "d. SNMP"], 
     "jawaban": "a"}
]

soal_sistem_operasi = [
    {"pertanyaan": "1. Perintah Linux untuk menghapus file adalah?", 
     "opsi": ["a. rm", 
              "b. del", 
              "c. rmdir", 
              "d. erase"], 
     "jawaban": "a"},
    {"pertanyaan": "2. Apa fungsi utama kernel dalam sistem operasi?", 
     "opsi": ["a. Menyediakan antarmuka pengguna", 
              "b. Mengelola sumber daya perangkat keras", 
              "c. Menjalankan aplikasi", 
              "d. Menyimpan data"], 
     "jawaban": "b"}
]

soal_pemrograman = [
    {"pertanyaan": "1. Apa arti dari OOP dalam pemrograman?", 
     "opsi": ["a. Object-Oriented Programming", 
              "b. Object Operation Protocol", 
              "c. Operational Object Process", 
              "d. Organized Operation Program"], 
     "jawaban": "a"},
    {"pertanyaan": "2. Fungsi untuk mencetak teks di Python adalah?", 
     "opsi": ["a. echo", 
              "b. print()", 
              "c. console.log", 
              "d. printf"], 
     "jawaban": "b"}
]

# Pilihan soal berdasarkan kategori
kategori_soal = {
    1: soal_teknologi_umum,
    2: soal_sistem_operasi,
    3: soal_pemrograman
}

def main():
    tampilkan_petunjuk()
    skor = 0

    # Memilih kategori soal
    kategori = tampilkan_kategori()
    soal_terpilih = random.sample(kategori_soal[kategori], 2)  # Mengambil 2 soal per kategori

    for index, soal in enumerate(soal_terpilih):
        print(f"\n🔹 Soal {index + 1}")
        skor += tampilkan_soal(soal, soal['jawaban'])

    print("\n🎮 Game selesai!")
    print(f"🎯 Skor Anda: {skor}/20")
    if skor == 20:
        print("🏆 Luar biasa! Kamu adalah seorang hecker sejati!")
    elif skor >= 10:
        print("✨ Hebat! Kamu punya potensi jadi hecker!")
    else:
        print("💡 Terus belajar, lamer!")

if __name__ == "__main__":
    main()