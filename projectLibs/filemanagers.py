from abc import ABC, abstractmethod
import os
import datetime as dt

class FileManager(ABC):
    """
        Alt sınıflar için Soyut Sınıf tanımı
    """
    def __init__(self):
        super().__init__()

    @abstractmethod
    def open_file(self, filePath:str, mode:str):
        """
        Args:
            filePath (str): Acılacak olan dosya yol
            mode (str): dosya açma metodu
        """
        pass

    @abstractmethod
    def close_file(self):
        """
            Acılan dosyayı kapatmak amacıyla kullanılacak fonksiyon
        """
        pass

    @abstractmethod
    def read_entire_file(self,file_path:str)-> str:
        """_summary_

        Args:
            file_path (str): Acılacak olan dosyanın yolu

        Returns:
            str: Dosyanın içeriğini göndürür
        """
        pass

    def read_line_from_file(self, file_path:str)->str:
        """_summary_

        Args:
            file_path (str): Acılacak olan dosyanın yolu

        Returns:
            str: Dosyadan okunan tek bir satır döndürür
        """
        pass

    @abstractmethod
    def write_to_file(self, file_path:str, data:str):
        """_summary_

        Args:
            file_path (_type_): Acılacak olan dosyanın yolu
            data (str): dosyaya yazılarcak olan bilgi
        """
        pass

    
    def append_to_file(self, file_path:str, data:str):
        """_summary_

        Args:
            file_path (str): Acılacak olan dosya
            data (str): Yazılacak olan bilgi
        """
        pass

    def delete_file(self,file_path:str):
        """Dosyayı tamamı ile siler

        Args:
            file_path (str): silinecek olan dosya yolu
        """
        try:
            os.remove(file_path)
        except Exception as e:
            print(str(e), "Dosya silme hatası")

    def get_file_size(self, file_path:str)->int:
        """Dosya boyutu okuma

        Args:
            file_path (str): Dosya boyutu alınacak olan eleman

        Returns:
            int: Dosya boyutu
        """
        return os.path.getsize(file_path)
    
    def get_file_creation_time(self,file_path) -> dt:
        """Dosyanın Oluşturulma zamanının döner

        Args:
            file_path (_type_): Dosya yolunu belirtir

        Returns:
            datetime: Dosyanın oluşturulduğu tarih ve ssati döner
        """

        return dt.datetime.fromtimestamp(os.path.getctime(file_path))
    
    def get_modification_time(self,file_path:str)->dt:
        """Dosya değiştirilme tarih ve ssati

        Args:
            file_path (str): Dosya yolu

        Returns:
            dt: Dosyanın değiştirilme tarih ve saatini verir
        """

        return dt.datetime.fromtimestamp(os.path.getmtime(file_path))
    
if __name__ == "__main__":
    print("Bu dosya direk olarak çalıştırmak için yaratılmadı. Git bir yerden import et!")