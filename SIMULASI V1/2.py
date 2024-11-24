import time
import sys

# Fungsi untuk menampilkan animasi loading
def loading_animation():
    print("Memeriksa jawaban", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print("\n")

# Fungsi untuk menampilkan peraturan
def show_rules():
    print("\n=== PERATURAN ===")
    print("1. Anda harus memecahkan teka-teki biner untuk melanjutkan.")
    print("2. Anda akan diberikan pesan dalam bentuk biner.")
    print("3. Anda harus menebak pesan asli dari biner tersebut.")
    print("4. Setiap kesalahan akan mengurangi nyawa.")
    print("5. Anda hanya memiliki 3 nyawa!")
    print("=================\n")

# Fungsi untuk mengonversi biner ke teks
def binary_to_text(binary_code):
    binary_values = binary_code.split(' ')
    ascii_characters = [chr(int(bv, 2)) for bv in binary_values]
    return ''.join(ascii_characters)

# Fungsi untuk halaman rahasia jika berhasil menebak
def success_page():
    print("\n=== SELAMAT! ===")
    print("Kamu berhasil menebak code biner!")
    print("Selamat datang di dunia hacker!")
    print("=================")

# Program utama
def main():
    print("Selamat datang di Game Hacking: Tebak Code Biner!")
    show_rules()

    lives = 3  # Jumlah nyawa
    binary_message = "01001000 01100101 01101100 01101100 01101111 00101100 00100000 01010111 01101111 01110010 01101100 01100100 00100001"
    # Ini adalah pesan biner yang berarti "Hello, World!"
    
    print("\n=== Teka-Teki Biner ===")
    print(f"Pesan dalam biner: {binary_message}")
    
    while True:
        user_input = input("\nMasukkan tebakanmu: ")
        loading_animation()
        
        if user_input == binary_to_text(binary_message):
            print(f"Tebakan kamu benar! Pesan asli adalah: {binary_to_text(binary_message)}")
            success_page()
            break
        else:
            lives -= 1
            print(f"Salah! Sisa nyawa: {lives}")
            if lives == 0:
                print("\n=== GAME OVER ===")
                print("Kamu kehabisan nyawa. Coba lagi nanti!")
                return

# Jalankan program
if __name__ == "__main__":
    main()