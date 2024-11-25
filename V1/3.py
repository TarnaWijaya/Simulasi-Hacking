# Game teka-teki dunia cyber dan hacker
import time

def delay_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    delay_print("Selamat datang, Cyber Agent!\n")
    delay_print("Misi Anda adalah memecahkan teka-teki dan menghentikan rencana hacker jahat yang ingin mengambil alih sistem dunia.\n")
    delay_print("Bersiaplah, waktu adalah musuh Anda!\n")
    delay_print("==========================================\n")
    start_game()

def start_game():
    delay_print("Teka-teki 1: Saya adalah sistem keamanan, tetapi banyak yang mencoba menjebol saya.\n")
    delay_print("Jika kata sandi saya terlalu lemah, mereka akan berhasil. Siapakah saya?")
    answer1 = input("Jawab: ").strip().lower()
    
    if answer1 in ["password", "kata sandi"]:
        delay_print("\nBenar! Kata sandi adalah pertahanan pertama.\n")
        teka_teki_2()
    else:
        delay_print("\nSalah! Cobalah lagi.\n")
        start_game()

def teka_teki_2():
    delay_print("Teka-teki 2: Saya seperti bayangan, saya bersembunyi di belakang layar. Tanpa saya, internet tidak aman. Siapakah saya?")
    answer2 = input("Jawab: ").strip().lower()
    
    if answer2 in ["vpn", "firewall", "proxy"]:
        delay_print("\nLuar biasa! Anda berhasil menjawab teka-teki ini.\n")
        teka_teki_3()
    else:
        delay_print("\nSalah! Pikirkan kembali.\n")
        teka_teki_2()

def teka_teki_3():
    delay_print("Teka-teki 3: Saya adalah mata-mata di sistem Anda. Saya datang dalam bentuk email atau unduhan mencurigakan. Siapakah saya?")
    answer3 = input("Jawab: ").strip().lower()
    
    if answer3 in ["malware", "virus", "spyware"]:
        delay_print("\nHebat! Anda berhasil mengenali ancaman tersebut.\n")
        ending()
    else:
        delay_print("\nJawaban salah. Cobalah lagi.\n")
        teka_teki_3()

def ending():
    delay_print("Selamat! Anda telah memecahkan semua teka-teki.\n")
    delay_print("Sistem dunia kini aman berkat Anda, Cyber Agent.\n")
    delay_print("Misi selesai. Terima kasih atas kerja keras Anda!\n")

# Mulai permainan
intro()