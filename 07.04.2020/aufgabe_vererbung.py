class FileReader():
    def __init__(self,file_):
        self.file_ = file_
    
    def lines(self):
        array = []
        with open(self.file_,"r") as file:
            for line in file:
                array.append(line.strip())
        return array

class CsvReader(FileReader):
    def __init__(self,file):
        super().__init__(file)
    
    def lines(self):
         return [list.split(",") for list in super().lines()]

f = CsvReader("datei.csv")
print(f.lines())