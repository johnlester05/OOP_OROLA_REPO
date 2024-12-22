class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price}"


class PhoneManager:
    def __init__(self):
        self.phones = []

    def add_phone(self, brand, model, price):
        new_phone = Phone(brand, model, price)
        self.phones.append(new_phone)
        print(f"Added: {new_phone}")

    def modify_phone(self, index, brand, model, price):
        if 0 <= index < len(self.phones):
            self.phones[index].brand = brand
            self.phones[index].model = model
            self.phones[index].price = price
            print(f"Modified: {self.phones[index]}")
        else:
            print("Invalid index.")

    def delete_phone(self, index):
        if 0 <= index < len(self.phones):
            removed_phone = self.phones.pop(index)
            print(f"Deleted: {removed_phone}")
        else:
            print("Invalid index.")

    def display_phones(self):
        if not self.phones:
            print("No phones available.")
        else:
            for i, phone in enumerate(self.phones):
                print(f"{i}: {phone}")


def main():
    manager = PhoneManager()

    while True:
        print("\nOptions: 1) Add 2) Modify 3) Delete 4) List 5) Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            price = float(input("Enter price: "))
            manager.add_phone(brand, model, price)

        elif choice == '2':
            manager.display_phones()
            index = int(input("Enter the index of the phone to modify: "))
            brand = input("Enter new brand: ")
            model = input("Enter new model: ")
            price = float(input("Enter new price: "))
            manager.modify_phone(index, brand, model, price)

        elif choice == '3':
            manager.display_phones()
            index = int(input("Enter the index of the phone to delete: "))
            manager.delete_phone(index)

        elif choice == '4':
            manager.display_phones()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
