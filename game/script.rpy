# --- 1. DEFINISI KARAKTER & GAMBAR ---

# Karakter
define c = Character("caesar", color="#ff4d4d") 
define t = Character("taeju", color="#4d79ff")     
define y = Character("[player_name]", color="#c8ffc8") 
define z = Character("Zhenya", color="#5bcaff")

# Backgrounds (Sesuai list scene kamu)
image bg apartement_room = "scenes/apartment_room.png"
image bg apartement_building = "scenes/apartement_building.png"
image bg streets = "scenes/streets.png"
image bg cafe_outside = "scenes/cafe_outside.png"
image bg cafe_inside = "scenes/cafe_inside.png"

# CG / Scene Spesial
image cg greeting_zhenya = "scenes/greeting with him.png"
image cg lunch_caesar = "scenes/lunch with caesar.png"
image cg zhenya_dominant = "scenes/zhenya dominant.png"
image cg relax_taeju = "scenes/relax time with taeju.png"

# Variabel untuk Poin Hubungan
default love_taeju = 0
default love_caesar = 0
default love_zhenya = 0

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
    
    play sound "audio/alarm beep.mp3" loop

    "Alarm ponselmu mati, dan kamu hanya punya waktu 15 menit sebelum shift di café dimulai."

    stop sound fadeout 0.5
    y "Ya ampun aku telat!" with hpunch

    # Transisi Slide Cepat (Kiri ke Kanan) seolah berpakaian
    show black with pushright
    hide black with pushleft

    "Dengan berpakaian terburu-buru dan langsung menutup pintu apartemen."
    play sound "audio/door slam.mp3"

    # --- SCENE 2: LARI DI JALANAN ---
    scene bg apartement_building
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

    play sound "audio/thud.mp3"
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

    hide taeju with dissolve
    jump kembali_kerja

# --- SCENE 6: KEMBALI KERJA & TAMU TAK TERDUGA ---
label kembali_kerja:

    scene bg cafe_inside
    with fade

    play music "audio/inside cafe.mp3" fadein 1.0

    "Kamu kembali ke balik konter dengan perut kenyang. Bekal buatan Taeju memang tidak pernah gagal."
    "Jam menunjukkan pukul dua siang. Café mulai lengang, hanya tersisa beberapa pelanggan."

    "Kamu sedang mengelap mesin kopi ketika lonceng pintu berbunyi."
    play sound "audio/door slam.mp3"

    "Seketika suasana café terasa... berubah. Beberapa pelanggan melirik ke arah pintu, lalu buru-buru menunduk."

    show caesar at center
    with dissolve

    "Pria bertubuh tinggi dengan mantel hitam itu berjalan santai ke arah konter. Kamu mengenali seringai itu."
    "Caesar. Pria yang kamu tabrak tadi pagi."

    c "Ternyata benar kau bekerja di sini, {i}Malen'kaya moya{/i}."
    c "Aku mencarimu di setiap café di jalan itu. Kau tahu betapa merepotkannya itu?"

    # --- MENU PILIHAN (CAESAR DATANG) ---
    menu:
        "(Kaget) K-kamu?! Kenapa bisa di sini?":
            $ love_caesar += 5
            y "K-kamu?! Kenapa bisa ada di sini?!"

            c "Kenapa? Kau tidak senang aku datang?"
            "Dia menopang dagunya di konter, menatapmu tanpa berkedip."
            c "Padahal aku sudah repot-repot mencarimu."

        "(Profesional) Selamat datang. Mau pesan apa?":
            $ love_caesar += 10
            y "S-selamat datang. Mau pesan apa?"

            "Caesar terdiam sesaat, lalu tertawa rendah. Sepertinya dia menyukai keberanianmu berpura-pura tenang."
            c "Menarik. Jantungmu berdebar kencang tapi kau tetap sok tenang."
            c "Baiklah. Satu americano. Dan satu jam waktumu."

    "Sebelum kamu sempat menjawab, dia meletakkan beberapa lembar uang di konter. Jauh lebih banyak dari harga kopi manapun di menu."

    c "Duduk dan temani aku makan siang. Aku tidak menerima penolakan."

    hide caesar with dissolve
    jump makan_siang_caesar

