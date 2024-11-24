contacts = {}

while True:
    print("\n1. Add a Contact")
    print("2. Update a Contact")
    print("3. Delete a Contact")
    print("4. Search for a Contact")
    print("5. Display All Contacts")
    print("6. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        name = input("Enter the contact name: ")
        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter the phone number: ")
            contacts[name] = phone
            print("Contact added successfully!")
    
    elif ch == 2:
        name = input("Enter the contact name to update: ")
        if name in contacts:
            phone = input("Enter the new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")
    
    elif ch == 3:
        name = input("Enter the contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    
    elif ch == 4:
        name = input("Enter the contact name to search: ")
        if name in contacts:
            print("Name:", name)
            print("Phone Number:", contacts[name])
        else:
            print("Contact not found!")
    
    elif ch == 5:
        if contacts:
            print("\nAll Contacts:")
            for name, phone in contacts.items():
                print("Name: ",name)
                print("Phone Number:", phone)
        else:
            print("No contacts found!")
    
    elif ch == 6:
        print("Exiting the program")
        break
    
    else:
        print("Invalid choice! Please try again.")
