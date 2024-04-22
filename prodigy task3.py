{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "33ae67ec-0141-411f-a000-729275ab3072",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Contact Management System\n",
      "1. Add contact\n",
      "2. View contacts\n",
      "3. Edit contact\n",
      "4. Delete contact\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your option:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Contact Management System\n",
      "1. Add contact\n",
      "2. View contacts\n",
      "3. Edit contact\n",
      "4. Delete contact\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your option:  5\n"
     ]
    }
   ],
   "source": [
    "class Contact:\n",
    "    def __init__(self, name, phone, email):\n",
    "        self.name = name\n",
    "        self.phone = phone\n",
    "        self.email = email\n",
    "\n",
    "class ContactManagementSystem:\n",
    "    def __init__(self):\n",
    "        self.contacts = []\n",
    "        self.load_contacts()\n",
    "\n",
    "    def add_contact(self, name, phone, email):\n",
    "        new_contact = Contact(name, phone, email)\n",
    "        self.contacts.append(new_contact)\n",
    "        self.save_contacts()\n",
    "\n",
    "    def view_contacts(self):\n",
    "        for i, contact in enumerate(self.contacts, 1):\n",
    "            print(f\"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}\")\n",
    "\n",
    "    def edit_contact(self, index, name, phone, email):\n",
    "        if index < 1 or index > len(self.contacts):\n",
    "            print(\"Invalid contact index.\")\n",
    "            return\n",
    "        self.contacts[index - 1].name = name\n",
    "        self.contacts[index - 1].phone = phone\n",
    "        self.contacts[index - 1].email = email\n",
    "        self.save_contacts()\n",
    "\n",
    "    def delete_contact(self, index):\n",
    "        if index < 1 or index > len(self.contacts):\n",
    "            print(\"Invalid contact index.\")\n",
    "            return\n",
    "        del self.contacts[index - 1]\n",
    "        self.save_contacts()\n",
    "\n",
    "    def load_contacts(self):\n",
    "        try:\n",
    "            with open(\"contacts.txt\", \"r\") as file:\n",
    "                for line in file:\n",
    "                    name, phone, email = line.strip().split(\",\")\n",
    "                    self.contacts.append(Contact(name, phone, email))\n",
    "        except FileNotFoundError:\n",
    "            pass\n",
    "\n",
    "    def save_contacts(self):\n",
    "        with open(\"contacts.txt\", \"w\") as file:\n",
    "            for contact in self.contacts:\n",
    "                file.write(f\"{contact.name},{contact.phone},{contact.email}\\n\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    cms = ContactManagementSystem()\n",
    "    while True:\n",
    "        print(\"\\nContact Management System\")\n",
    "        print(\"1. Add contact\")\n",
    "        print(\"2. View contacts\")\n",
    "        print(\"3. Edit contact\")\n",
    "        print(\"4. Delete contact\")\n",
    "        print(\"5. Exit\")\n",
    "        option = int(input(\"Enter your option: \"))\n",
    "        if option == 1:\n",
    "            name = input(\"Enter name: \")\n",
    "            phone = input(\"Enter phone: \")\n",
    "            email = input(\"Enter email: \")\n",
    "            cms.add_contact(name, phone, email)\n",
    "        elif option == 2:\n",
    "            cms.view_contacts()\n",
    "        elif option == 3:\n",
    "            index = int(input(\"Enter contact index to edit: \"))\n",
    "            name = input(\"Enter new name: \")\n",
    "            phone = input(\"Enter new phone: \")\n",
    "            email = input(\"Enter new email: \")\n",
    "            cms.edit_contact(index, name, phone, email)\n",
    "        elif option == 4:\n",
    "            index = int(input(\"Enter contact index to delete: \"))\n",
    "            cms.delete_contact(index)\n",
    "        elif option == 5:\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid option. Please try again.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39f19471-a36f-4f7d-94b7-0f1c8fe8dab1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Contact Management System\n",
      "1. Add contact\n",
      "2. View contacts\n",
      "3. Edit contact\n",
      "4. Delete contact\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your option:  1\n",
      "Enter name:  meena\n",
      "Enter phone:  975287436\n",
      "Enter email:  meenamurugan157@gmail.com\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Contact Management System\n",
      "1. Add contact\n",
      "2. View contacts\n",
      "3. Edit contact\n",
      "4. Delete contact\n",
      "5. Exit\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your option:  4\n",
      "Enter contact index to delete:  975287436\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid contact index.\n",
      "\n",
      "Contact Management System\n",
      "1. Add contact\n",
      "2. View contacts\n",
      "3. Edit contact\n",
      "4. Delete contact\n",
      "5. Exit\n"
     ]
    }
   ],
   "source": [
    "class Contact:\n",
    "    def __init__(self, name, phone, email):\n",
    "        self.name = name\n",
    "        self.phone = phone\n",
    "        self.email = email\n",
    "\n",
    "class ContactManagementSystem:\n",
    "    def __init__(self):\n",
    "        self.contacts = []\n",
    "        self.load_contacts()\n",
    "\n",
    "    def add_contact(self, name, phone, email):\n",
    "        new_contact = Contact(name, phone, email)\n",
    "        self.contacts.append(new_contact)\n",
    "        self.save_contacts()\n",
    "\n",
    "    def view_contacts(self):\n",
    "        for i, contact in enumerate(self.contacts, 1):\n",
    "            print(f\"{i}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}\")\n",
    "\n",
    "    def edit_contact(self, index, name, phone, email):\n",
    "        if index < 1 or index > len(self.contacts):\n",
    "            print(\"Invalid contact index.\")\n",
    "            return\n",
    "        self.contacts[index - 1].name = name\n",
    "        self.contacts[index - 1].phone = phone\n",
    "        self.contacts[index - 1].email = email\n",
    "        self.save_contacts()\n",
    "\n",
    "    def delete_contact(self, index):\n",
    "        if index < 1 or index > len(self.contacts):\n",
    "            print(\"Invalid contact index.\")\n",
    "            return\n",
    "        del self.contacts[index - 1]\n",
    "        self.save_contacts()\n",
    "\n",
    "    def load_contacts(self):\n",
    "        try:\n",
    "            with open(\"contacts.txt\", \"r\") as file:\n",
    "                for line in file:\n",
    "                    name, phone, email = line.strip().split(\",\")\n",
    "                    self.contacts.append(Contact(name, phone, email))\n",
    "        except FileNotFoundError:\n",
    "            pass\n",
    "\n",
    "    def save_contacts(self):\n",
    "        with open(\"contacts.txt\", \"w\") as file:\n",
    "            for contact in self.contacts:\n",
    "                file.write(f\"{contact.name},{contact.phone},{contact.email}\\n\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    cms = ContactManagementSystem()\n",
    "    while True:\n",
    "        print(\"\\nContact Management System\")\n",
    "        print(\"1. Add contact\")\n",
    "        print(\"2. View contacts\")\n",
    "        print(\"3. Edit contact\")\n",
    "        print(\"4. Delete contact\")\n",
    "        print(\"5. Exit\")\n",
    "        option = int(input(\"Enter your option: \"))\n",
    "        if option == 1:\n",
    "            name = input(\"Enter name: \")\n",
    "            phone = input(\"Enter phone: \")\n",
    "            email = input(\"Enter email: \")\n",
    "            cms.add_contact(name, phone, email)\n",
    "        elif option == 2:\n",
    "            cms.view_contacts()\n",
    "        elif option == 3:\n",
    "            index = int(input(\"Enter contact index to edit: \"))\n",
    "            name = input(\"Enter new name: \")\n",
    "            phone = input(\"Enter new phone: \")\n",
    "            email = input(\"Enter new email: \")\n",
    "            cms.edit_contact(index, name, phone, email)\n",
    "        elif option == 4:\n",
    "            index = int(input(\"Enter contact index to delete: \"))\n",
    "            cms.delete_contact(index)\n",
    "        elif option == 5:\n",
    "            break\n",
    "        else:\n",
    "            print(\"Invalid option. Please try again.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef60be09-84d4-49e9-aa69-4bce8c0b1559",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
