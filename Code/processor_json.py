import json
# import os
# print(os.getcwd())
# print(os.path.exists("data/menu-list.json"))

def read_json(nama_file):
    try:
        with open(nama_file, "r") as file:
            data = json.load(file) 
        return data 
    except FileNotFoundError:
        print(f"Error: File '{nama_file}' tidak ditemukan.")
        return None 
    except json.JSONDecodeError:
        print(f"Error: File '{nama_file}' tidak valid.")
        return None