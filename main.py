from Code import menu, grouping

def main():
    while True:
        print("===== CLI KELOMPOK =====")
      
        # show_menu() 
        menu.show_menu()
        chose_menu = input("Pilih menu: ")

        match chose_menu:
            case "0":
                print("Keluar dari program.")
                break
            case "1":
                print("Menu 1 dipilih.")
                grouping.grouping_data()
            case "2":
                print("Menu 2 dipilih.")
                grouping.show_group()
            case "3":
                print("Menu 3 dipilih.")
            case "4":
                print("Menu 4 dipilih.")
                grouping.update_group()
            case "5":
                print("Menu 5 dipilih.")
            case "6":
                print("Menu 6 dipilih.")
            case "7":
                print("Menu 7 dipilih.")
            case "8":
                print("Menu 8 dipilih.")
            case _:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
if __name__ == "__main__":
    main()


