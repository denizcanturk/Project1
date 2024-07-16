from projectLibs.csvmanager import CSVFileManager
from projectLibs.jsonmanager import JSONFileManager
from projectLibs.txtmanager import TextFileManager
from tkinter.filedialog import asksaveasfilename

import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime as dt

class StokKontrol(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stok Kontrol Formu")
        self.geometry("700x400")
        self.create_widgets()
        self.csvmanager = CSVFileManager()
        self.txtmanager = TextFileManager()
        self.jsonmanager = JSONFileManager()

    def degerOku(self):
        file_name = asksaveasfilename()

        data=[self.grMalzemeStokKodu.get(),
            self.grMalzemeAdi.get(),
            self.grMiktar.get(),
            self.grBirim.get(),
            self.grGiristarihi.get(),
            self.grMalzemeUretimTarihi.get(),
            self.grLotNumarasi.get(),
            self.grMalzemeSonKullanmaTarihi.get()
        ]
        print(data)
        self.csvmanager.write_to_file(file_name,data=data)

    def formTemizle(self):
        self.grMalzemeStokKodu.delete(0,tk.END)
        self.grMalzemeAdi.delete(0,tk.END)
        self.grMiktar.delete(0,tk.END)
        self.grBirim.delete(0,tk.END)
        self.grGiristarihi.set_date(dt.datetime.today())
        self.grMalzemeUretimTarihi.delete(0,tk.END)
        self.grLotNumarasi.delete(0,tk.END)
        self.grMalzemeSonKullanmaTarihi.set_date(dt.datetime.today())

    def updateBirimCombo(self, event=None):
        val = self.grMalzemeAdi.get()
        if val == "Polyester" or val=="PBA":
            self.grBirim.set("kg")

        if val == "ABS" :
            self.grBirim.set("metre")

        if val == "Silikon":
            self.grBirim.set("adet")

    def dateChange(self, event=None):
        date1 = self.grGiristarihi.get_date()
        date2 = self.grMalzemeSonKullanmaTarihi.get_date()
        print("Giris Tarihi :", date1,"-//- Son Kullanma Tarihi :", date2)
        #print(str(date1-date2).split(" ")[0]) #Burda ne yaptığımı anlamaya çalışın lütfen...

    #--------------------------------------
    #Create Tabs on Main Window
    def create_widgets(self):
        notebook = ttk.Notebook(self)
        self.tab1=ttk.Frame(notebook)
        self.tab2= ttk.Frame(notebook)

        notebook.add(self.tab1, text="Stok Giris")
        notebook.add(self.tab2,text="Stok Çıkış")
        notebook.pack(expand=True, fill="both")

        self.create_tab1widgets()
        self.create_tab2widgets()
    #--------------------------------------

    def create_tab1widgets(self):
        #--------------------------------------
        # Get tab1 Widgets together

        #Malzeme Giris Stok Kod Etiket ve Giris Aracı
        self.etMalzemeStokKodu = tk.Label(self.tab1, text="Malzeme Stok Kodu")
        self.etMalzemeStokKodu.grid(row=0, column=0,padx=5, pady=5, sticky="w")

        self.grMalzemeStokKodu = tk.Entry(self.tab1, bd=0)
        self.grMalzemeStokKodu.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        #Malzeme Adı Etiket ve Giris Aracı
        self.etMalzemeAdi = tk.Label(self.tab1, text="Malzeme Adı")
        self.etMalzemeAdi.grid(row=1, column=0,padx=5, pady=5, sticky="w")

        self.MalzemeAdlari = ["Polyester", "Silikon", "ABS", "PBA", "Cam Elyafı"]
        self.grMalzemeAdi = ttk.Combobox(self.tab1, values=self.MalzemeAdlari)
        self.grMalzemeAdi.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        self.grMalzemeAdi.bind("<<ComboboxSelected>>", self.updateBirimCombo)

        #Miktar Etiket ve Giris Aracı
        self.etMiktar = tk.Label(self.tab1, text="Miktar")
        self.etMiktar.grid(row=2, column=0,padx=5, pady=5, sticky="w")

        self.grMiktar = tk.Spinbox(self.tab1, from_=0, to=1000, bd=0, increment=0.1)
        self.grMiktar.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        #Birim Etiket ve Giris Aracı
        self.etBirim = tk.Label(self.tab1, text="Birim")
        self.etBirim.grid(row=3, column=0,padx=5, pady=5, sticky="w")

        birimler = ["kg", "adet", "metre"]
        self.grBirim = ttk.Combobox(self.tab1, values=birimler)
        self.grBirim.grid(row=3, column=1, padx=5, pady=5, sticky="we")


        #Giris Tarihi Etiket ve Giris Aracı
        self.etgirisTarihi = tk.Label(self.tab1, text="Giris Tarihi")
        self.etgirisTarihi.grid(row=0, column=2,padx=5, pady=5, sticky="w")

        self.grGiristarihi = DateEntry(self.tab1, date_pattern="dd-mm-yy")
        self.grGiristarihi.grid(row=0, column=3, padx=5, pady=5, sticky="we")
        self.grGiristarihi.bind("<<DateEntrySelected>>",self.dateChange)

        #Malzeme Üretim Tarihi Etiket ve Giris Aracı
        self.etMalzemeUretimTarihi = tk.Label(self.tab1, text="Malzeme Üretim Tarihi")
        self.etMalzemeUretimTarihi.grid(row=1, column=2,padx=5, pady=5, sticky="w")

        self.grMalzemeUretimTarihi = tk.Entry(self.tab1, bd=0)
        self.grMalzemeUretimTarihi.grid(row=1, column=3, padx=5, pady=5, sticky="we")

        #Lot Numarası Etiket ve Giris Aracı
        self.etLotNumarasi = tk.Label(self.tab1, text="Lot Numarası")
        self.etLotNumarasi.grid(row=2, column=2,padx=5, pady=5, sticky="w")

        self.grLotNumarasi = tk.Entry(self.tab1, bd=0)
        self.grLotNumarasi.grid(row=2, column=3, padx=5, pady=5, sticky="we")


        #Malzeme Son Kullanama Tarihi Etiket ve Giris Aracı
        self.etMalzemeSonKullanmaTarihi = tk.Label(self.tab1, text="Malzeme Son Kullanma Tarihi")
        self.etMalzemeSonKullanmaTarihi.grid(row=3, column=2,padx=5, pady=5, sticky="w")

        self.grMalzemeSonKullanmaTarihi = DateEntry(self.tab1, date_pattern="dd-mm-yy")
        self.grMalzemeSonKullanmaTarihi.grid(row=3, column=3, padx=5, pady=5, sticky="we")
        self.grMalzemeSonKullanmaTarihi.bind("<<DateEntrySelected>>",self.dateChange)

        #Tab1 Buttonlar
        # Deger Oku ve degerleri Temizle
        self.btnDegerOku = tk.Button(self.tab1, text= "Deger Oku",command=self.degerOku)
        self.btnDegerOku.grid(row=4, column=2)

        self.btnDegerSil = tk.Button(self.tab1, text= "Temizle", command=self.formTemizle)
        self.btnDegerSil.grid(row=4, column=3, padx=5, pady=5, sticky="we")

    #--------------------------------------
    def create_tab2widgets(self):
        #Tab2 Widgetlari
        #Üretime Veriliş Tarihi
        self.etUretimeVerilisTarihi = tk.Label(self.tab2, text="Üretime Veriliş Tarihi")
        self.etUretimeVerilisTarihi.grid(row=0, column=0, sticky="w")

        grUretimeVerilisTarihi = DateEntry(self.tab2, date_pattern="dd-mm-yy")
        grUretimeVerilisTarihi.grid(row=0, column=1,padx=5, pady=5, sticky="we")


        #Çıktı Miktarı
        self.etCiktiMiktari = tk.Label(self.tab2, text="Cikti Miktari")
        self.etCiktiMiktari.grid(row=1, column=0,padx=5, pady=5, sticky="w")

        self.grCiktiMiktari = tk.Entry(self.tab2, bd=0)
        self.grCiktiMiktari.grid(row=1, column=1, padx=5, pady=5, sticky="we")


        #Çıktı Lot Numarası
        self.etCiktiLotNumarasi = tk.Label(self.tab2, text="Cikti Lot Numarası")
        self.etCiktiLotNumarasi.grid(row=2, column=0,padx=5, pady=5, sticky="w")

        self.grCiktiLotNumarasi = tk.Entry(self.tab2, bd=0)

        self.grCiktiLotNumarasi.grid(row=2, column=1, padx=5, pady=5, sticky="we")


#pencere.mainloop()

uygulama = StokKontrol()
uygulama.mainloop()

"""
Early testing
Defect clustering
Testing is context dependent
Testing shows presence of defects
Absence of error fallacy
Exhaustive testing is impossible
Pesticide paradox
"""