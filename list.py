# Lokasi Wisata Kutai Barat
kutaibarat_alam = ["1.Jantur Mapan" ,"2.Danau Aco" ,"3.Kersik Luway"]
kutaibarat_kuliner = ["1.Keraton Resto & Art Gallery" ,"2.Grand Family Hotel"]
kutaibarat_keluarga = ["1.Taman Budaya Sendawar" ,"2.CIA Wisata"]
kutaibarat_belanja = [".Pasar Olah Bebaya"]
kutaibarat_sejarah = ["1.Lamin Tolan" ,"2.Pura Jagatnatha Sendawar Agung"]
kutaibarat_religi = ["1.Islamic Center"]

# Lokasi Wisata Kutai Kartanegara
kutaikartanegara_alam = ["1.Hutan Pinus Samboja" ,"2.Bukit Bangkirai"]
kutaikartanegara_kuliner = ["1.Rumah Makan Minang Asli" ,"2.Rumah Makan Tepian Pandan"]
kutaikartanegara_keluarga = ["1.Ladang Buaya Tenggarong"]
kutaikartanegara_sejarah = ["1.Museum Mulawarman" ,"2.Museum Kayu Tua Himba"]
kutaikartanegara_religi = ["1.Masjid Agung Sultan Sulaiman" ,"2.Masjid Jami' Adji Amir Hasanoeddin"]

# Lokasi Wisata Berau
berau_alam = ["1.Labuan Cermin" ,"2.Pulau Derawan" ,"3.Pulau Kakaban"]
berau_kuliner = ["1.Kahyangan Seafood and Chinese Restaurant" ,"2.Rumah Makan Sari Ponti"]
berau_keluarga = ["1.Taman Wisata Bumi Bangun Lestari" ,"2.Taman Cendana" ,"3.Taman Sanggam"]
berau_belanja = ["1.Pasar Adji Dilayas"]
berau_sejarah = ["1.Keraton Sambaliung" ,"2.Keraton Gunung Tabur"]
berau_religi = ["1.Masjid Agung Baitul Hikmah" ,"2.Kelenteng Tri Dharma"]

# Lokasi Wisata di Kutai_Timur
kutaitimur_keluarga = ("\n1.Taman Nasional Kutai \n2.Aquatiq \n3.Taman Nasional Kutai Mentoko")
kutaitimur_kuliner = ("\n1.Taman Bersemi sangatta")
kutaitimur_alam = ("\n1.Wisata Alam Pervab TN Kutai \n2.Danau Senal \n3.Goa Karst Ampanas")
kutaitimur_sejarah = ("\n1.Kawasan Goa Gunung Kombeng")

