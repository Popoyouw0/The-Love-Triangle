# --- 1. DEFINISI KARAKTER & GAMBAR ---

# Karakter
define c = Character("caesar", color="#ff4d4d") 
define t = Character("taeju", color="#4d79ff")     
define y = Character("[player_name]", color="#c8ffc8") 
define z = Character("Zhenya", color="#5bcaff")

# Backgrounds (Sesuai list scene kamu)
image bg apartement_room = "scenes/apartment_room.png"
image bg apartement_building = "scenes/apartment_building.png"
image bg streets = "scenes/streets.png"
image bg cafe_outside = "scenes/cafe_outside.png"
image bg cafe_inside = "scenes/cafe_inside.png"

# Variabel untuk Poin Hubungan
default love_taeju = 0

# --- 2. MULAI CERITA ---

label start:

    stop music fadeout 1.0
    # Input Nama Pemain
    $ player_name = renpy.input("Masukkan namamu:", length=15).strip() or "Y/N"

    # --- SCENE 1: PAGI YANG KACAU ---
    scene bg apartement_room
    with fade

    play music "audio/apartement room.mp3" fadein 1.0

    "Pagi ini dimulai dengan bencana."
    
    play sound "alarm beep.mp3" loop

    "Alarm ponselmu mati, dan kamu hanya punya waktu 15 menit sebelum shift di café dimulai."

    stop sound fadeout 0.5
    y "Ya ampun aku telat!" with hpunch

    # Transisi Slide Cepat (Kiri ke Kanan) seolah berpakaian
    show black with pushright
    hide black with pushleft

    "Dengan berpakaian terburu-buru dan langsung menutup pintu apartemen."
    play sound "door slam.mp3"

    # --- SCENE 2: LARI DI JALANAN ---
    scene bg apartment_building
    with vpunch # Efek getar vertikal (Banting pintu)

    "Kamu berlari keluar..."

    scene bg streets
    with moveinright # Efek masuk cepat dari kanan (lari)

    "Kamu menyusuri trotoar padat, tidak menyadari bahwa hidupmu yang tenang akan segera berubah."
    
    "Kamu berlari kencang hingga..."

    # --- SCENE 3: TABRAKAN DENGAN CAESAR ---
    
    # EFEK TABRAKAN (Flash Putih + Getar Keras)
    scene bg streets 
    with Fade(0.1, 0.0, 0.5, color="#fff") 
    with hpunch

    play sound "thud.mp3"
    "{b}BRAK!{/b}"

    "Kamu menabrak dada seseorang yang sekeras beton. Tubuhmu terpental..."
    "Tapi sebuah tangan kekar menangkap pinggangmu sebelum kamu jatuh ke aspal."

    # Muncul Caesar
    show caesar at center with dissolve

    "Caesar menatapmu dengan intensitas yang membuat napasmu tertahan. Dia tidak marah, justru ada seringai tipis di bibirnya."

    c "Terburu-buru, {i}Malen'kaya moya{/i}?"
    c "Lain kali, lihat jalan... atau aku akan berpikir kau sengaja menjatuhkan diri ke pelukanku."

    "Belum sempat kamu meminta maaf, ponselmu bergetar hebat di saku."

    # Pesan Masuk (Bisa pakai format NVL atau narasi biasa)
    "'Y/N, kau di mana? Aku akan ke cafe dan membawakan bekal favoritmu. Hati-hati di jalan dan jangan lupa kabari aku kalau sudah sampai, oke?'"

    hide caesar with dissolve
    "Kamu segera melanjutkan lari menuju kafe."

    # --- SCENE 4: CAFE & TIME SKIP ---
    scene bg cafe_outside
    with fade

    "(30 Menit Kemudian)"
    "Kamu akhirnya sampai dan memulai shift pagi mu. Temanmu yang sudah bersiap hanya bisa menggelengkan kepala."

    # Efek Time Skip (Clock wipe atau fade)
    scene bg cafe_inside
    with pixellate 

    "Waktu berlalu dari pagi menuju siang. Pelanggan makin berdatangan, terlebih saat jam makan siang."
    "Kamu sedikit kerepotan tetapi bekerja dengan sangat baik."
    
    "Break time telah tiba. Kamu mulai ke ruang staff dan meraih ponsel."

    "'Pesan Masuk & Missed Call: Yeo Taeju] : 'Y/N, aku sudah di depan café-mu. Keluar dan ambil bekalmu ini, aku tidak mau kamu skip makan siang.'"

    # --- SCENE 5: PERTEMUAN DENGAN TAEJU ---
    scene bg cafe_outside
    with wipeleft

    "Kamu keluar café dari pintu belakang dan menemui Taeju yang sedang membawa bekal untukmu."
    
    show taeju at center with dissolve
    "Senyum hangat berada di bibirnya."

    t "Akhirnya kau keluar juga."
    "Dia tersenyum lembut dan mengelus rambutmu."
    t "Kenapa kau tidak membalas pesanku, hmm?"

    # --- MENU PILIHAN (BRANCHING) ---
    menu:
        "Jujur dan Sedikit Manja":
            # Pilihan 1
            jump pilihan_jujur

        "Diam/Gugup (Mengingat Caesar)":
            # Pilihan 2
            jump pilihan_diam

# --- LOGIKA PILIHAN 1 (JUJUR) ---
label pilihan_jujur:
    y "Maaf, Taeju-ya... Tadi aku benar-benar hampir terlambat, jadi tidak sempat mengecek ponsel sama sekali."

    show taeju
    t "Sudah kuduga. Kamu kesiangan lagi, kan? Berhenti bergadang, Y/N."
    t "Kamu tahu sendiri kafemu ini tidak pernah sepi. Aku tidak mau kamu jatuh sakit karena terlalu memaksakan diri. Mengerti?"

    # Sub-Menu (Pilihan A/B)
    menu:
        "(Patuh) Iya, aku mengerti.":
            $ love_taeju += 10 # Tambah poin banyak (Taeju suka)
            y "Iya, aku mengerti. Maaf ya sudah membuatmu khawatir."
            
            show taeju 
            "(Taeju merasa menang dan semakin menyukaimu.)"
            t "Anak pintar."

        "(Canggung) Iya, jangan ngomel terus.":
            $ love_taeju += 5 # Tambah poin sedikit
            y "Iya, iya... jangan mengomel terus."
            
            show taeju 
            "(Taeju merasa sedikit terabaikan, tapi tetap peduli.)"
            t "Aku mengomel karena aku peduli, tahu."

    jump after_choice

# --- LOGIKA PILIHAN 2 (DIAM) ---
label pilihan_diam:
    # Tidak ada penambahan/pengurangan poin
    "Kamu terdiam sejenak, masih sedikit terguncang karena kejadian dengan Caesar tadi pagi."

    show taeju 
    "(Senyum Taeju memudar, ekspresinya berubah khawatir. Dia memegang bahumu.)"
    
    t "Kenapa diam saja? Kamu sakit? Atau ada seseorang yang mengganggumu di jalan tadi?"
    
    y "Ah, t-tidak. Bukan apa-apa."

    jump after_choice

# --- PENUTUP SCENE ---
label after_choice:
    
    show taeju 
    t "Ah, sudahlah… Ambil ini dan segera makan."
    t "Tempat makannya nanti saja dikembalikan."
    
    # Aksi mengacak rambut
    "Dia mengacak-acak rambut kamu sesaat."
    t "Semangat bekerjanya!"

    "Total Poin Taeju saat ini: [love_taeju]"

    return