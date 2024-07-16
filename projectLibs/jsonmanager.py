import json
import csv
from .filemanagers import FileManager
import datetime as dt

class JSONFileManager(FileManager):
    """
        FileManager sınıfından kalıtım yoluyla alınmış
        ve implement edilmiş olan sınıf
    """
    def __init__(self):
        print("JSON File Manager initialized!")

    def open_file(self, file_path: str, mode :str):
        self.file = open(file_path, mode)

    def close_file(self):
        self.file.close()

    def read_entire_file(self, file_path:str)->dict:
        with open(file_path) as jsonFile:
            return json.load(jsonFile)
        
    def read_line_from_file(self,file_path:str):
        print("Bu Fonksiyon bu dosya tipi için uygun değil")
        return None
    
    def write_to_file(self, file_path:str, data:dict):
        with open(file_path,"w") as file:
            json.dump(data, file,indent=4)

    # NOTE :def appeend_to_file function not implemented.

    def json_to_csv(self, jsonFile_path:str,\
                    csvFile_path:str):
        #TODO : Bunu mutlaka bir çalıştır ve dene... 
        """Bu fonksiyon json dosyalarını csv formatına dönüştürmek
        ve dosyaya yazmak üzere tasarlanmıştır.

        Args:
            jsonFile_path (str): Okunacak olan json dosya konumu
            csvFile_path (str): Yazılacak olan csv dosya konumu
        """

        #Json Dosyasını oku ve Dict olarak data değişkenine ata
        with open(jsonFile_path) as jsonFile:
            data = json.load(jsonFile)

        with open(csvFile_path,"w") as csvFile:
            writer = csv.writer(csvFile)
            headers = data.keys() #CSV Dosyası için başlıklar

            writer.writerow(headers)
            rows = zip(data.values())

            writer.writerows(rows)

    def replace_data(self,old_value, new_value, data):
        if isinstance(data, dict):
            new_data = {}

            for k, v in data.items():
                new_data[k] = self.replace_data(old_value, new_value, v)
            return new_data
        
        if isinstance(data, list):
            result = []
            for i in data:
                result.append(self.replace_data(old_value, new_value,i))
            return result
        
        else:
            if data == old_value:
                return new_value
            else:
                data




    def change_val_in_key(self, file_path:str,\
                          old_value, new_value):
        """JSON dosyası içinde yer alan specific gir anahtarın,
        değerini değiştirir.

        Args:
            file_path (str): json Dosya yolu
            old_value (_type_): Değiştirilecek olan Eski Değer
            new_value (_type_): Değiştirilecek olan Yeni Değer
        """

        with open(file_path) as file:
            data=json.load(file)


        updated_data = self.replace_data(old_value, new_value, data)

        with open(file_path, "w") as file:
            json.dump(updated_data,file_path)
    

    def create_file(self, file_path:str):
        with open(file_path,"w") as file:  # noqa: F841
            pass

    def delete_file(self, file_path):
        super().delete_file(file_path)

    def get_file_size(self, file_path:str)->int:
        return super().get_file_size(file_path)
    
    def get_file_creation_time(self,file_path) -> dt:
        return super().get_file_creation_time(file_path)
    
    def get_modification_time(self,file_path:str)->dt:
        return super().get_modification_time(file_path)
    
if __name__ == "__main__":
    json_manager = JSONFileManager()

    json_manager.create_file('data.json')
    
    # Writing data to JSON
    data_to_write = {
        "users": [
            {"name": "John Doe", "age": 30, "city": "New York"},
            {"name": "Jane Smith", "age": 25, "city": "Los Angeles"}
        ]
    }
    json_manager.write_to_file('data.json', data_to_write)
    json_manager.json_to_csv("data.json", "csvv.csv")
    # Reading entire JSON
    print("Reading entire JSON:")
    data_read = json_manager.read_entire_file('data.json')
    print(data_read)
    
    # Appending data to JSON
    data_to_append = {"name": "Tom Brown", "age": 40, "city": "Chicago"}
    json_manager.append_to_file('data.json', data_to_append)
    
    # Reading line from JSON (not really applicable for JSON but mimicking for consistency)
    print("\nReading single line from JSON:")
    single_line = json_manager.read_line_from_file('data.json')
    print(single_line)
    
    #json_manager.delete_file('data.json')
    print("Finished Succesfully")
