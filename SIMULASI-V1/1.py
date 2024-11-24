import string

# Fungsi untuk mengenkripsi pesan menggunakan Caesar Cipher
def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():  # Jika karakter adalah huruf
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  # Menambahkan karakter selain huruf (spasi, tanda baca, dll)
    return encrypted

# Fungsi untuk mendekripsi pesan menggunakan Caesar Cipher
def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Jika karakter adalah huruf
            shift_base = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char  # Menambahkan karakter selain huruf (spasi, tanda baca, dll)
    return decrypted

# Fungsi untuk memulai game enkripsi
def start_game():
    print("=== Game Enkripsi ===")
    print("Selamat datang di Game Enkripsi!")
    print("Tugas Anda adalah mendekripsi pesan rahasia yang telah dienkripsi menggunakan Caesar Cipher.")
    print("Sebelum memulai, Anda akan diberi tahu cara bekerja dengan enkripsi ini.")
    print("\n=== Aturan Permainan ===")
    print("1. Pesan telah dienkripsi dengan Caesar Cipher.")
    print("2. Tugas Anda adalah menebak pergeseran (shift) yang digunakan untuk mengenkripsi pesan.")
    print("3. Setelah menebak pergeseran, coba dekripsi pesan dengan pergeseran yang benar.")

    # Pesan yang dienkripsi
    secret_message = "Uif qmbdf jt up xjmm zpv up uif psjoh!"
    print("\nPesan yang dienkripsi:")
    print(secret_message)

    # Meminta pemain untuk menebak pergeseran
    while True:
        try:
            shift_guess = int(input("\nMasukkan nilai pergeseran (shift) untuk mendekripsi pesan (misalnya: 1, 2, 3, ...): "))
            decrypted_message = caesar_decrypt(secret_message, shift_guess)
            print("\nPesan yang didekripsi:")
            print(decrypted_message)

            # Cek apakah pesan yang didekripsi benar
            if decrypted_message == "The plant is to kill you to the point!":
                print("\nSelamat! Anda berhasil mendekripsi pesan dengan benar!")
                break
            else:
                print("\nPesan tidak sesuai. Coba lagi dengan pergeseran yang berbeda.")
        except ValueError:
            print("Masukkan pergeseran yang valid (angka). Coba lagi.")

# Fungsi utama untuk menjalankan game
def main():
    start_game()

if __name__ == "__main__":
    main()