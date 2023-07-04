import csv

def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data_list = []
        datas = csv.DictReader(file, skipinitialspace=True)
        for data in datas:
            data_list.append(data)
    return data_list