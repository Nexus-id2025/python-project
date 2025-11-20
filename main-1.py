import math
import cmath

def hitung_lengkap(a, b, c, n):
    # --- BAGIAN 1: MENCARI AKAR ---
    if a == 0:
        print("Error: Nilai 'a' tidak boleh 0.")
        return

    D = b**2 - 4*a*c
    print("=" * 50)
    print(f"Persamaan: {a}x² + ({b})x + ({c}) = 0")
    print(f"Nilai pengguna (n): {n}")
    print("-" * 50)

    # Menentukan x1 dan x2
    if D >= 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        tipe_akar = "Real"
    else:
        x1 = (-b + cmath.sqrt(D)) / (2*a)
        x2 = (-b - cmath.sqrt(D)) / (2*a)
        tipe_akar = "Kompleks/Imajiner"

    print(f"Akar ({tipe_akar}):")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    print("-" * 50)

    # --- BAGIAN 2: OPERASI DASAR (Dari request sebelumnya) ---
    print("OPERASI DASAR X1 & X2:")
    print(f"1. x1 + x2 \t= {x1 + x2}")
    print(f"2. x1 - x2 \t= {x1 - x2}")
    print(f"3. (x1)² \t= {x1**2}")
    print(f"4. (x2)² \t= {x2**2}")
    print(f"5. x1 × x2 \t= {x1 * x2}")
    print("-" * 50)

    # --- BAGIAN 3: OPERASI KUSTOM (Request BARU Anda) ---
    # a. X1 dijumlahkan dengan nilai pengguna
    hasil_a = x1 + n
    
    # b. X2 dikurangi dengan nilai pengguna
    hasil_b = x2 - n
    
    # c. X1 dikalikan dengan nilai pengguna
    hasil_c = x1 * n
    
    # d. Hasil ketiga nilai dijumlahkan lalu dibagi 3
    total_kustom = hasil_a + hasil_b + hasil_c
    rata_rata_kustom = total_kustom / 3

    print(f"OPERASI DENGAN NILAI PENGGUNA (n={n}):")
    print(f"A. x1 + n \t\t= {hasil_a}")
    print(f"B. x2 - n \t\t= {hasil_b}")
    print(f"C. x1 × n \t\t= {hasil_c}")
    print("-" * 30)
    print(f"Total (A+B+C) \t\t= {total_kustom}")
    print(f"Rata-rata (Total / 3) \t= {rata_rata_kustom}")
    print("=" * 50)

# --- Bagian Input Pengguna ---
if __name__ == "__main__":
    print("--- Program Analisis Akar Kuadrat Kustom ---")
    try:
        in_a = float(input("Masukkan nilai a: "))
        in_b = float(input("Masukkan nilai b: "))
        in_c = float(input("Masukkan nilai c: "))
        
        # Input tambahan sesuai permintaan Anda
        in_n = float(input("Masukkan nilai kustom tambahan: "))
        
        hitung_lengkap(in_a, in_b, in_c, in_n)
        
    except ValueError:
        print("Mohon masukkan angka saja.")