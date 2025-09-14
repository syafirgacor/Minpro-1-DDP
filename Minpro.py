#Nama = Syafir Ahzami
#Kelas = B
#NIM = 2509116074
#Tema = Manajemen Hewan di Kebun Binatang

List_Hewan = []

while True:
    print("Manajemen Hewan Kebun Binatang Penajam")
    print("1. Tambah Hewan")
    print("2. Tampilkan Daftar Hewan")
    print("3. Hapus Hewan")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        hewan_baru = input("Masukkan nama hewan yang ingin ditambahkan: ")
        if hewan_baru in List_Hewan:
            print(f"Hewan {hewan_baru} sudah ada di daftar.")
        else:
            List_Hewan.append(hewan_baru)
            print(f"Hewan {hewan_baru} telah ditambahkan.")

    elif pilihan == '2':
        if List_Hewan:
            print("Daftar Hewan di Kebun Binatang: ")
            for hewan in List_Hewan:
                print(hewan)
        else:
            print("Belum ada hewan di kebun binatang.")

    elif pilihan == '3':
        Hapus_Hewan = (input("Masukkan Hewan yang ingin dihapus: "))
        if Hapus_Hewan in List_Hewan:
                List_Hewan.remove(Hapus_Hewan)
                print (f"Hewan {Hapus_Hewan} telah dihapus dari kebun binatang")
        else:
            print(f"Tidak ada {Hapus_Hewan} di kebun binatang.")
            
    elif pilihan == '4':
        print("terimakasih telah menggunakan program ini")
        break