# --- SCENE 7: MAKAN SIANG DENGAN CAESAR ---
label makan_siang_caesar:

    # CG: Lunch with Caesar
    scene cg lunch_caesar
    with dissolve

    "Entah bagaimana, kamu berakhir duduk di meja pojok bersama Caesar. Anehnya, tidak ada satu pun rekan kerjamu yang berani menegur."

    c "Jadi... siapa namamu? Aku tidak bisa terus memanggilmu 'gadis yang menabrakku'."

    y "...[player_name]."

    c "[player_name]."
    "Dia mengulang namamu perlahan, seolah mencicipi setiap hurufnya."
    c "Nama yang manis. Cocok untukmu."

    "Kamu menunduk, berusaha menyembunyikan wajahmu yang memanas. Pria ini berbahaya — instingmu berteriak begitu. Tapi kenapa jantungmu tidak mau tenang?"

    c "Pagi tadi. Pria yang mengirimimu pesan itu... kekasihmu?"

    # --- MENU PILIHAN (PERTANYAAN CAESAR) ---
    menu:
        "Bukan urusanmu.":
            $ love_caesar += 10
            y "...Bukan urusanmu."

            "Mata Caesar menyala. Bukan marah — justru tertarik."
            c "Berani sekali. Aku semakin menyukaimu, {i}Malen'kaya moya{/i}."
            c "Tapi kau belum menjawab. Berarti... bukan."

        "D-dia temanku. Teman dekat.":
            $ love_caesar += 5
            y "D-dia temanku. Teman dekat."

            c "Teman dekat, hm?"
            "Dia bersandar, tersenyum puas seperti kucing besar yang menemukan mangsa."
            c "Bagus. Berarti aku masih punya kesempatan."

    "Caesar menghabiskan makanannya dengan santai, sesekali melontarkan pertanyaan yang membuatmu gugup."
    "Saat akhirnya dia berdiri untuk pergi, dia menunduk mendekat ke telingamu."

    c "Sampai jumpa lagi, [player_name]. Dan percayalah... akan ada 'lagi'."

    "Dia pergi begitu saja, meninggalkan aroma parfum maskulin dan jantungmu yang berantakan."

    jump zhenya_muncul

# --- SCENE 8: ZHENYA, SANG PEMILIK CAFÉ ---
label zhenya_muncul:

    scene bg cafe_inside
    with dissolve

    "Kamu baru saja akan membereskan meja ketika sebuah suara dalam terdengar dari belakangmu."

    z "Kau tahu siapa pria itu, [player_name]?"

    # CG: Greeting with him (Zhenya)
    scene cg greeting_zhenya
    with dissolve

    "Kamu terlonjak dan berbalik. Zhenya — pemilik café ini — berdiri tepat di belakangmu. Sejak kapan?!"
    "Bosmu yang biasanya hanya muncul sesekali itu kini menatap pintu keluar dengan ekspresi yang belum pernah kamu lihat. Dingin. Tajam."

    # CG: Zhenya Dominant
    scene cg zhenya_dominant
    with dissolve

    "Tiba-tiba dia melangkah maju, memerangkapmu antara tubuhnya dan meja. Aura santainya yang biasa menghilang tanpa jejak."

    z "Jawab aku. Kau kenal Caesar Volkov?"

    y "V-Volkov...? Aku... aku hanya menabraknya tadi pagi, sungguh!"

    "Zhenya menatapmu lama, seolah membaca isi kepalamu. Lalu dia menghela napas."

    z "Menjauh darinya. Pria itu bukan orang yang bisa kau hadapi."

    # --- MENU PILIHAN (ZHENYA) ---
    menu:
        "Kenapa kamu bisa tahu tentang dia?":
            $ love_zhenya += 10
            y "...Kenapa kamu bisa tahu tentang dia? Kalian saling kenal?"

            "Rahang Zhenya mengeras. Untuk sesaat, kamu melihat sesuatu di matanya — masa lalu yang gelap."
            z "Anak pintar bertanya di saat yang salah."
            z "Cukup tahu bahwa aku dan dia... berasal dari dunia yang sama. Dan aku keluar dari sana bukan tanpa alasan."

        "B-baik, aku mengerti...":
            $ love_zhenya += 5
            y "B-baik... aku mengerti..."

            "Ekspresi Zhenya melunak sedikit. Dia mengusap puncak kepalamu — gestur yang tidak pernah dia lakukan sebelumnya."
            z "Bagus. Aku tidak mempekerjakanmu untuk melihatmu terseret ke dalam masalah."

    z "Satu hal lagi."
    "Dia mencondongkan tubuh, suaranya turun menjadi bisikan."
    z "Kalau dia datang lagi ke sini... langsung beritahu aku. Ini perintah."

    "Dia menegakkan tubuh dan berjalan pergi seolah tidak terjadi apa-apa, meninggalkanmu dengan seribu pertanyaan."
    "Siapa sebenarnya Zhenya? Dan apa hubungannya dengan Caesar?"

    jump pulang_dengan_taeju

