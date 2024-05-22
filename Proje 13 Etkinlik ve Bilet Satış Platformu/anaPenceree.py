class Etkinlik:
    def __init__(self, ad, tarih, mekan, toplam_bilet):
        self.ad = ad
        self.tarih = tarih
        self.mekan = mekan
        self.toplam_bilet = toplam_bilet
        self.satilan_bilet = 0

    def etkinlik_ekle(self, ad, tarih, mekan, toplam_bilet):
        return Etkinlik(ad, tarih, mekan, toplam_bilet)

    def bilet_sat(self, bilet_sayisi):
        if self.satilan_bilet + bilet_sayisi <= self.toplam_bilet:
            self.satilan_bilet += bilet_sayisi
            return True
        else:
            return False

    def bilet_al(self, kullanici, bilet_sayisi):
        if self.bilet_sat(bilet_sayisi):
            kullanici.bilet_al(self, bilet_sayisi)
            return True
        else:
            return False
class Bilet:
    def __init__(self, bilet_no, etkinlik):
        self.bilet_no = bilet_no
        self.etkinlik = etkinlik
class Kullanici:
    def __init__(self, isim, email):
        self.isim = isim
        self.email = email
        self.biletler = []

    def bilet_al(self, etkinlik, bilet_sayisi):
        for i in range(bilet_sayisi):
            yeni_bilet = Bilet(len(self.biletler) + 1, etkinlik)
            self.biletler.append(yeni_bilet)
        print(f'{bilet_sayisi} bilet satın alındı.')

    def __init__(self, isim, email):
        self.isim = isim
        self.email = email
        self.biletler = []

    def bilet_al(self, etkinlik, bilet_sayisi):
        for i in range(bilet_sayisi):
            yeni_bilet = Bilet(len(self.biletler) + 1, etkinlik)
            self.biletler.append(yeni_bilet)
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Etkinlik ve Bilet Satış Platformu')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Etkinlik Ekleme Bölümü
        self.etkinlik_ad = QLineEdit(self)
        self.etkinlik_ad.setPlaceholderText("Etkinlik Adı")
        self.layout.addWidget(self.etkinlik_ad)

        self.etkinlik_tarih = QLineEdit(self)
        self.etkinlik_tarih.setPlaceholderText("Etkinlik Tarihi")
        self.layout.addWidget(self.etkinlik_tarih)

        self.etkinlik_mekan = QLineEdit(self)
        self.etkinlik_mekan.setPlaceholderText("Etkinlik Mekanı")
        self.layout.addWidget(self.etkinlik_mekan)

        self.toplam_bilet = QLineEdit(self)
        self.toplam_bilet.setPlaceholderText("Toplam Bilet Sayısı")
        self.layout.addWidget(self.toplam_bilet)

        self.ekle_button = QPushButton('Etkinlik Ekle')
        self.ekle_button.clicked.connect(self.etkinlik_ekle)
        self.layout.addWidget(self.ekle_button)

        self.mesaj = QLabel('', self)
        self.layout.addWidget(self.mesaj)

        # Bilet Satın Alma Bölümü
        self.kullanici_isim = QLineEdit(self)
        self.kullanici_isim.setPlaceholderText("Kullanıcı İsmi")
        self.layout.addWidget(self.kullanici_isim)

        self.kullanici_email = QLineEdit(self)
        self.kullanici_email.setPlaceholderText("Kullanıcı Email")
        self.layout.addWidget(self.kullanici_email)

        self.etkinlik_sec = QComboBox(self)
        self.layout.addWidget(self.etkinlik_sec)

        self.bilet_sayisi = QLineEdit(self)
        self.bilet_sayisi.setPlaceholderText("Bilet Sayısı")
        self.layout.addWidget(self.bilet_sayisi)

        self.bilet_al_button = QPushButton('Bilet Al')
        self.bilet_al_button.clicked.connect(self.bilet_al)
        self.layout.addWidget(self.bilet_al_button)

        self.etkinlikler = []

    def etkinlik_ekle(self):
        ad = self.etkinlik_ad.text()
        tarih = self.etkinlik_tarih.text()
        mekan = self.etkinlik_mekan.text()
        toplam_bilet = int(self.toplam_bilet.text())

        yeni_etkinlik = Etkinlik(ad, tarih, mekan, toplam_bilet)
        self.etkinlikler.append(yeni_etkinlik)

        self.etkinlik_sec.addItem(ad)
        self.mesaj.setText(f'{ad} etkinliği başarıyla eklendi.')

    def bilet_al(self):
        kullanici_isim = self.kullanici_isim.text()
        kullanici_email = self.kullanici_email.text()
        etkinlik_ad = self.etkinlik_sec.currentText()
        bilet_sayisi = int(self.bilet_sayisi.text())

        # Kullanıcı oluşturma
        kullanici = Kullanici(kullanici_isim, kullanici_email)

        # Etkinliği bulma
        etkinlik = next((e for e in self.etkinlikler if e.ad == etkinlik_ad), None)

        if etkinlik:
            if etkinlik.bilet_al(kullanici, bilet_sayisi):
                QMessageBox.information(self, 'Başarılı', f'{kullanici_isim} için {bilet_sayisi} bilet başarıyla satın alındı.')
            else:
                QMessageBox.warning(self, 'Başarısız', 'Yeterli bilet yok.')
        else:
            QMessageBox.warning(self, 'Başarısız', 'Etkinlik bulunamadı.')

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
