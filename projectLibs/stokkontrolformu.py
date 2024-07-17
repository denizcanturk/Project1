
from .csvmanager import CSVFileManager
from .txtmanager import TextFileManager
from .jsonmanager import JSONFileManager
from tkinter.filedialog import asksaveasfilename
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import datetime as dt

#TODO : Form okunurken boş alan kalmış mı kontrol edilecek
#       Formalara girilen değer aralıkları kontrol edilcek mi?
#       Formdan okunan değerlerin dosyaya yazılması için fonksiyon implement edilecek
#       Dosya seçebilmek için FileDialog implement edilecek.
#       Eğer self.dosya elemanına girili bir dosya seçili değilse dosya seç yaptırılacak
#       

class StokKontrolFormu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stok Kontrol Formu")
        self.geometry("700x400")
        
        self.txtManager = TextFileManager()
        self.csvManager = CSVFileManager()
        self.jsonManager = JSONFileManager()
        self.fileName = ""
        self.data = []

        self.create_widgets()
        self.create_menu_bar()

    def create_widgets(self):
        notebook = ttk.Notebook(self)
        self.tab1 = ttk.Frame(notebook)
        notebook.add(self.tab1, text="Stok Giris")

        self.tab2 = ttk.Frame(notebook)
        notebook.add(self.tab2, text="Stok Çıkış")

        notebook.pack(expand=True, fill="both")

        # Tab1 Widgets
        self.create_tab1_widgets()
        # Tab2 Widgets
        self.create_tab2_widgets()

    def create_menu_bar(self):
        menubar = tk.Menu()
        file_menu= tk.Menu(menubar, tearoff=False)
        edit_menu= tk.Menu(menubar, tearoff=False)
        settings_menu = tk.Menu(menubar, tearoff=False)
        about_menu = tk.Menu(menubar, tearoff=False)

        menubar.add_cascade(menu=file_menu, label="File")
        menubar.add_cascade(menu=edit_menu, label="Edit")
        menubar.add_cascade(menu=settings_menu, label="Settings")
        

        self.config(menu=menubar)
        #File Menu
        file_menu.add_command(label="Temizle", accelerator="Ctrl+T", command=self.formTemizle)
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", accelerator="Ctrl+X", command=self.destroy)
        self.bind_all("<Control-T>", self.formTemizle)
        self.bind_all("<Control-X>", self.destroy)

        #Edit Menu
        edit_menu.add_radiobutton(label="Radio Box", command=None, variable=None)

        #Settings menu
        cek= tk.BooleanVar()
        settings_menu.add_checkbutton(label="Checkeyim mi?", command=None, variable=cek)
        settings_menu.add_cascade(menu=about_menu, label="...")

        #About Menu- Sub Menu and New Form show up!
        about_menu.add_command(label="About...",command=self.create_about_window)
        
    def create_about_window(self):
        sec_window = tk.Toplevel()
        sec_window.resizable(False,False)
        sec_window.title("Hakkında")
        sec_window.geometry("250x100")
        tk.Label(sec_window, text="This is a about section \nfor the program which is not \ncared by anyone...").pack(anchor="center")

    def create_tab1_widgets(self):
        tk.Label(self.tab1, text="Malzeme Stok Kodu").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.grMalzemeStokKodu = tk.Entry(self.tab1, bd=0)
        self.grMalzemeStokKodu.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        tk.Label(self.tab1, text="Malzeme Adı").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        MalzemeAdlari = ["Polyester", "Silikon", "ABS", "PBA", "Cam Elyafı"]
        self.grMalzemeAdi = ttk.Combobox(self.tab1, values=MalzemeAdlari)
        self.grMalzemeAdi.grid(row=1, column=1, padx=5, pady=5, sticky="we")
        self.grMalzemeAdi.bind("<<ComboboxSelected>>", self.updateBirimCombo)

        tk.Label(self.tab1, text="Miktar").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.grMiktar = tk.Spinbox(self.tab1, from_=0, to=1000, bd=0, increment=0.1)
        self.grMiktar.grid(row=2, column=1, padx=5, pady=5, sticky="we")

        tk.Label(self.tab1, text="Birim").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        birimler = ["kg", "adet", "metre"]
        self.grBirim = ttk.Combobox(self.tab1, values=birimler)
        self.grBirim.grid(row=3, column=1, padx=5, pady=5, sticky="we")

        tk.Label(self.tab1, text="Giris Tarihi").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.grGiristarihi = DateEntry(self.tab1, date_pattern="dd-mm-yy")
        self.grGiristarihi.grid(row=0, column=3, padx=5, pady=5, sticky="we")

        tk.Label(self.tab1, text="Malzeme Üretim Tarihi").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.grMalzemeUretimTarihi = tk.Entry(self.tab1, bd=0)
        self.grMalzemeUretimTarihi.grid(row=1, column=3, padx=5, pady=5, sticky="we")

        tk.Label(self.tab1, text="Lot Numarası").grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.grLotNumarasi = tk.Entry(self.tab1, bd=0)
        self.grLotNumarasi.grid(row=2, column=3, padx=5, pady=5, sticky="we")

        tk.Label(self.tab1, text="Malzeme Son Kullanma Tarihi").grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.grMalzemeSonKullanmaTarihi = DateEntry(self.tab1, date_pattern="dd-mm-yy")
        self.grMalzemeSonKullanmaTarihi.grid(row=3, column=3, padx=5, pady=5, sticky="we")

        self.tab1Frame = tk.Frame(self.tab1)
        self.tab1Frame.grid(row=4, column=0, columnspan=4,pady=15, sticky="we")

        tk.Button(self.tab1Frame, text="Deger Oku", command=self.degerOku).pack(side=tk.RIGHT, padx=5)
        tk.Button(self.tab1Frame, text="Temizle", command=self.formTemizle).pack(side=tk.RIGHT, padx=5)
        tk.Button(self.tab1Frame, text="Dosyaya Yaz", command=self.degerOku).pack(side=tk.RIGHT, padx=5)
        tk.Button(self.tab1Frame, text="Temizle", command=self.formTemizle).pack(side=tk.RIGHT, padx=5)

    def create_tab2_widgets(self):
        tk.Label(self.tab2, text="Üretime Veriliş Tarihi").grid(row=0, column=0, sticky="w")
        self.grUretimeVerilisTarihi = DateEntry(self.tab2, date_pattern="dd-mm-yy")
        self.grUretimeVerilisTarihi.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        tk.Label(self.tab2, text="Cikti Miktari").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.grCiktiMiktari = tk.Entry(self.tab2, bd=0)
        self.grCiktiMiktari.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        tk.Label(self.tab2, text="Cikti Lot Numarası").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.grCiktiLotNumarasi = tk.Entry(self.tab2, bd=0)
        self.grCiktiLotNumarasi.grid(row=2, column=1, padx=5, pady=5, sticky="we")

    def degerOku(self):
        file_name = asksaveasfilename(title="Please Select a File", 
                                      initialdir="./",
                                      defaultextension="csv",
                                      filetypes=[("Text Files","*.txt"),
                                                 ("json Files", "*.json"),
                                                 ("CSV Files","*.csv")
                                                 ]
                                      )
        self.data = [
            self.grMalzemeStokKodu.get(),
            self.grMalzemeAdi.get(),
            self.grMiktar.get(),
            self.grBirim.get(),
            self.grGiristarihi.get(),
            self.grMalzemeUretimTarihi.get(),
            self.grLotNumarasi.get(),
            self.grMalzemeSonKullanmaTarihi.get()
        ]
        self.csvManager.write_to_file(file_name,data=self.data)
        print(self.data)

    def formTemizle(self):
        self.grMalzemeStokKodu.delete(0, tk.END)
        self.grMalzemeAdi.delete(0, tk.END)
        self.grMiktar.delete(0, tk.END)
        self.grBirim.delete(0, tk.END)
        self.grGiristarihi.set_date(dt.datetime.today())
        self.grMalzemeUretimTarihi.delete(0, tk.END)
        self.grLotNumarasi.delete(0, tk.END)
        self.grMalzemeSonKullanmaTarihi.set_date(dt.datetime.today())

    def updateBirimCombo(self, event=None):
        val = self.grMalzemeAdi.get()
        if val == "Polyester":
            self.grBirim.set("kg")
        elif val == "Silikon":
            self.grBirim.set("adet")
        elif val == "ABS":
            self.grBirim.set("metre")
        # Add more conditions as needed


if __name__ == "__main__":
    print("This file not intended for direct use... ")