# --- SCENE 9: SANTAI BERSAMA TAEJU ---
label pulang_dengan_taeju:

    stop music fadeout 1.0

    scene bg cafe_outside
    with fade

    play music "audio/outside cafe.mp3" fadein 1.0

    "Pukul delapan malam. Shift-mu akhirnya selesai."
    "Begitu keluar dari café, kamu menemukan sosok familiar bersandar di dinding sambil memainkan ponselnya."

    show taeju at center with dissolve

    t "Kerja bagus hari ini."

    y "Taeju?! Kamu menungguku?"

    t "Tentu saja. Hari ini kamu aneh sejak siang. Mana mungkin aku membiarkanmu pulang sendirian."

    hide taeju with dissolve

    # CG: Relax time with Taeju
    scene cg relax_taeju
    with dissolve

    "Kalian berakhir duduk santai berdua, ditemani angin malam. Kamu mengembalikan kotak bekalnya yang sudah kosong."

    t "Habis. Anak baik."
    "Dia tersenyum puas melihat kotak bekal yang bersih."

    t "Jadi... mau cerita? Ada apa hari ini?"
    "Tatapannya lembut, tapi kamu tahu Taeju — dia tidak akan berhenti bertanya sampai kamu bicara."

    # --- MENU PILIHAN (TAEJU) ---
    menu:
        "Cerita jujur tentang Caesar":
            $ love_taeju += 10
            y "Tadi pagi... waktu aku hampir telat, aku menabrak seseorang di jalan. Dan siangnya dia tiba-tiba datang ke café."

            "Taeju terdiam. Senyumnya masih ada, tapi matanya berubah serius."
            t "Dia melakukan sesuatu padamu?"
            y "Tidak! Dia cuma... mengajakku bicara."
            t "...Hm. Kalau dia datang lagi dan membuatmu tidak nyaman, telepon aku. Detik itu juga. Janji?"
            "Dia mengulurkan jari kelingkingnya. Kekanakan, tapi entah kenapa membuatmu merasa aman."

        "Rahasiakan (Bukan apa-apa kok)":
            y "Bukan apa-apa kok. Cuma capek, pelanggan hari ini ramai sekali."

            "Taeju menatapmu beberapa detik. Kamu tahu dia tidak sepenuhnya percaya."
            t "...Baiklah, kalau kamu bilang begitu."
            t "Tapi ingat, [player_name]. Aku selalu tahu kalau kamu berbohong. Aku cuma menunggu kamu siap cerita."
            "Ada nada terluka tipis di suaranya yang membuat dadamu sedikit sesak."

    "Sisa malam itu kalian habiskan dengan obrolan ringan. Bersama Taeju, dunia selalu terasa lebih pelan dan hangat."
    "Tapi jauh di dalam hatimu, kamu tahu — hari ini sesuatu telah berubah. Tiga pria, tiga dunia yang berbeda... dan kamu berdiri tepat di tengahnya."

    jump penutup_hari_1

# --- PENUTUP HARI 1 ---
label penutup_hari_1:

    stop music fadeout 2.0

    scene black
    with fade

    centered "{i}Hari Pertama — Selesai{/i}"

    # Baris debug poin (hapus/komentari saat rilis)
    "Poin Taeju: [love_taeju] | Poin Caesar: [love_caesar] | Poin Zhenya: [love_zhenya]"

    "— Bersambung —"

    return