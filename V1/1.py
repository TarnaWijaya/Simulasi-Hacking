# Fungsi untuk memulai game
def start_game():
    print("=== Game Tebak Password ===")
    print("Selamat datang di Game Tebak Password!")
    print("Tugas Anda adalah menebak kata sandi untuk setiap level.")
    print("Anda akan diberikan petunjuk jika salah menebak.")
    
    # Daftar kata sandi untuk setiap level
    passwords = [
        "4V05TlDMPBtx",
        "HMKPN4rB8xEf",
        "zAFp3nZtvgVY",
        "wUUxQUgSY7cp",
        "44G2ZUTUELL4",
        "938538686728"
    ]
    
    # Mulai dari level 1
    current_level = 1
    
    # Iterasi untuk setiap level
    for password in passwords:
        print(f"\n--- Level {current_level} ---")
        while True:
            guess = input("Masukkan kata sandi: ")
            if guess == password:
                print("Benar! Anda berhasil ke level berikutnya.")
                current_level += 1
                break
            else:
                print("Salah! Coba lagi.")
    
    print("\nSelamat! Anda telah menyelesaikan semua level!")

# Fungsi utama untuk menjalankan game
def main():
    start_game()

if __name__ == "__main__":
    main()
