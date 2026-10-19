from Code import processor_json

def show_menu():
    data_menu = processor_json.read_json("data/menu-list.json")
        # print("Menu:", data_menu)
    if data_menu is not None:
        for no, name in data_menu.items():
            print(f"{no}. {name}")
    else:
        print("Menu tidak tersedia karena file menu-list.json tidak ditemukan atau tidak valid.")
        