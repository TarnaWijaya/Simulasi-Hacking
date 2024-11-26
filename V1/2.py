import random

def generate_questions(level):
    """
    Fungsi untuk menghasilkan soal berdasarkan level.
    """
    questions = []
    for i in range(10):  # 10 soal per lembar
        if level == 1:
            # Soal level 1: Penjumlahan sederhana
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            correct_answer = num1 + num2
            questions.append((f"{num1} + {num2} = ?", correct_answer))
        elif level == 2:
            # Soal level 2: Pengurangan sederhana
            num1 = random.randint(10, 20)
            num2 = random.randint(1, 10)
            correct_answer = num1 - num2
            questions.append((f"{num1} - {num2} = ?", correct_answer))
        elif level == 3:
            # Soal level 3: Perkalian sederhana
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            correct_answer = num1 * num2
            questions.append((f"{num1} x {num2} = ?", correct_answer))
        else:
            # Level di atas 3: Campuran soal
            num1 = random.randint(1, 10 * level)
            num2 = random.randint(1, 10 * level)
            operation = random.choice(["+", "-", "*"])
            if operation == "+":
                correct_answer = num1 + num2
                questions.append((f"{num1} + {num2} = ?", correct_answer))
            elif operation == "-":
                correct_answer = num1 - num2
                questions.append((f"{num1} - {num2} = ?", correct_answer))
            elif operation == "*":
                correct_answer = num1 * num2
                questions.append((f"{num1} x {num2} = ?", correct_answer))
    return questions

def play_level(level):
    """
    Fungsi untuk memainkan satu level.
    """
    print(f"📘 Level {level}: Jawab 10 soal berikut!")
    questions = generate_questions(level)
    score = 0
    
    for idx, (question, correct_answer) in enumerate(questions, start=1):
        try:
            user_answer = int(input(f"Soal {idx}: {question} "))
            if user_answer == correct_answer:
                print("✅ Benar!")
                score += 1
            else:
                print(f"❌ Salah! Jawaban yang benar: {correct_answer}")
        except ValueError:
            print("❌ Input tidak valid! Jawaban salah.")
    
    print(f"\nLevel {level} selesai! Skor Anda: {score}/10")
    return score >= 7  # Lulus jika benar minimal 7 soal

# Gameplay utama
def main():
    print("🔥 Selamat datang di Game Hacker Level! 🔥")
    print("Naikkan level Anda dengan menyelesaikan lembar soal (10 soal/level).\n")
    
    level = 1
    while level <= 10:
        print(f"=== Memulai Level {level} ===")
        if play_level(level):
            print(f"🎉 Selamat! Anda lulus Level {level}.\n")
            level += 1
        else:
            print("❌ Anda gagal di level ini. Coba lagi!\n")
    
    print("🎊 Selamat! Anda telah menyelesaikan semua level! 🎊")

if __name__ == "__main__":
    main()