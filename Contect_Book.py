contacts = []
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email id")
    address = input("Enter address: ")
    contacts.append({
        "name" : name,
        "phone" : phone,
        "email" : email,
        "address": address
    })

    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        print("\n--- Contact List---")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
       if keyword in contact["name"].lower() or keyword in contact["phone"]:
           print(f"Name: {contact['name']}")
           print(f"Phone: {contact['phone']}")
           print(f"Email: {contact['email']}")
           print(f"Address: {contact['address']}")
           print("-"  * 20)
           found = True
    if not found:
        print("No contact found.")

def update_contact():
    view_contacts()
    try:
        idx = int(input("Enter contact number to update: ")) -1
        if 0 <= idx < len(contacts):
            contacts[idx]["name"] = input("Enter new name: ")
            contacts[idx]["phone"] = input("Enter new phone: ")
            contacts[idx]["email"] = input("Enter new email: ")
            contacts[idx]["address"] = input("Enter new address: ")
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("please enter a valid number.")

def delete_contact():
    view_contacts()
    try:
        idx = int(input("Enter contact number to delete: "))-1
        if 0 <= idx < len(contacts):
            contacts.pop(idx)
            print("Contact delete successfully!")
        else:
            print("Please enter a valid number.")

    except ValueError:
        print("Please enter a valid number.")
        

while True:
    print("\n==== CONTACT BOOK MENU ====")
    print("1. Add Contact")
    print("2.View Contact List")
    print("3 Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")


