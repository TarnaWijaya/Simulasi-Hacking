import random
import time
import json
import os
import sys
import pickle

# File untuk menyimpan skor tertinggi
LEADERBOARD_FILE = "leaderboard.json"
PROGRESS_FILE = "progress.pkl"

def animasi_tulisan(teks, delay=0.03):
    """Menampilkan teks dengan animasi sederhana."""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def tampilkan_petunjuk():
    print("=" * 50)
    animasi_tulisan("🎮 Selamat Datang di Game Hecker Lamer (V8) 🎮")
    print("=" * 50)
    animasi_tulisan("📜 Peraturan:")
    animasi_tulisan("1. Pilih mode permainan: Multiplayer atau Story.")
    animasi_tulisan("2. Jawab sebanyak mungkin pertanyaan dalam waktu terbatas.")
    animasi_tulisan("3. Jawaban benar bernilai 10 poin.")
    animasi_tulisan("4. Setiap mode permainan memiliki tantangannya sendiri.")
    animasi_tulisan("5. Tingkat kesulitan dapat disesuaikan.")
    animasi_tulisan("6. Anda bisa menyelamatkan dan melanjutkan permainan di lain waktu.")
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

def simpan_progress(nama, level, skor):
    """Menyimpan progress permainan (level dan skor)."""
    progress = {
        'nama': nama,
        'level': level,
        'skor': skor
    }
    with open(PROGRESS_FILE, 'wb') as file:
        pickle.dump(progress, file)

def load_progress():
    """Memuat progress permainan jika ada."""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'rb') as file:
            return pickle.load(file)
    else:
        return None

def pilih_mode():
    print("\n💡 Pilih Mode Permainan:")
    print("1. Multiplayer (Bersaing dengan teman!)")
    print("2. Story Mode (Menyelesaikan misi dengan cerita)")
    pilihan = input("Masukkan nomor mode (1/2): ").strip()
    if pilihan == "1":
        return "multiplayer"
    elif pilihan == "2":
        return "story"
    else:
        print("❌ Pilihan tidak valid! Default ke 'Story Mode'.")
        return "story"

def pilih_avatar():
    print("\n👤 Pilih Avatar Anda:")
    print("1. 👨‍💻 Hacker Klasik")
    print("2. 👩‍💻 Hacker Futuristik")
    print("3. 🕶️ Hacker Misterius")
    pilihan = input("Masukkan nomor avatar (1/2/3): ").strip()
    if pilihan == "1":
        return "Hacker Klasik"
    elif pilihan == "2":
        return "Hacker Futuristik"
    elif pilihan == "3":
        return "Hacker Misterius"
    else:
        print("❌ Pilihan tidak valid! Default ke 'Hacker Klasik'.")
        return "Hacker Klasik"

def story_mode():
    print("\n📖 Story Mode - Anda adalah seorang hacker pemula yang sedang mencoba menyusup ke sistem rahasia.")
    print("Tugas Anda adalah menjawab serangkaian soal yang akan membawa Anda melalui tahapan misi.")
    print("Setiap jawaban benar membawa Anda lebih dekat untuk menyelesaikan misi!")

def multiplayer_mode():
    print("\n🌍 Multiplayer Mode - Bersiap untuk bersaing dengan teman!")
    nama1 = input("Masukkan nama Pemain 1: ")
    nama2 = input("Masukkan nama Pemain 2: ")
    print(f"\n🔹 {nama1} vs {nama2}")
    return [(nama1, 0), (nama2, 0)]

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

    mode = pilih_mode()
    avatar = pilih_avatar()

    progress = load_progress()

    if mode == "story":
        story_mode()
    else:
        players = multiplayer_mode()

    nama = input("\nMasukkan nama Anda: ").strip()
    skor = 0
    level = 1
    if progress:
        print(f"\n📝 Memuat progres permainan...")
        nama = progress['nama']
        level = progress['level']
        skor = progress['skor']
        animasi_tulisan(f"🎮 Selamat datang kembali, {nama}! Anda berada di level {level} dengan skor {skor}.")

    waktu_mulai = time.time()
    waktu_total = 60  # Waktu bermain dalam detik

    while time.time() - waktu_mulai < waktu_total:
        print(f"\n⏳ Waktu tersisa: {int(waktu_total - (time.time() - waktu_mulai))} detik")
        soal = random.choice(level_soal[level])
        benar = tampilkan_soal(soal, soal['jawaban'])
        if benar:
            skor += 10
            level = min(level + 1, 3)

    print("\n⏰ Waktu habis!")
    print(f"🎯 Skor Anda: {skor}")
    simpan_leaderboard(nama, skor)
    simpan_progress(nama, level, skor)

    print("\n🔰 Skor akhir telah disimpan di leaderboard.")
    tampilkan_leaderboard()

if __name__ == "__main__":
    main()