elif pilih == "2":
        kabupaten()
        print("Masukkan angka sesuai dengan Kabupaten yang ingin dikunjungi!")
        kabupaten_pilihan = input("Kabupaten pilihan: ")
        if kabupaten_pilihan == "1":
            print("\n1.Wisata Alam\n2.Wisata Kuliner\n3.Wisata Keluarga\n4.Wisata Belanja\n5.Wisata Sejarah\n6.Wisata Religi")
            kategori_pilihan = input("Masukkan Kategori Wisata yang ingin dikunjungi: ")
            if kategori_pilihan == "1":
                print(" ")
                print(" ")
                print("Berikut Wisata Alam yang ada di Kutai Barat")
                for i in kutaibarat_alam:
                    print (i)
                alam_kutaibarat = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if alam_kutaibarat == "1":
                    print(" ")
                    print("Lokasi air terjun yang dikelilingi tebing batu dan pepohonan")
                    print("Lokasi: Jalan Sengkereaq Lacaaq, Linggan Mapan")
                elif alam_kutaibarat == "2":
                    print(" ")
                    print("Surga yang tersembunyi yang jauh dari pemukiman warga")
                    print("Lokasi: kampung linggang melateh, kecamatan linggang bigung, 20 km dari pusat kota sendawar")
                elif alam_kutaibarat == "3":
                    print(" ")
                    print("Kersik Luway adalah Cagar alam dengan perumahan warga berjarak sekitar 5km")
                    print("Lokasi: Kecamatan Skolaq darat")
                else: ulang()
            elif kategori_pilihan == "2":
                print(" ")
                print(" ")
                print("Berikut Wisata Kuliner yang ada di Kutai Barat")
                for i in kutaibarat_kuliner:
                    print (i)
                kuliner_kutaibarat = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if kuliner_kutaibarat == "1":
                    print(" ")
                    print("Salah satu rumah makan yang harus kamu kunjungi ketika di kutai barat")
                    print("Lokasi: Jalan Wolter Monginsidi No.45, Timbau, Tenggarong")
                elif kuliner_kutaibarat == "2":
                    print(" ")
                    print("Makanan yang disajikan di hotel ini wajib anda coba saat menginap di hotel ini")
                    print("Lokasi: Wilayah Barong tongkok, Jalan Antasari")
                else: ulang()
            elif kategori_pilihan == "3":
                print(" ")
                print(" ")
                print("Berikut Wisata Keluarga yang ada di Kutai Barat")
                for i in kutaibarat_keluarga:
                    print(i)
                keluarga_kutaibarat = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if keluarga_kutaibarat == "1":
                    print(" ")
                    print("Taman budaya ini menawarkan rumah khas yaitu rumah lamin dan juga biasanya menunjukkan tarian khas dayak")
                    print("Lokasi: Jalan Sendawar raya, kampung sendawar, Kecamatan Barong tangkok")
                elif keluarga_kutaibarat == "2":
                    print(" ")
                    print("Tempat wisata alam terbuka yang dimana pengunjungnya dapat menggunakan ATV")
                    print("Lokasi: Linggang melateh, kecamatan linggang bigung")
                else: ulang()
            elif kategori_pilihan == "4":
                print(" ")
                print(" ")
                print("Berikut Wisata Belanja yang ada di Kutai Barat")
                for i in kutaibarat_belanja:
                    print(i)
                belanja_kutaibarat = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if belanja_kutaibarat == "1":
                    print(" ")
                    print("Pasar ini merupakan pasar yang cukup ramai dikunjungi oleh para pembeli, mengingat keaneka ragaman produk yang dipasarkan")
                    print("Lokasi: Sendawar, Kutai Barat")
                else: ulang()
            elif kategori_pilihan == "5":
                print(" ")
                print(" ")
                print("Berikut Wisata Sejarah yang ada di Kutai Barat")
                for i in kutaibarat_sejarah:
                    print (i)
                sejarah_kutaibarat = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if sejarah_kutaibarat == "1":
                    print(" ")
                    print("Lamin paling tua yang unik dan asli di Kutai Barat dengan usia kurang lebih 200 tahun")
                    print("Lokasi: Lambing, Kecamatan Muara Lawa")
                elif sejarah_kutaibarat == "2":
                    print(" ")
                    print("Adalah satu satunya tempat ibadah umat hindu di kutai barat")
                    print("Lokasi: Jl. Sapinq RT. 009 Busur, Barong Tongkok, Simpang Raya, Barong Tongkok")
                else: ulang()
            elif kategori_pilihan == "6":
                print(" ")
                print(" ")
                print("Berikut Wisata Religi yang ada di Kutai Barat")
                for i in kutaibarat_religi:
                    print (i)
                religi_kutaibarat = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if religi_kutaibarat == "1":
                    print(" ")
                    print("Tempat ibadah terbesar bagi Umat Islam di Kutai Barat dengan fasilitas multi fungsi")
                    print("Lokasi: Jl.KH Dewantara Kelurahan Melak Ulu Kecamatan Melak")
                else: ulang()
        elif kabupaten_pilihan == "2":
            print("\n1.Wisata Alam\n2.Wisata Kuliner\n3.Wisata Keluarga\n4.Wisata Sejarah\n5.Wisata Religi")
            kategori_pilihan = input("Masukkan Kategori Wisata yang ingin dikunjungi: ")
            if kategori_pilihan == "1":
                print(" ")
                print(" ")
                print("Berikut Wisata Alam yang ada di Kutai Kartanegara")
                for i in kutaikartanegara_alam:
                    print(i)
                alam_kutaikartanegara = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if alam_kutaikartanegara == "1":
                    print(" ")
                    print("Pemandangan di hutan ini begitu cantik dan indah sehingga memanjakan mata anda")
                    print("Lokasi: Samboja")
                elif kategori_pilihan == "2":
                    print(" ")
                    print("Wisata ini menawarkan pesona hutan hujan tropis yang masih alami")
                    print("Lokasi: Kecamatan Samboja")
                else: ulang()
            elif kategori_pilihan == "2":
                print(" ")
                print(" ")
                print("Berikut Wisata Kuliner yang ada di Kutai Kartanegara")
                for i in kutaikartanegara_kuliner:
                    print(i)
                kuliner_kutaikartanegara = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if kuliner_kutaikartanegara == "1":
                    print(" ")
                    print("Salah satu rumah makan minang asli yang ada di Kutai Kartanegara")
                    print("Lokasi: Jl. Robert Wolter Mongisidi, Timbau, Kec. Tenggarong")
                elif kuliner_kutaikartanegara == "2":
                    print(" ")
                    print("Rumah makan yang disertai dengan pemandangan sungai mahakam")
                    print("Lokasi: Jln. Wolter Monginsidi, Tenggarong")
                else: ulang()
            elif kategori_pilihan == "3":
                print(" ")
                print(" ")
                print("Berikut Wisata Keluarga yang ada di Kutai Kartanegara")
                for i in kutaikartanegara_keluarga:
                    print(i)
                keluarga_kutaikartanegara = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if keluarga_kutaikartanegara == "1":
                    print(" ")
                    print("Lokasi ini sering dijadikan sebagai lokasi acara gathering keluarga atau kantor, terdapat wahana outbond di dalamnya")
                    print("Lokasi: Jl.H. Bachrin Seman, Mangkurawang, Kecamatan Tenggarong")
                else: ulang()
            elif kategori_pilihan == "4":
                print(" ")
                print(" ")
                print("Berikut Wisata Sejarah yang ada di Kutai kartanegara")
                for i in kutaikartanegara_sejarah:
                    print(i)
                sejarah_kutaikartanegara = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if sejarah_kutaikartanegara == "1":
                    print(" ")
                    print("Arsitektur Bangunan gedung ini mengadopsi dari arsitektur tradisional suku dayak yang ada di Kutai")
                    print("Lokasi: Jl. Tepian Pandan, Panji, Kecamatan Tenggarong")
                elif sejarah_kutaikartanegara == "2":
                    print(" ")
                    print("Seluruh arsitektur bangunan terbuat dari kayu berkualitas terbaik yang membentuk rumah adat panggung khas Kalimantan")
                    print("Lokasi: Jl.Museum Kayu, Panji, Kecamatan Tenggarong")
                else: ulang()
            elif kategori_pilihan == "5":
                print(" ")
                print(" ")
                print("Berikut Wisata Religi yang ada di Kutai Kartanegara")
                for i in kutaikartanegara_religi:
                    print(i)
                religi_kutaikartanegara = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if religi_kutaikartanegara == "1":
                    print(" ")
                    print("Salah Satu Masjid Besar di Kutai Kartanegara")
                    print("Lokasi: Jl.KH Dewantara, Panji, Tenggarong")
                elif religi_kutaikartanegara == "2":
                    print(" ")
                    print("Salah satu masjid bersejarah di Indonesia")
                    print("Lokasi: Jl.Panji, Tenggarong")
                else: ulang()
        elif kabupaten_pilihan == "3":
            print("\n1.Wisata Alam\n2.Wisata Kuliner\n3.Wisata Keluarga\n4.Wisata Belanja\n5.Wisata Sejarah\n6.Wisata Religi")
            kategori_pilihan = input("Masukkan Kategori Wisata yang ingin dikunjungi: ")
            if kategori_pilihan == "1":
                print(" ")
                print(" ")
                print("Berikut Wisata Alam yang ada di Berau")
                for i in berau_alam:
                    print(i)
                alam_berau = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if alam_berau == "1":
                    print(" ")
                    print("Danau dua rasa yaitu tawar dan asin, serta airnya yang sangat jernih dan dingin membuat banyak orang tertarik mengunjunginya")
                    print("Lokasi: Kecamatan biduk biduk")
                elif alam_berau == "2":
                    print(" ")
                    print("Memiliki sejumlah objek wisata bahari menawan, salah satunya Taman Bawah Laut yang diminati Wisatawan mancanegara")
                    print("Lokasi: Kepulauan Derawan, Kabupaten Berau")
                elif alam_berau == "3":
                    print(" ")
                    print("Terkenal dengan ubur ubur yang tidak menyengat dengan jumlah yang sangat banyak")
                    print("Lokasi: Kepulauan Derawan, Kabupaten Berau")
                else: ulang()
            elif kategori_pilihan == "2":
                print(" ")
                print(" ")
                print("Berikut Wisata Kuliner yang ada di Berau")
                for i in berau_kuliner:
                    print(i)
                kuliner_berau = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if kuliner_berau == "1":
                    print(" ")
                    print("Salah satu Tempat Makan dengan menu laut dan Chinese food terbaik di berau")
                    print("Lokasi: Jl Akb Sanipah, Kecamatan Tanjung Redeb")
                elif kuliner_berau == "2":
                    print(" ")
                    print("Salah Satu Rumah makan Seafood dan Chinese food di berau")
                    print("Lokasi: Jl.Durian, Kecamatan Tanjung Redeb")
                else: ulang()
            elif kategori_pilihan == "3":
                print(" ")
                print(" ")
                print("Berikut Wisata Keluarga yang ada di Berau")
                for i in berau_keluarga:
                    print(i)
                keluarga_berau = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if keluarga_berau == "1":
                    print(" ")
                    print("Taman dipenuhi dengan pohon karet yang asri dan banyak zona nyaman untuk bermain serta arena outbond")
                    print("Lokasi: Kecamatan Sambaliung, Trans Bangun, 5Km dari Pusat Kota Tanjung Redeb")
                elif keluarga_berau == "2":
                    print(" ")
                    print("Taman dengan banyak Fasilitas disekelilingnya seperti lapangan bola, Vollyball, Tennis ball, serta Gedung Kantor Bupati Berau")
                    print("Lokasi: Jl.APT Pranoto, Karang Ambun, Kecamatan Tanjung Redeb")
                elif keluarga_berau == "3":
                    print(" ")
                    print("Salah Satu taman yang banyak dikunjungi serta banyak penjual makanan disekitar dan bersebelahan dengan Gedung Perpustakaan Umum")
                    print("Lokasi: Jl.Milono, Kelurahan Bugis, Kecamatan Tanjung Redeb")
                else: ulang()
            elif kategori_pilihan == "4":
                print(" ")
                print(" ")
                print("Berikut Wisata Belanja yang ada di Berau")
                for i in berau_belanja:
                    print(i)
                belanja_berau = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if belanja_berau == "1":
                    print(" ")
                    print("Pasar tradisional yang ada di Berau, Biasanya digunakan sebagai tempat diselenggarakannya acara EXPO tahunan")
                    print("Lokasi: Jl.HM Raden Ayoeb, Kabupaten Berau")
                else: ulang()
            elif kategori_pilihan == "5":
                print(" ")
                print(" ")
                print("Berikut Wisata Sejarah yang ada di Berau")
                for i in berau_sejarah:
                    print(i)
                sejarah_berau = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if sejarah_berau == "1":
                    print(" ")
                    print("Keraton Sambaliung adalah bukti sejarah adanya kesultanan Sambaliung, Kemudian dialih fungsikan menjadi museum yang menyimpan banyak benda bersejarah")
                    print("Lokasi: Jl.St Aminuddin, Kecamatan Sambaliung")
                elif sejarah_berau == "2":
                    print(" ")
                    print("Sama Halnya dengan Keraton di Sambaliung, lokasinya pun hampir bersebrangan dengan Keraton Sambaliung, dipisahkan oleh sungai kelay")
                    print("Lokasi: Kecamatan Gunung Tabur")
                else: ulang()
            elif kategori_pilihan == "6":
                print(" ")
                print(" ")
                print("Berikut Wisata Religi yang ada di Berau")
                for i in berau_religi:
                    print(i)
                religi_berau = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if religi_berau == "1":
                    print(" ")
                    print("Salah Satu Masjid Terbesar yang ada di Berau")
                    print("Lokasi: Jl.Karang Ambun, Kecamatan Tanjung Redeb")
                elif religi_berau == "2":
                    print(" ")
                    print("Satu satunya tempat beribadah bagi umat agama konghucu di Berau")
                    print("Lokasi: Jl.Kapten Tendean, Kecamatan Tanjung Redeb")
                else: ulang()
        elif kabupaten_pilihan == "4":
            print("\n1.Wisata Keluarga\n2.Wisata Kuliner\n3.Wisata Alam\n4.Wisata Sejarah")
            kategori_pilihan = input("Masukkan Kategori Wisata yang ingin dikunjungi: ")
            if kategori_pilihan == "1":
                print(" ")
                print(" ")
                print("Berikut Wisata Keluarga yang ada di Kutai Timur")
                for i in kutaitimur_keluarga:
                    print(i)
                keluarga_kutaitimur = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if keluarga_kutaitimur == "1":
                    print(" ")
                    print("Kawasan konservasi yang melindungi dan mengawetkan ekosistem hutan hujan tropis dataran rendah yang kaya flora dan fauna")
                    print("Lokasi: Kabupaten Kutai Timur")
                elif keluarga_kutaitimur == "2":
                    print(" ")
                    print("Selain Mempunyai pemandangan indah ke laut Makassar pantai ini juga memiliki pemandangan hutan bakau yang mengelilinginya")
                    print("Lokasi: Desa Singa Gembara, Kecamatan Sangatta utara")
                elif keluarga_kutaitimur == "3":
                    print(" ")
                    print("Adalah Tempat penelitian Orang utan di Kutai timur")
                    print("Lokasi: 1 jam dengan ketinting dari kota sangatta ke arah hulu sungai Sangatta")
                else: ulang()
            elif kategori_pilihan == "2":
                print(" ")
                print(" ")
                print("Berikut Wisata Kuliner yang ada di Kutai Timur")
                for i in kutaitimur_kuliner:
                    print(i)
                kuliner_kutaitimur = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if kuliner_kutaitimur == "1":
                    print(" ")
                    print("Merupakan kawasan wisata belanja sekaligus ruang terbuka dan wadah hiburan bagi masyarakat. Berbagai jenis jajanan dijual di lapangan Eks STQ tersebut")
                    print("Lokasi: Sangatta Utara, Kutai Timur")
                else: ulang()
            elif kategori_pilihan == "3":
                print(" ")
                print(" ")
                print("Berikut Wisata Alam yang ada di Kutai Timur")
                for i in kutaitimur_alam:
                    print(i)
                alam_kutaitimur = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if alam_kutaitimur == "1":
                    print(" ")
                    print("Adalah Tempat penelitian Orang utan oleh universitas luar negeri di Kutai timur")
                    print("Lokasi: 1 jam dengan ketinting dari kota sangatta ke arah hulu sungai Sangatta")
                elif alam_kutaitimur == "2":
                    print(" ")
                    print("Adalah Taman Rekreasi Air di Kutai timur")
                    print("Lokasi: Desa, Nehes Liah Bing, Kec. Muara Wahau")
                elif alam_kutaitimur == "3":
                    print(" ")
                    print("Wisata alam goa yang menyuguhkan pemandangan formasi batuan Stalagtit dan Stalagmit")
                    print("Lokasi: Desa Pengadaan, Kecamatan Karangan")
                else: ulang()
            elif kategori_pilihan == "4":
                print(" ")
                print(" ")
                print("Berikut Wisata Sejarah yang ada di Kutai Timur")
                for i in kutaitimur_sejarah:
                    print(i)
                sejarah_kutaitimur = input("Masukkan angka yang diinginkan untuk melihat info seputar tempat wisata yang dipilih: ")
                if sejarah_kutaitimur == "1":
                    print(" ")
                    print("Cukup Menarik untuk dikunjungi Wisatawan, di dalam goa terdapat patung peninggalan kerajaan kutai")
                    print("Lokasi: Desa Pantun, Kecamatan Muara Wahau")
                else: ulang()