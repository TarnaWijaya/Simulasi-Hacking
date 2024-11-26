import random
import time

# Pendahuluan
print("🔥 Selamat datang di Game Hacker! 🔥")
print("Mulailah dari Level 1 dan tingkatkan ke Level 10!")
print("Selesaikan tantangan hacking untuk menjadi hacker legendaris!\n")

# Variabel awal
level = 1
points = 0

# Fungsi tantangan hacking
def hacking_challenge(level):
    print(f"\nLevel {level}: Tantangan dimulai...")
    time.sleep(1)

    # Soal berdasarkan level
    if level == 1:
        print("Soal: Hitung 5 + 3")
        return int(input("Jawaban: ")) == 8
    
    elif level == 2:
        print("Soal: Berapa hasil dari 12 * 2?")
        return int(input("Jawaban: ")) == 24
    
    elif level == 3:
        print("Soal: Tebak password ini: 'abc123'")
        return input("Masukkan password: ") == "abc123"
    
    elif level == 4:
        print("Soal: Apa sistem operasi yang sering digunakan oleh server?")
        return input("Jawaban: ").strip().lower() == "linux"
    
    elif level == 5:
        print("Soal: Berapa hasil dari 9 + 6?")
        return int(input("Jawaban: ")) == 15
    
    elif level == 6:
        password = "h4x0r"
        print(f"Soal: Password terenkripsi adalah '{password}'. Masukkan password yang sama.")
        return input("Masukkan password: ") == password
    
    elif level == 7:
        print("Soal: Apa kepanjangan dari HTTPS?")
        return input("Jawaban: ").strip().lower() == "hypertext transfer protocol secure"
    
    elif level == 8:
        print("Soal: Berapa hasil dari 45 / 5?")
        return int(input("Jawaban: ")) == 9
    
    elif level == 9:
        print("Soal: Apa nama bahasa pemrograman yang memiliki logo ular?")
        return input("Jawaban: ").strip().lower() == "python"
    
    elif level == 10:
        print("Soal terakhir: Berapa hasil dari 100 - 25?")
        return int(input("Jawaban: ")) == 75

    return False

# Gameplay utama
while level <= 10:
    print(f"\n💻 Anda berada di Level {level}.")
    if hacking_challenge(level):
        print("✅ Tantangan berhasil! Naik level!")
        points += level * 10
        level += 1
    else:
        print("❌ Salah jawaban. Coba lagi!")

# Akhir permainan
print("\n🎉 Selamat! Anda telah menyelesaikan semua level! 🎉")
print(f"Skor akhir Anda: {points} poin.")
print("Terima kasih telah bermain!")