import pandas as pd
import json

class FileReader:
    def read(self, file_path):
        raise NotImplementedError("Subclasses should implement this!")

class CSVReader(FileReader):
    def read(self, file_path):
        return pd.read_csv(file_path)

class ExcelReader(FileReader):
    def read(self, file_path):
        return pd.read_excel(file_path)

class JSONReader(FileReader):
    def read(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

class FileReaderFactory:
    def get_reader(self, file_format):
        if file_format == 'csv':
            return CSVReader()
        elif file_format == 'excel':
            return ExcelReader()
        elif file_format == 'json':
            return JSONReader()
        else:
            raise ValueError(f"Unsupported file format: {file_format}")


factory = FileReaderFactory()

csv_reader = factory.get_reader('csv')
data_csv = csv_reader.read('example.csv')


excel_reader = factory.get_reader('excel')
data_excel = excel_reader.read('example.xlsx')

json_reader = factory.get_reader('json')
data_json = json_reader.read('example.json')

print(data_csv.head())
print(data_excel.head())
print(data_json)
