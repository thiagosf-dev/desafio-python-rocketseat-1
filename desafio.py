class Person:
    def __init__(self, name) -> None:
        self.__name = name
        self.__isFavorite = False

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_isFavorite(self):
        return self.__isFavorite

    def set_isFavorite(self, isFavorite):
        self.__isFavorite = isFavorite


class Contact(Person):
    def __init__(self, name, email, phone) -> None:
        super().__init__(name)
        self.__email = email
        self.__phone = phone

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone


def add_contact(contacts):
    name = input("\nEnter the contact's name: ")
    email = input("Enter the contact's email: ")
    phone = input("Enter the contact's phone number: ")
    isFavorite = input(f"To favorite (y/n): ")
    contact = Contact(name, email, phone)
    contact.set_isFavorite(isFavorite.lower() == "y")
    contacts.append(contact)
    print("\nContact added successfully!\n")


def list_contacts(contacts):
    if len(contacts) == 0:
        print("\n⚠ No contact registered at the moment.")
    else:
        for index, contact in enumerate(contacts):
            print(f"---")
            print(f"Contact ID: {index + 1}:")
            print(f"Name: {contact.get_name()}")
            print(f"Email: {contact.get_email()}")
            print(f"Phone: {contact.get_phone()}")
            print(f"Favorite: {'Yes' if contact.get_isFavorite() else 'No'}")
            print(f"---")
    return


def remove_contact(contacts):
    contact_id = int(
        input("📝 Enter the contact ID you want to remove or '0' to return to the options menu:\n👉 ")
    )
    if contact_id == 0:
        return
    while not 0 <= contact_id - 1 < len(contacts):
        print("\n⚠ Contact not found.")
        contact_id = int(
            input(
                "\n📝 Enter the contact ID you want to remove or '0' to return to the options menu:\n👉 ")
        )
        if contact_id == 0:
            return
    contacts.pop(contact_id - 1)
    print("Contact removed successfully!\n")
    return


def edit_contact(contacts):
    contact_id = int(
        input("\n📝 Enter the contact ID you want to edit or '0' to return to the options menu:\n👉 "))
    if contact_id == 0:
        return
    while not 0 <= contact_id - 1 < len(contacts):
        print("\n⚠ Contact not found.")
        contact_id = int(
            input(
                "\n📝 Enter the contact ID you want to edit or '0' to return to the options menu:\n👉 "))
        if contact_id == 0:
            return
    contact = contacts[contact_id - 1]
    contact_name = input("Enter the new contact's name: ")
    contact_email = input("Enter the new contact's email: ")
    contact_phone = input("Enter the new contact's phone number: ")
    contact_favorite = input(f"To favorite (y/n): ")
    contact.set_name(contact_name)
    contact.set_email(contact_email)
    contact.set_phone(contact_phone)
    if contact_favorite.lower() == "y":
        contact.set_isFavorite(True)
    else:
        contact.set_isFavorite(False)
    print("\nContact edited successfully!")
    return


def list_favorites(contacts):
    total = 0
    for contact in contacts:
        print(f"\nFavorite Contacts:")
        if contact.get_isFavorite():
            total += 1
            print(f"---")
            print(f"Name: {contact.get_name()}")
            print(f"Email: {contact.get_email()}")
            print(f"Phone: {contact.get_phone()}")
            print(f"---")
    if total == 0:
        print("\n⚠ No favorite contact registered at the moment.")
    return


contacts = []

while True:
    print("\nOPTIONS:")
    print("1 - List Contacts")
    print("2 - Add Contact")
    print("3 - Remove Contact")
    print("4 - Edit Contact")
    print("5 - View Favorite Contacts")
    print("6 - Exit")
    option = input("\nChoose an option: ")

    if option == "1":
        list_contacts(contacts)
    elif option == "2":
        add_contact(contacts)
    elif option == "3":
        remove_contact(contacts)
    elif option == "4":
        edit_contact(contacts)
    elif option == "5":
        list_favorites(contacts)
    elif option == "6":
        print("\n🚧 Exiting the Contact Manager...")
        break
    else:
        print("\n🚫 Invalid option. Please choose a valid option.")

print("🎉 Program successfully finished. Thank you for using our software 😎\n")
