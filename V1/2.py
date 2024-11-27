import random

def tampilkan_petunjuk():
    print("=" * 40)
    print("🔥 Selamat datang di Game Hecker Lamer 🔥")
    print("=" * 40)
    print("📌 Jawab 10 pertanyaan untuk membuktikan diri Anda!")
    print("📌 Jawaban benar bernilai 10 poin.")
    print("📌 Ketik huruf jawaban (a, b, c, d) untuk memilih.")
    print("=" * 40)

def tampilkan_soal(soal, jawaban_benar):
    print("\n📖 " + soal['pertanyaan'])
    for opsi in soal['opsi']:
        print(opsi)
    jawaban = input("⚡ Jawaban Anda (a/b/c/d): ").lower()
    if jawaban == jawaban_benar:
        print("✅ Benar!")
        return 10
    else:
        print(f"❌ Salah! Jawaban yang benar adalah {jawaban_benar.upper()}.")
        return 0

# Kumpulan soal untuk versi ini
soal_version_2 = [
    {"pertanyaan": "1. Apa fungsi utama dari sistem operasi?", 
     "opsi": ["a. Mengelola perangkat keras", 
              "b. Memroses data pengguna", 
              "c. Menyimpan data secara permanen", 
              "d. Mempercepat kinerja CPU"], 
     "jawaban": "a"},
    
    {"pertanyaan": "2. Apa arti dari HTML?", 
     "opsi": ["a. Hyper Text Markup Language", 
              "b. High Tech Machine Learning", 
              "c. Hyperlink Text Manager Logic", 
              "d. Hyper Tool Machine Learning"], 
     "jawaban": "a"},
    
    {"pertanyaan": "3. Port default untuk SSH adalah?", 
     "opsi": ["a. 21", 
              "b. 22", 
              "c. 80", 
              "d. 443"], 
     "jawaban": "b"},
    
    {"pertanyaan": "4. Apa itu DNS?", 
     "opsi": ["a. Domain Name System", 
              "b. Data Network System", 
              "c. Disk Networking System", 
              "d. Directory Network Service"], 
     "jawaban": "a"},
    
    {"pertanyaan": "5. Siapa penemu Linux?", 
     "opsi": ["a. Linus Torvalds", 
              "b. Richard Stallman", 
              "c. Dennis Ritchie", 
              "d. Steve Jobs"], 
     "jawaban": "a"},
    
    {"pertanyaan": "6. Perintah Linux untuk melihat daftar file adalah?", 
     "opsi": ["a. ls", 
              "b. cd", 
              "c. mkdir", 
              "d. rm"], 
     "jawaban": "a"},
    
    {"pertanyaan": "7. Apa fungsi dari firewall?", 
     "opsi": ["a. Mencegah akses tidak sah ke jaringan", 
              "b. Mempercepat koneksi internet", 
              "c. Mengelola database", 
              "d. Meningkatkan keamanan password"], 
     "jawaban": "a"},
    
    {"pertanyaan": "8. Apa kepanjangan dari API?", 
     "opsi": ["a. Application Programming Interface", 
              "b. Advanced Protocol Interface", 
              "c. Application Process Integration", 
              "d. Automated Programming Interface"], 
     "jawaban": "a"},
    
    {"pertanyaan": "9. Dalam Python, fungsi untuk mencetak adalah?", 
     "opsi": ["a. echo", 
              "b. print()", 
              "c. cout", 
              "d. write"], 
     "jawaban": "b"},
    
    {"pertanyaan": "10. IP Address versi 4 terdiri dari berapa bit?", 
     "opsi": ["a. 16-bit", 
              "b. 32-bit", 
              "c. 64-bit", 
              "d. 128-bit"], 
     "jawaban": "b"}
]

def main():
    tampilkan_petunjuk()
    skor = 0

    # Pilih 10 soal secara acak
    soal_terpilih = random.sample(soal_version_2, 10)

    for index, soal in enumerate(soal_terpilih):
        print(f"\n🕹️ Soal {index + 1}")
        skor += tampilkan_soal(soal, soal['jawaban'])

    print("\n🎮 Game selesai!")
    print(f"🎯 Skor Anda: {skor}/100")
    if skor == 100:
        print("🏆 Luar biasa! Kamu adalah seorang hecker sejati!")
    elif skor >= 70:
        print("✨ Hebat! Kamu punya potensi jadi hecker!")
    else:
        print("💡 Terus belajar, lamer!")

if __name__ == "__main__":
    main()