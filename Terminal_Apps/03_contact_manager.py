class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name} | Phone: {self.phone} | Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact '{name}' added!")
    
    def show_contacts(self):
        if len(self.contacts) == 0:
            print("No contacts yet!")
        else:
            for i in range(len(self.contacts)):
                print(f"{i + 1}. {self.contacts[i]}")
    
    def search_contact(self, name):
        found = False
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                print(contact)
                found = True
        if not found:
            print("No contact found!")
    
    def remove_contact(self, index):
        if index < 1 or index > len(self.contacts):
            print("Invalid contact number!")
        else:
            removed = self.contacts.pop(index - 1)
            print(f"Contact '{removed.name}' removed!")
    
    def save_to_file(self, filename):
        file = open(filename, "w")
        for contact in self.contacts:
            file.write(f"{contact.name}|{contact.phone}|{contact.email}\n")
        file.close()
        print("Contacts saved!")
    
    def load_from_file(self, filename):
        try:
            file = open(filename, "r")
            lines = file.readlines()
            file.close()
            self.contacts = []
            for line in lines:
                parts = line.strip().split("|")
                contact = Contact(parts[0], parts[1], parts[2])
                self.contacts.append(contact)
            print("Contacts loaded!")
        except FileNotFoundError:
            print("No saved file found!")
    
    def __len__(self):
        return len(self.contacts)
    
    def __str__(self):
        return f"ContactManager: {len(self.contacts)} contacts"

manager = ContactManager()

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Save to File")
    print("6. Load from File")
    print("q. Quit")
    
    choice = input("Choose: ")
    
    if choice == "q":
        print("Goodbye!")
        break
    
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        manager.add_contact(name, phone, email)
    elif choice == "2":
        manager.show_contacts()
    elif choice == "3":
        name = input("Search name: ")
        manager.search_contact(name)
    elif choice == "4":
        manager.show_contacts()
        try:
            index = int(input("Contact number to remove: "))
            manager.remove_contact(index)
        except ValueError:
            print("Please enter a number!")
    elif choice == "5":
        manager.save_to_file("contacts.txt")
    elif choice == "6":
        manager.load_from_file("contacts.txt")
    else:
        print("Invalid choice!")