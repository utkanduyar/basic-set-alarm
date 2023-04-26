"""Projenin amacı : Orta seviyede gelişmiş basit alarm sistemi oluşturmak başlangıç tarihi: 01.02.2021"""
import datetime
import winsound
AlarmListe = []
# noinspection NonAsciiCharacters
Uygulama_seç = str(input("Merhaba Uygulamaya Hoş Geldin Seçeneği başlatmak için alarm yaz :) : "))
if Uygulama_seç == "alarm":
    while True:
        saat1 = str(input("Lütfen Bir Saat değeri giriniz, mevcut alarmı kurunuz ya da çıkış yapınız :"))
        if not saat1:
            print("Lütfen bir saat değeri giriniz !")
        elif saat1 == "Alarmı Kur":
            if not AlarmListe:
                print("Lütfen bir alarm kurun !")
            else:
                for i in AlarmListe:
                 print("Alarm Kuruldu")
                while True:
                    anı=datetime.datetime.now()
                    sistemsaat=datetime.datetime.strftime(anı,'%X')
                    for i in AlarmListe:
                     if sistemsaat==i:
                      print("Alarm Çalıyor!!!")    
                      winsound.PlaySound('alarm3.wav',winsound.SND_FILENAME)
        elif saat1 == "çıkış":
            print("Çıkış Yapılıyor")
            break
        else:
            if 0 <= int(saat1) <= 24:
                dakika1 = str(input("bir dakika giriniz :"))
                if not dakika1:
                    print("lütfen bir dakika değeri giriniz !")
                else:
                    if 0 <= int(saat1) <= 24:
                        Anasaat = saat1 + ":" + dakika1 +":"+"00"
                        AlarmListe.append(Anasaat)
                        for i in AlarmListe:
                            print(i)
                        Alarmeklesorgu = str(
                            input(
                                "Alarm kurulmadan önce Eklemek,silmek istermisiniz yoksa kurulsunmu? çıkış yapmak "
                                "isterseniz çıkış yazın: "))
                        if Alarmeklesorgu == "ekle":
                            print("Gidiliyor")
                        elif Alarmeklesorgu == "sil":
                            for i in AlarmListe:
                                print(i)
                            listesil = str(input("silmek istediğiniz saati giriniz :"))
                            AlarmListe.remove(listesil)
                            for i in AlarmListe:
                                print(i)
                            print("Başarılı sekilde silinmiştir.")
                        elif Alarmeklesorgu == "kur":
                            if not AlarmListe:
                                print("Lütfen bir alarm kurun !")
                            else:
                                print("Alarm Kuruldu")
                                while True:
                                    anı=datetime.datetime.now()
                                    sistemsaat=datetime.datetime.strftime(anı,'%X')
                                    for i in AlarmListe:
                                     if sistemsaat==i:
                                        print("Alarm Çalıyor!!!")    
                                        winsound.PlaySound('alarm3.wav',winsound.SND_FILENAME)
                        elif Alarmeklesorgu == "çıkış":
                            AlarmListe.clear()
                            print("Uygulamadan çıkılıyor")
                            break
                    else:
                        print("lütfen geçerli bir saat değeri giriniz!")
            else:
                print("Lütfen geçerli bir saat aralığı giriniz 00 ile 23 dahil olmak üzere arasında değer lazım")
