import csv
import json
from .filemanagers import FileManager
import datetime as dt

class CSVFileManager(FileManager):
    """
        CSV Dosyalarını işlemek üzere oluşturulan ve
        FileManager dan implement edilen sınıf
    """
    def __init__(self):
        print("CSV File Manager initialized!")

    def open_file(self, file_path:str, mode:str):
        self.file = open(file_path, mode, newline="")

    def close_file(self):
        if self.file:
            self.file.close()

    def read_entire_file(self,file_path:str)->list:
        data = []
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            for row in content:
                data.append(row)
        return data

    def read_line_from_file(self, file_path:str)->list:
        """ Bu fonksiyon csv dosyasının sadece başlıklarını verir"""
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            return next(content)
    
    #BUG : Bu fonksiyon farklı caseler için sorun çıkarıyor!
    def write_to_file(self, file_path:str, data:list):
        with open(file_path, "w", newline="") as csv_file:
            content = csv.writer(csv_file)
            content.writerows(data)

    #BUG : Bu fonksiyon farklı caseler için sorun çıkarıyor!
    def append_to_file(self, file_path:str, data:list):
        with open(file_path, "a", newline="") as csv_file:
            content=csv.writer(csv_file)
            content.writerow(data)
    
    def csv_to_json(self,csv_file_path:str,json_file_path:str):
        """
            CSV dosyalarını, json formatına dönüştüren fonksiyon
        """
        #TODO : burda patlak olma ihtimali var. Bug a açık dosya.
        # Just calling a function returning the first line may cause problems. 
        # Keep eye on this staff

        data = {}
        headers = self.read_line_from_file(csv_file_path)
        for header in headers:
            data[header] = []

        with open(csv_file_path,newline="") as csv_file:
            content=csv.reader(csv_file)

            for i, row in enumerate(content):
                if i == 0 :
                    continue
                for key_, value_ in zip(headers,row):
                    data[key_].append(value_)

        with open(json_file_path, "w", newline="") as json_file:
            json.dump(data,json_file,indent=4)
    
    #BUG : Bu fonksiyon eksik kalmış!
    def update_value_in_cell(self, file_path:str,value_to_replace:str,new_value:str):
        """
         Değiştirilecek olan değerin konumunu bulacak ve yeni ifade ile değiştirecek olan fonksiyon.
        """
        with open(file_path) as file :
            content = file.read()
        content = content.replace(value_to_replace, new_value)

        with open(file_path, "w") as file:
            file.writelines(content)

    #BUG : 
    def update_cell_by_ref(self,
                           file_path:str,
                           reference_col:str, #Bilginin eşsiz bilgisini alacağımız kolon
                           col_to_change:str, #Bilginin değiştirileceği kolon
                           reference_val:str, #Eşsiz Anahtar Kelime - aradığımız değer için
                           new_val:str):
    
        """_summary_

        @param :
            file_path : Değişiklik yapılacak olan dosyanın yolu
            reference_col : Anahtar kelimenin aranacağı sütun
            col_to_change : Değiştirilecek olan bilginin yer aldığı sütun
            reference_val : Hangi anahtar kelimeye ait alt bilginin değiştirileceğine dair 
            new_val : Hücreye yazılacak olan yeni veri. 
        """
        data = []
        ref_row_index = 0
        ref_col_index = 0
        
        with open(file_path,newline="") as csv_file:
            content = csv.reader(csv_file)
            headers = next(content)

            ref_row_index = headers.index(reference_col)
            ref_col_index = headers.index(col_to_change)
            print("row : ",ref_row_index, "col : ", ref_col_index)
            data.append(headers)

            for row in content:
                for cell in row:
                    if cell == reference_val:
                            row[ref_col_index] = new_val
                            print(row[ref_col_index],new_val)
                data.append(row)

        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)

    def delete_file(self, file_path:str):
        super().delete_file(file_path)

    def get_file_size(self, file_path:str)->int:
        return super().get_file_size(file_path)

    def get_file_creation_time(self, file_path:str)->dt:
        return super().get_file_creation_time(file_path)
    
    def get_modification_time(self,file_path:str)->dt:
        return super().get_modification_time(file_path)
    
if __name__ == "__main__":

    testlist = [["Adi", "Soyadi", "tlf no", "parça no", "kim ki"],
                ["Deniz", "Aydan", "Cabbar", "nergiz", "Rahime"]]
    
    liste_To_add = ["Denz", "Aydn", "Cabar", "nerz", "Rahe"]
    csvmanager = CSVFileManager()
    csvmanager.write_to_file("deneme.csv",testlist)

    csvmanager.append_to_file("deneme.csv", liste_To_add)

    print(csvmanager.read_line_from_file("deneme.csv"))

    csvmanager.csv_to_json("deneme.csv","deneme.json")

    #BUGGY
    csvmanager.update_value_in_cell("deneme.csv","Denz","Ebru")

    csvmanager.update_cell_by_ref("deneme.csv","Adi","tlf no","Denz","kimene")