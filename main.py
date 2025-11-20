import os
from colorama import Fore


#ukuran terminal
lebar_terminal = os.get_terminal_size().columns

#hiasan
print(Fore.GREEN + "=" * lebar_terminal)
print(Fore.YELLOW + "Selamat datang di Multi Mini Game".center(lebar_terminal))
print(Fore.GREEN + "=" * lebar_terminal)
print("")
print("Silakan pilih game yang akan dimainkan!")
print("")

game = ["Game1", "Game2", "Game3", "Game4"]
huruf = ["a", "b", "c", "d"]

for i in range (len(game)):
    print(f"{huruf[i]})", f"{game[i]}")

print("")
pilihan = input("Pilihan : ")

