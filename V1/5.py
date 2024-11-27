import random
import time
import json
import os

# File untuk menyimpan skor tertinggi
LEADERBOARD_FILE = "leaderboard.json"

def animasi_tulisan(teks, delay=0.03):
    """Menampilkan teks dengan animasi sederhana."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def tampilkan_petunjuk():
    print("=" * 50)
    animasi_tulisan("🎮 Selamat Datang di Game Hecker Lamer (V5) 🎮")
    print("=" * 50)
    animasi_tulisan("📜 Peraturan:")
    animasi_tulisan("1. Jawab sebanyak mungkin pertanyaan dalam waktu 60 detik.")
    animasi_tulisan("2. Jawaban benar bernilai 10 poin.")
    animasi_tulisan("3. Kesalahan tidak mengurangi nyawa, tapi waktu tetap berjalan.")
    animasi_tulisan("4. Semakin banyak jawaban benar, semakin sulit soal berikutnya!")
    print("=" * 50)

def tampilkan_leaderboard():
    print("\n🏆 Skor Tertinggi:")
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = json.load(file)
        for index, entry in enumerate(sorted(leaderboard, key=lambda x: x['score'], reverse=True)[:5]):
            print(f"{index + 1}. {entry['name']} - {entry['score']} poin")
    else:
        print("📂 Belum ada skor tertinggi! Jadilah yang pertama!")

def simpan_leaderboard(nama, skor):
    if os.path.exists(LEADERBOARD_FILE):
        with open(LEADERBOARD_FILE, "r") as file:
            leaderboard = json.load(file)
    else:
        leaderboard = []

    leaderboard.append({"name": nama, "score": skor})
    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)

def tingkatkan_kesulitan(level):
    return min(level + 1, 3)

def tampilkan_soal(soal, jawaban_benar):
    print("\n📝 " + soal['pertanyaan'])
    for opsi in soal['opsi']:
        print(opsi)
    jawaban = input("⚡ Jawaban Anda (a/b/c/d): ").lower()
    if jawaban == jawaban_benar:
        animasi_tulisan("✅ Benar!")
        return True
    else:
        animasi_tulisan(f"❌ Salah! Jawaban yang benar adalah {jawaban_benar.upper()}.")
        return False

# Kumpulan soal berdasarkan level kesulitan
soal_mudah = [
    {"pertanyaan": "1. Apa singkatan dari RAM?", 
     "opsi": ["a. Random Access Memory", "b. Read Access Memory", "c. Read Advanced Memory", "d. Rapid Access Module"], 
     "jawaban": "a"},
    {"pertanyaan": "2. Apa itu URL?", 
     "opsi": ["a. Uniform Resource Locator", "b. Unified Resource Logic", "c. Unique Resource Link", "d. User Resource Label"], 
     "jawaban": "a"}
]

soal_sedang = [
    {"pertanyaan": "1. Protokol untuk pengiriman email adalah?", 
     "opsi": ["a. SMTP", "b. HTTP", "c. FTP", "d. SNMP"], 
     "jawaban": "a"},
    {"pertanyaan": "2. Perintah Linux untuk melihat proses yang berjalan adalah?", 
     "opsi": ["a. ps", "b. top", "c. htop", "d. semua benar"], 
     "jawaban": "d"}
]

soal_sulit = [
    {"pertanyaan": "1. Apa fungsi hashing dalam keamanan data?", 
     "opsi": ["a. Mengenkripsi data", "b. Membuat sidik jari data", 
              "c. Mengompres data", "d. Mentransfer data"], 
     "jawaban": "b"},
    {"pertanyaan": "2. Apa perbedaan IPv4 dan IPv6?", 
     "opsi": ["a. Panjang alamat", "b. Keamanan", 
              "c. Konektivitas perangkat", "d. Semua benar"], 
     "jawaban": "d"}
]

level_soal = {
    1: soal_mudah,
    2: soal_sedang,
    3: soal_sulit
}

def main():
    tampilkan_petunjuk()
    tampilkan_leaderboard()

    nama = input("\nMasukkan nama Anda: ").strip()
    skor = 0
    level = 1
    waktu_mulai = time.time()
    waktu_total = 60  # Waktu bermain dalam detik

    while time.time() - waktu_mulai < waktu_total:
        print(f"\n⏳ Waktu tersisa: {int(waktu_total - (time.time() - waktu_mulai))} detik")
        soal = random.choice(level_soal[level])
        benar = tampilkan_soal(soal, soal['jawaban'])
        if benar:
            skor += 10
            level = tingkatkan_kesulitan(level)

    print("\n⏰ Waktu habis!")
    print(f"🎯 Skor Anda: {skor}")
    simpan_leaderboard(nama, skor)

    print("\n🔰 Skor akhir telah disimpan di leaderboard.")
    tampilkan_leaderboard()

if __name__ == "__main__":
    main()