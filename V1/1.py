import random
import time

# Fungsi untuk menampilkan waktu dan teks dengan delay
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Fungsi untuk membuat kode acak
def generate_code(level):
    return ''.join(random.choices('0123456789abcdef', k=level))

# Fungsi untuk level
def hacker_level(level):
    slow_print(f"--- Level {level} ---")
    code = generate_code(level)
    slow_print(f"Memasuki sistem... Kode yang ditemukan: {code}")

    attempts = 3
    while attempts > 0:
        user_input = input(f"Masukkan kode untuk level {level}: ").strip()
        if user_input == code:
            slow_print("Kode benar! Akses diterima.", 0.1)
            return True
        else:
            attempts -= 1
            slow_print(f"Kode salah! {attempts} percobaan tersisa.", 0.1)
    slow_print("Akses ditolak. Anda kehabisan percobaan.", 0.1)
    return False

# Fungsi utama untuk game
def hacker_game():
    slow_print("Selamat datang di game Hacker Lamer!", 0.1)
    slow_print("Anda adalah seorang hacker pemula yang mencoba menyusup ke sistem.", 0.1)
    
    for level in range(1, 11):
        success = hacker_level(level)
        if not success:
            slow_print("Game Over! Anda gagal dalam menyusup ke sistem.", 0.1)
            break
        else:
            slow_print(f"Selamat! Anda berhasil menyusup ke level {level}.", 0.1)
    else:
        slow_print("Selamat! Anda telah berhasil menyelesaikan semua level!", 0.1)

# Memulai game
if __name__ == "__main__":
    hacker_game()