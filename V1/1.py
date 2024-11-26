import random
import time

# Pendahuluan
print("🔥 Selamat datang di Game Hacker! 🔥")
print("Mulailah dari level Lamer 1 dan tingkatkan ke Lamer 10!")
print("Selesaikan tantangan hacking untuk naik level!\n")

# Variabel awal
level = 1
points = 0

# Fungsi tantangan hacking
def hacking_challenge(level):
    print(f"Level {level}: Mulai tantangan hacking...\n")
    time.sleep(1)
    challenge_type = random.choice(["Math", "Password", "Trivia"])
    
    if challenge_type == "Math":
        # Tantangan matematika sederhana
        num1 = random.randint(1, 10 * level)
        num2 = random.randint(1, 10 * level)
        correct_answer = num1 + num2
        answer = int(input(f"Hitung: {num1} + {num2} = "))
        return answer == correct_answer
    
    elif challenge_type == "Password":
        # Tantangan menebak password
        password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=level + 2))
        print(f"Password adalah: {password}")
        guess = input("Tebak password (masukkan kembali): ")
        return guess == password
    
    elif challenge_type == "Trivia":
        # Tantangan trivia hacking
        trivia = {
            "Apa nama sistem operasi yang digunakan kebanyakan server?": "linux",
            "Apa kepanjangan dari SQL?": "structured query language",
            "Protokol untuk transfer data aman di web?": "https",
        }
        question, correct_answer = random.choice(list(trivia.items()))
        answer = input(f"{question} ").strip().lower()
        return answer == correct_answer
    
    return False

# Gameplay utama
while level <= 10:
    print(f"💻 Anda berada di Level {level}.")
    if hacking_challenge(level):
        print("✅ Tantangan berhasil! Naik level!\n")
        points += level * 10
        level += 1
    else:
        print("❌ Gagal menyelesaikan tantangan. Coba lagi!\n")
        time.sleep(1)

# Akhir permainan
print("🎉 Selamat! Anda telah mencapai Level Lamer 01 ! 🎉")
print(f"Skor akhir Anda: {points} poin.")
print("Terima kasih telah bermain!")