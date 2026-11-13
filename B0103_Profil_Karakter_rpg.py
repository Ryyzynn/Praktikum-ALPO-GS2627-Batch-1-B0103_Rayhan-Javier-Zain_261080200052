# ---- 1. DEKLARASI PROFIL KARAKTER GAME RPG ----
nama_hero = "Shadow Monarch"
level = 999
hp = 999
is_alive = True

inventory = ["Pedang", "Busur", "Perisai", "Pisau", "Tombak", "Tongkat", "Kapak"]

atribut = {
    "kekuatan": 999,
    "kelincahan": 999
}

# ---- 2. MENAMPILKAN INFORMASI KARAKTER ----
print("--- PROFIL KARAKTER RPG ---")
print("Nama Hero    :", nama_hero)
print("Level        :", level)
print("HP           :", hp)
print("Status Hidup :", is_alive)
print("Inventory    :", inventory)
print("Atribut      :", atribut)

# ---- 3. MENAMPILKAN TIPE DATA SETIAP VARIABEL ----
print("\n--- TIPE DATA VARIABEL ---")
print("Tipe nama_hero :", type(nama_hero))
print("Tipe level     :", type(level))
print("Tipe hp        :", type(hp))
print("Tipe is_alive  :", type(is_alive))
print("Tipe inventory :", type(inventory))
print("Tipe atribut   :", type(atribut))

# ---- 4. AKSI KARAKTER (UPDATE DATA) ----
# A. Karakter mendapatkan item baru
inventory.append("Ramuan HP")

# B. Karakter naik level
level = float(level) + 0.5

# ---- 5. MENAMPILKAN INFORMASI TERBARU ----
print("\n--- PROFIL KARAKTER SETELAH UPDATE ---")
print("Nama Hero    :", nama_hero)
print("Level        :", level)
print("HP           :", hp)
print("Status Hidup :", is_alive)
print("Inventory    :", inventory)
print("Atribut      :", atribut)