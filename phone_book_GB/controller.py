import model
import view

# def main_menu():

def phone_book():

    choice = view.menu()
    if choice == 2:
        model.new_entry()
    elif choice == 3:
        model.buffer()
    elif choice == 4:
        model.export_entry()
