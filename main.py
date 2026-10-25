from Code import menu, grouping

def main():
    while True:
        print("===== CLI KELOMPOK =====")
        menu.show_menu()
        chose_menu = input("Pilih menu: ").strip()

        match chose_menu:
            case "0":
                print("Keluar dari program.")
                break
            case "1":
                print("Menu 1 dipilih.")
                grouping.grouping_data()
            case "2":
                print("Menu 2 dipilih.")
                grouping.show_group()  # Atau grouping.lihat_kelompok()
            case "3":
                print("Menu 3 dipilih.")
                grouping.remove_group()  # <--- Hubungkan fungsi remove dari Fahmi
            case "4":
                print("Menu 4 dipilih.")
                grouping.update_group()
            case _:
                print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()