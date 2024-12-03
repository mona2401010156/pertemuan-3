
import math

# Input nilai sisi-sisi bangun
panjang_persegi_panjang = 28  # cm
lebar_persegi_panjang = 14  # cm

# Hitung jari-jari lingkaran
jari_jari = lebar_persegi_panjang / 2

# Hitung luas
luas_persegi_panjang = panjang_persegi_panjang * lebar_persegi_panjang
luas_lingkaran_penuh = math.pi * jari_jari**2
luas_setengah_lingkaran = luas_lingkaran_penuh / 2
luas_daerah_arsir = luas_persegi_panjang - 2 * luas_setengah_lingkaran

# Tampilkan hasil
print("Luas daerah yang diarsir adalah:", luas_daerah_arsir, "cm²")
